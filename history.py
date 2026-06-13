import json
import os
from datetime import datetime

# Load current hardware state
with open("hardware_state.json", "r") as f:
    current = json.load(f)

entry = {
    "timestamp": str(datetime.now()),
    "data": current
}

history_file = "history.json"

# If file exists, load old history
if os.path.exists(history_file):
    with open(history_file, "r") as f:
        history = json.load(f)
else:
    history = []

# Add new record
history.append(entry)

# Save updated history
with open(history_file, "w") as f:
    json.dump(history, f, indent=4)

print("History updated.")