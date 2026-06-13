import json

with open("history.json", "r") as f:
    history = json.load(f)

if len(history) < 2:
    print("Not enough history for trend analysis.")
    exit()

latest = history[-1]["data"]
previous = history[-2]["data"]

warnings = []

if latest["battery_temperature"] > previous["battery_temperature"]:
    warnings.append("Battery temperature rising over time")

if latest["ram_free_kb"] < previous["ram_free_kb"]:
    warnings.append("Available RAM decreasing")

if warnings:
    print("Trend warnings:")
    for w in warnings:
        print("-", w)
else:
    print("No negative trend detected.")