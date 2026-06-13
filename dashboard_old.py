import streamlit as st
import json

st.title("Hardware Sentinel AI Dashboard")

try:
    with open("hardware_state.json", "r") as f:
        data = json.load(f)

    with open("health_report.json", "r") as f:
        health = json.load(f)

    ram_used_percent = ((data["ram_total_kb"] - data["ram_free_kb"]) / data["ram_total_kb"]) * 100

    st.metric("Battery Temperature", data["battery_temperature"])
    st.metric("RAM Usage %", round(ram_used_percent, 2))
    st.metric("Battery Health Score", health["device_health_score"])
    st.metric("Risk Level", health["risk_level"])

except Exception as e:
    st.error(f"Error: {e}")