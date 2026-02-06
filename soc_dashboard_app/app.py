import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="SOC Dashboard Suite", layout="wide")

st.title("🛡️ SOC Dashboard — Threat Monitoring Overview")

# --- Paths ---
BASE_PATH = Path(__file__).resolve().parents[1] / "data" / "dashboard"

# --- Load Data ---
alerts_by_priority = pd.read_csv(BASE_PATH / "alerts_by_priority.csv")
alerts_over_time = pd.read_csv(BASE_PATH / "alerts_over_time.csv")
alerts_by_rule = pd.read_csv(BASE_PATH / "alerts_by_detection_rule.csv")
alerts_by_role = pd.read_csv(BASE_PATH / "alerts_by_user_role.csv")
top_risky_domains = pd.read_csv(BASE_PATH / "top_risky_domains.csv")
priority_rule_matrix = pd.read_csv(BASE_PATH / "priority_vs_rule_matrix.csv", index_col=0)

# --- Layout ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔔 Alerts by Priority")
    st.bar_chart(alerts_by_priority.set_index("priority"))

with col2:
    st.subheader("📅 Alerts Over Time")
    st.line_chart(alerts_over_time.set_index("date"))

st.divider()

col3, col4 = st.columns(2)

with col3:
    st.subheader("🧠 Alerts by Detection Rule")
    st.bar_chart(alerts_by_rule.set_index("detection_rule"))

with col4:
    st.subheader("👤 Alerts by User Role")
    st.bar_chart(alerts_by_role.set_index("user_role"))

st.divider()

col5, col6 = st.columns(2)

with col5:
    st.subheader("🌐 Top Risky Sender Domains")
    st.dataframe(top_risky_domains)

with col6:
    st.subheader("📊 Priority vs Detection Rule Matrix")
    st.dataframe(priority_rule_matrix)

st.divider()

st.caption("SOC Dashboard Suite — Detection Engineering & Alert Intelligence Pipeline")
