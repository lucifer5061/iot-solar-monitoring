import sys, json, joblib
import numpy as np

# Load your trained model
model = joblib.load("C:/iot-solar-monitoring/model/clean_predictor.pkl")

# Read incoming JSON string from argv[1]
data = json.loads(sys.argv[1])

# Build feature vector using only the 5 features the model expects
X = np.array([[ 
    data['voltage'],
    data['current'],
    data['temperature'],
    data['irradiance'],
    data['dust_level']
]])

# Predict days until next cleaning
pred = model.predict(X)[0]

# Print as integer
print(int(round(pred)))
