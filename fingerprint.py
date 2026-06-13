import json
import hashlib

# Load hardware state
with open("hardware_state.json", "r") as f:
    data = json.load(f)

# Combine unique hardware fields
fingerprint_string = (
    str(data["device_model"]) +
    str(data["android_version"]) +
    str(data["cpu_cores"]) +
    str(data["ram_total_kb"])
)

# Generate SHA256 fingerprint
device_fingerprint = hashlib.sha256(
    fingerprint_string.encode()
).hexdigest()

result = {
    "device_fingerprint": device_fingerprint
}

# Save result
with open("fingerprint.json", "w") as f:
    json.dump(result, f, indent=4)

print("Fingerprint generated.")
print(result)