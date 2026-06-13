import json

# Load history
with open("history.json", "r") as f:
    history = json.load(f)

if len(history) < 3:
    print("Need at least 3 history points for prediction.")
    exit()

# Extract battery temperatures
temps = [entry["data"]["battery_temperature"] for entry in history]

# Temperature trend calculation
change_rate = (temps[-1] - temps[0]) / (len(temps) - 1)

# Load current hardware state
with open("hardware_state.json", "r") as f:
    hardware = json.load(f)

# RAM pressure %
ram_total = hardware["ram_total_kb"]
ram_free = hardware["ram_free_kb"]

ram_usage_percent = ((ram_total - ram_free) / ram_total) * 100

prediction = {}

# Multi-factor prediction logic
if change_rate > 1.0 or ram_usage_percent > 85:

    risk_score = 0

    if change_rate > 1:
        risk_score += 40

    if ram_usage_percent > 85:
        risk_score += 40

    if temps[-1] > 40:
        risk_score += 20

    prediction = {
        "current_temp": temps[-1],
        "temp_rise_rate": round(change_rate, 2),
        "ram_usage_percent": round(ram_usage_percent, 2),
        "predicted_failure_risk": risk_score,
        "risk": "HIGH"
    }

else:

    prediction = {
        "current_temp": temps[-1],
        "ram_usage_percent": round(ram_usage_percent, 2),
        "risk": "LOW"
    }

print("Advanced Prediction Engine:")
print(prediction)