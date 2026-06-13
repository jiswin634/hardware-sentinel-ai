import json


# Read collected hardware data
with open("hardware_state.json", "r") as f:
    data = json.load(f)


score = 100
issues = []


# Battery checks
if data["battery_temperature"] > 40:
    score -= 20
    issues.append("High battery temperature")


if data["battery_level"] < 15:
    score -= 10
    issues.append("Low battery level")


# RAM pressure check
if data["ram_free_kb"] < 150000:
    score -= 15
    issues.append("Low free RAM")


# CPU sanity check
if data["cpu_cores"] < 4:
    score -= 10
    issues.append("Low CPU core count")


# Risk classification
if score >= 85:
    risk = "LOW"

elif score >= 60:
    risk = "MEDIUM"

else:
    risk = "HIGH"


result = {
    "device_health_score": score,
    "risk_level": risk,
    "issues": issues
}


# Save result
with open("health_report.json", "w") as f:
    json.dump(result, f, indent=4)


print("Health scoring complete.")
print(result)