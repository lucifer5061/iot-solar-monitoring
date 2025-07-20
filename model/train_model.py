import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

# Load prepared data
df = pd.read_csv("prepared.csv")

# Select features and target
features = ['voltage', 'current', 'temperature', 'irradiance', 'dust_level']
target = 'days_to_clean'

X = df[features]
y = df[target]

# Split into training and test data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train a Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"✅ Model trained. MAE: {mae:.2f} days")

# Save the model
joblib.dump(model, "clean_predictor.pkl")
print("📦 Model saved as 'clean_predictor.pkl'")
