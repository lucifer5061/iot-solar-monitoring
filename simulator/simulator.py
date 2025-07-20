import time, random, json, math
import paho.mqtt.client as mqtt

# ─── CONFIGURATION ────────────────────────────────────────
BROKER       = "broker.hivemq.com"
PORT         = 1883
TOPIC        = "solar/data"
PUBLISH_SEC  = 3                # 3 real‑seconds ≡ 1 simulated day

# Area dustiness: False = twice/year cleaning, True = quarterly cleaning
DUSTY_AREA   = False

# Cleaning schedule (in simulated days)
DAYS_PER_MONTH      = 30
if DUSTY_AREA:
    CLEAN_INTERVAL_DAYS = 3 * DAYS_PER_MONTH    # every 3 months
else:
    CLEAN_INTERVAL_DAYS = 6 * DAYS_PER_MONTH    # every 6 months

# Dust parameters
LOW_DUST     = 1              # start at 1 %
HIGH_DUST    = 95              # cap at 95 %
DUST_STEP_CHOICES = [2,3,5,7]  # % increase per day

# Panel MPP (500 W, 12–14 V panel)
V_CLEAN_MIN  = 12.0
V_CLEAN_MAX  = 14.0
I_CLEAN_MIN  = 35.0
I_CLEAN_MAX  = 42.0

# Seasonal irradiance (yearly sinusoid)
IRR_MEAN     = 1000.0
IRR_AMP      = 200.0

# Sensor noise
NOISE_VOL_STD= 0.005
NOISE_CUR_STD= 0.005

# ─── MQTT SETUP ──────────────────────────────────────────
client = mqtt.Client(client_id="solar_simulator")
client.connect(BROKER, PORT)
print(f"Connected to MQTT broker at {BROKER}:{PORT}")

# Simulation state
dust_level = LOW_DUST
day_count  = 0

def generate_data():
    global dust_level, day_count
    day_count += 1

    # Scheduled cleaning
    if day_count > 0 and day_count % CLEAN_INTERVAL_DAYS == 0:
        dust_level = LOW_DUST
    else:
        # Dust accumulation (variable step)
        step = random.choice(DUST_STEP_CHOICES)
        dust_level = min(dust_level + step, HIGH_DUST)

    # Seasonal base irradiance (365‑day cycle)
    seasonal = IRR_MEAN + IRR_AMP * math.sin(2 * math.pi * day_count / 365)

    # Add daily randomness
    base_irradiance = max(0.0, seasonal + random.uniform(-50, 50))

    # Effective irradiance after dust
    eff_irradiance  = base_irradiance * (1 - dust_level / 100)

    # Clean‑panel MPP voltage & current
    V_clean = random.uniform(V_CLEAN_MIN, V_CLEAN_MAX)
    I_clean = random.uniform(I_CLEAN_MIN, I_CLEAN_MAX)

    # Scale by irradiance ratio
    ratio   = eff_irradiance / base_irradiance if base_irradiance>0 else 0
    voltage = V_clean * (ratio ** 0.1)    # gentle voltage drop
    current = I_clean * ratio             # linear current drop

    # Add sensor noise
    voltage *= (1 + random.gauss(0, NOISE_VOL_STD))
    current *= (1 + random.gauss(0, NOISE_CUR_STD))

    # Temperature (random 30–50 °C)
    temperature = random.uniform(30.0, 50.0)

    return {
        "voltage":     round(voltage, 2),
        "current":     round(current, 2),
        "temperature": round(temperature, 1),
        "irradiance":  round(eff_irradiance, 1),
        "dust_level":  dust_level,
        "day":         day_count
    }

# ─── MAIN LOOP ────────────────────────────────────────────
try:
    while True:
        msg = json.dumps(generate_data())
        client.publish(TOPIC, msg)
        print("Published:", msg)
        time.sleep(PUBLISH_SEC)

except KeyboardInterrupt:
    print("\nStopped simulator. Next start resets dust_level and day_count.")
