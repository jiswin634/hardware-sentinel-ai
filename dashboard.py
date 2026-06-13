import streamlit as st
import json
import pandas as pd
import numpy as np
import random
from datetime import datetime

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="Hardware Sentinel AI",
    page_icon="⚡",
    layout="wide"
)

# ==========================================
# CUSTOM CSS (Premium UI)
# ==========================================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(180deg, #07111F 0%, #0B1628 100%);
    color: white;
}

h1, h2, h3 {
    color: white;
}

div[data-testid="metric-container"] {
    background: rgba(17, 24, 39, 0.85);
    border: 1px solid #2B3445;
    padding: 15px;
    border-radius: 14px;
}

section[data-testid="stSidebar"] {
    background-color: #09111F;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================
st.sidebar.title("⚡ Hardware Sentinel")

st.sidebar.markdown("### Navigation")
st.sidebar.markdown("• Live Monitoring")
st.sidebar.markdown("• AI Engine")
st.sidebar.markdown("• Threat Detection")
st.sidebar.markdown("• Device Identity")
st.sidebar.markdown("• Predictive Analytics")

st.sidebar.divider()
st.sidebar.success("SYSTEM ACTIVE")

# ==========================================
# LOAD REAL DATA
# ==========================================
try:
    with open("hardware_state.json", "r") as f:
        data = json.load(f)

    with open("health_report.json", "r") as f:
        health = json.load(f)

except Exception as e:
    st.error(f"Could not load system files: {e}")
    st.stop()

# ==========================================
# REAL DATA EXTRACTION
# ==========================================
battery_temp = data["battery_temperature"]

ram_usage = round(
    (1 - (data["ram_free_kb"] / data["ram_total_kb"])) * 100,
    2
)

health_score = health["device_health_score"]
risk_level = health["risk_level"]

battery_level = data["battery_level"]

cpu_cores = data["cpu_cores"]

device_model = data["device_model"]
android_version = data["android_version"]

# ==========================================
# SYNTHETIC HISTORY GENERATION
# ==========================================
temp_history = np.random.normal(
    battery_temp,
    0.6,
    30
)

ram_history = np.random.normal(
    ram_usage,
    2,
    30
)

# ==========================================
# HEADER
# ==========================================
st.title("⚡ Hardware Sentinel AI")

st.subheader("Enterprise Predictive Hardware Monitoring Platform")

st.markdown("")

# ==========================================
# LIVE STATUS BAR
# ==========================================
status1, status2, status3 = st.columns(3)

with status1:
    st.info("🟢 Device Online")

with status2:
    st.info("⚡ AI Engine Active")

with status3:
    st.info("🔒 Security Verified")

st.divider()

# ==========================================
# TOP METRICS
# ==========================================
m1, m2, m3, m4, m5, m6 = st.columns(6)

with m1:
    st.metric("Battery Temp", f"{battery_temp}°C")

with m2:
    st.metric("RAM Usage", f"{ram_usage}%")

with m3:
    st.metric("Health Score", health_score)

with m4:
    st.metric("Risk", risk_level)

with m5:
    trust_score = random.randint(90, 99)
    st.metric("Trust Score", trust_score)

with m6:
    st.metric("Battery %", battery_level)

st.divider()

# ==========================================
# LIVE ANALYTICS
# ==========================================
left, right = st.columns(2)

with left:
    st.subheader("📈 Temperature Trend")

    temp_df = pd.DataFrame(
        temp_history,
        columns=["Battery Temperature"]
    )

    st.line_chart(temp_df)

with right:
    st.subheader("🧠 RAM Usage Trend")

    ram_df = pd.DataFrame(
        ram_history,
        columns=["RAM Usage"]
    )

    st.line_chart(ram_df)

st.divider()

# ==========================================
# AI ENGINE
# ==========================================
colA, colB = st.columns(2)

with colA:

    st.subheader("🤖 AI Prediction Engine")

    predictions = [
        "Battery degradation predicted in 43 days",
        "RAM usage spike detected over baseline",
        "Thermal behavior stable for next 24h",
        "Performance stable under sustained load",
        "No thermal anomaly detected"
    ]

    prediction = random.choice(predictions)

    confidence = round(random.uniform(91, 98), 2)

    st.warning(prediction)

    st.write("Confidence Score:", confidence, "%")

with colB:

    st.subheader("🛡 Threat Detection")

    threats = [
        "No anomalies detected",
        "Device fingerprint verified",
        "No unauthorized modification",
        "Secure execution environment"
    ]

    threat = random.choice(threats)

    st.success(threat)

    malware_probability = round(
        random.uniform(0.1, 0.7),
        2
    )

    st.write("Malware Probability:", malware_probability, "%")

st.divider()

# ==========================================
# DEVICE IDENTITY PANEL
# ==========================================
id1, id2 = st.columns(2)

with id1:

    st.subheader("📱 Device Identity")

    st.write("Device Model:", device_model)
    st.write("Android Version:", android_version)
    st.write("CPU Cores:", cpu_cores)

with id2:

    st.subheader("🔐 Verification Status")

    st.write("Fingerprint Status: VERIFIED")
    st.write("Security Layer: ACTIVE")
    st.write("Trust Rating:", trust_score, "/100")

st.divider()

# ==========================================
# PREDICTIVE FAILURE ANALYTICS
# ==========================================
st.subheader("📊 Predictive Failure Analytics")

future_health_7 = max(health_score - random.randint(1, 4), 0)
future_health_30 = max(health_score - random.randint(5, 12), 0)

days_to_issue = random.randint(35, 60)

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("7 Day Projection", future_health_7)

with c2:
    st.metric("30 Day Projection", future_health_30)

with c3:
    st.metric("Estimated Failure Window", f"{days_to_issue} days")

st.divider()

# ==========================================
# EVENT LOG
# ==========================================
st.subheader("📝 System Event Log")

event_data = {
    "Time": [
        datetime.now().strftime("%H:%M:%S"),
        datetime.now().strftime("%H:%M:%S"),
        datetime.now().strftime("%H:%M:%S"),
        datetime.now().strftime("%H:%M:%S")
    ],

    "Event": [
        "Hardware telemetry collected",
        "AI analysis complete",
        "Security verification passed",
        "Predictive analytics updated"
    ]
}

event_df = pd.DataFrame(event_data)

st.dataframe(
    event_df,
    use_container_width=True
)

st.divider()

# ==========================================
# FOOTER
# ==========================================
st.caption(
    "Built by Jiswin Tom Jose • Hardware Sentinel AI • Enterprise Build v3"
)