import streamlit as st
import pandas as pd

from auth.auth import register_user, login_user
from db.analytics import incidents_by_severity, incidents_by_status


# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Unified Intelligence Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# Session state initialization
# --------------------------------------------------
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if "username" not in st.session_state:
    st.session_state["username"] = ""


# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("Unified Intelligence Platform")
st.caption("Secure multi-domain analytics system")

st.write(
    """
    This platform provides analytical insights for multiple technical user groups.
    The current implementation focuses on **secure authentication**, **efficient CSV
    ingestion using pandas**, and **database-backed analytics using SQLite**.
    """
)

st.divider()


# --------------------------------------------------
# Authentication Section
# --------------------------------------------------
if not st.session_state["authenticated"]:

    st.subheader("Secure Login & Registration")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login", use_container_width=True):
            if login_user(username, password):
                st.success("Login successful")
                st.session_state["authenticated"] = True
                st.session_state["username"] = username
                st.rerun()
            else:
                st.error("Invalid username or password")

    with col2:
        if st.button("Register", use_container_width=True):
            if register_user(username, password):
                st.success("Registration successful. You may now log in.")
            else:
                st.warning("Username already exists")


# --------------------------------------------------
# Dashboard Section (Visible only after login)
# --------------------------------------------------
else:
    st.success(f"Logged in as **{st.session_state['username']}**")

    if st.button("Logout"):
        st.session_state["authenticated"] = False
        st.session_state["username"] = ""
        st.rerun()

    st.divider()

    # --------------------------------------------------
    # System Status
    # --------------------------------------------------
    st.subheader("System Status")
    st.success("Environment and dependencies loaded successfully.")

    st.divider()

    # --------------------------------------------------
    # Cybersecurity Incident Dataset (CSV → pandas)
    # --------------------------------------------------
    st.subheader("Cybersecurity Incident Dataset")

    @st.cache_data
    def load_cyber_data():
        return pd.read_csv("data/cyber_incidents.csv")

    df = load_cyber_data()

    st.markdown("### Dataset Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Records", df.shape[0])

    with col2:
        st.metric("Total Features", df.shape[1])

    with col3:
        st.metric("Unique Incident Categories", df["category"].nunique())

    st.divider()

    # --------------------------------------------------
    # Data Preview
    # --------------------------------------------------
    st.markdown("### Preview of Ingested Data")
    st.dataframe(df.head(10), use_container_width=True)

    st.divider()

    # --------------------------------------------------
    # Database Analytics (Week 8 – REQUIRED)
    # --------------------------------------------------
    st.subheader("Database Insights")

    severity_data = incidents_by_severity()
    status_data = incidents_by_status()

    severity_df = pd.DataFrame(
        severity_data,
        columns=["Severity", "Incident Count"]
    )

    status_df = pd.DataFrame(
        status_data,
        columns=["Status", "Incident Count"]
    )

    st.markdown("### Incident Severity Distribution")
    st.bar_chart(severity_df.set_index("Severity"))

    st.markdown("### Incident Status Distribution")
    st.bar_chart(status_df.set_index("Status"))
