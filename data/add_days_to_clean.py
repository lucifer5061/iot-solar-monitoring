import pandas as pd

# Load the original log.csv
df = pd.read_csv("log.csv")

# Number of rows (used as simulated days passed)
total_rows = len(df)

# Simulate a cleaning every 30 days (adjust this if needed)
cleaning_interval = 30

# Create a list to hold 'days_to_clean'
days_to_clean = []

# Loop through each row and calculate days remaining until next cleaning
for i in range(total_rows):
    days_passed = i % cleaning_interval
    days_remaining = cleaning_interval - days_passed
    days_to_clean.append(days_remaining)

# Add the new column
df["days_to_clean"] = days_to_clean

# Save the new CSV
df.to_csv("prepared.csv", index=False)

print("✅ 'prepared.csv' created with 'days_to_clean' column added.")