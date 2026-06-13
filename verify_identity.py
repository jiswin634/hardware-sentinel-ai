import json
import hashlib
import os

# Load current hardware state
with open("hardware_state.json", "r") as f:
    data = json.load(f)

# Generate current fingerprint
fingerprint_string = (
    str(data["device_model"]) +
    str(data["android_version"]) +
    str(data["cpu_cores"]) +
    str(data["ram_total_kb"])
)

current_fingerprint = hashlib.sha256(
    fingerprint_string.encode()
).hexdigest()

# Check if baseline exists
if not os.path.exists("baseline_fingerprint.json"):

    with open("baseline_fingerprint.json", "w") as f:
        json.dump(
            {"device_fingerprint": current_fingerprint},
            f,
            indent=4
        )

    print("Baseline fingerprint created.")

else:

    with open("baseline_fingerprint.json", "r") as f:
        baseline = json.load(f)

    if baseline["device_fingerprint"] == current_fingerprint:
        print("Identity verified. Device unchanged.")

    else:
        print("WARNING: Hardware identity changed.")