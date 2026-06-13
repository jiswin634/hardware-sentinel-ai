import subprocess
import json
import re


def adb(command):
    result = subprocess.run(
        f'"C:\\Users\\USER\\Downloads\\platform-tools-latest-windows\\platform-tools\\adb.exe" {command}',
        shell=True,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()


print("Collecting hardware data...")


battery_raw = adb("shell dumpsys battery")
cpu_raw = adb("shell cat /proc/cpuinfo")
memory_raw = adb("shell cat /proc/meminfo")


# BATTERY PARSER
battery_level = re.search(r"level: (\d+)", battery_raw)
battery_temp = re.search(r"temperature: (\d+)", battery_raw)
battery_status = re.search(r"status: (\d+)", battery_raw)


# CPU PARSER
cpu_cores = cpu_raw.count("processor")


# MEMORY PARSER
mem_total = re.search(r"MemTotal:\s+(\d+)", memory_raw)
mem_free = re.search(r"MemFree:\s+(\d+)", memory_raw)


data = {
    "battery_level": int(battery_level.group(1)) if battery_level else None,
    "battery_temperature": int(battery_temp.group(1))/10 if battery_temp else None,
    "battery_status": battery_status.group(1) if battery_status else None,
    "cpu_cores": cpu_cores,
    "ram_total_kb": int(mem_total.group(1)) if mem_total else None,
    "ram_free_kb": int(mem_free.group(1)) if mem_free else None,
    "device_model": adb("shell getprop ro.product.model"),
    "android_version": adb("shell getprop ro.build.version.release")
}


with open("hardware_state.json", "w") as f:
    json.dump(data, f, indent=4)


print("Structured collection complete.")