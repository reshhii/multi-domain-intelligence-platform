import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from models.cyber_incident import CyberIncident
from services.cyber_services import CyberIncidentService
from services.cyber_analytics import CyberAnalyticsService
from datetime import datetime
from services.ai_insights_services import AIInsightsService


# -------------------------------
# CONFIG
# -------------------------------
st.set_page_config(page_title="Multi-Domain Intelligence Platform", layout="wide")

DATA_PATH = Path("data/cyber_incidents.csv")
USERS_PATH = Path("data/users.csv")

DOMAINS = [
    "Cybersecurity Intelligence",
    "IT Operations",
    "Data Science"
]

# -------------------------------
# SESSION STATE INIT
# -------------------------------
for key in ["logged_in", "page", "domain"]:
    if key not in st.session_state:
        st.session_state[key] = None

# -------------------------------
# USER STORAGE HELPERS
# -------------------------------
def load_users():
    if not USERS_PATH.exists():
        return pd.DataFrame(columns=["username", "password"])
    return pd.read_csv(USERS_PATH)

def save_users(df):
    df.to_csv(USERS_PATH, index=False)

# -------------------------------
# AUTH (FIXED – LOGIC ONLY)
# -------------------------------
def login_ui():
    st.markdown("## 🔐 Welcome")
    st.caption("Please register or sign in to continue")

    choice = st.radio("Select an option:", ["New User", "Existing User"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    users_df = load_users()

    if choice == "New User":
        if st.button("Register"):
            if not username or not password:
                st.error("Username and password are required")
                return

            if username in users_df["username"].values:
                st.error("Account already exists. Please login.")
            else:
                new_user = pd.DataFrame(
                    [{"username": username, "password": password}]
                )
                users_df = pd.concat([users_df, new_user], ignore_index=True)
                save_users(users_df)
                st.success("Registration successful. Please login.")

    else:
        if st.button("Login"):
            if not username or not password:
                st.error("Username and password are required")
                return

            user_row = users_df[users_df["username"] == username]

            if user_row.empty:
                st.error("Account not found. Please register first.")
            elif user_row.iloc[0]["password"] != password:
                st.error("Incorrect password. Please try again.")
            else:
                st.session_state.logged_in = True
                st.session_state.page = "login_success"

# -------------------------------
# LOGIN SUCCESS
# -------------------------------
def login_success():
    st.success("✅ Login successful")
    st.markdown(
        "This platform allows you to explore insights across multiple domains.\n\n"
        "**Select a domain to begin.**"
    )
    if st.button("Go to Dashboard"):
        st.session_state.page = "dashboard"

# -------------------------------
# MAIN DASHBOARD
# -------------------------------
def dashboard():
    st.markdown("# 📊 Main Dashboard")
    st.caption("Select a domain to explore")

    cols = st.columns(3)

    for i, domain in enumerate(DOMAINS):
        with cols[i]:
            st.subheader(domain)
            if "Cybersecurity" in domain:
                if st.button("Explore", key=f"domain_{i}"):
                    st.session_state.domain = domain
                    st.session_state.page = "cyber"
            else:
                st.button("Coming Soon", disabled=True, key=f"disabled_{i}")

# -------------------------------
# LOAD DATA
# -------------------------------
def load_data():
    if not DATA_PATH.exists():
        st.error("cyber_incidents.csv not found")
        return pd.DataFrame()
    return pd.read_csv(DATA_PATH)

def save_data(df):
    df.to_csv(DATA_PATH, index=False)

# -------------------------------
# CYBERSECURITY DOMAIN
# -------------------------------
def cybersecurity_dashboard():
    st.markdown("## 🛡️ Cybersecurity Intelligence")
    st.caption("Monitor, analyze and manage cyber incidents")

    if st.button("⬅ Back to Main Dashboard"):
        st.session_state.page = "dashboard"
        return

    df = load_data()

    # -------------------------------
    # ANALYTICS
    # -------------------------------
    st.markdown("### 📈 Incident Analytics")

    col1, col2 = st.columns(2)

    with col1:
        severity_counts = df["severity"].value_counts()
        fig, ax = plt.subplots(figsize=(5,3))
        ax.bar(severity_counts.index, severity_counts.values)
        ax.set_title("Incidents by Severity")
        ax.title.set_size(11)
        ax.tick_params(axis="both", labelsize=9)
        plt.tight_layout()
        st.pyplot(fig)

    with col2:
        status_counts = df["status"].value_counts()
        fig, ax = plt.subplots(figsize=(5,3))
        ax.bar(status_counts.index, status_counts.values)
        ax.set_title("Incidents by Status")
        ax.title.set_size(11)
        ax.tick_params(axis="both", labelsize=9)
        plt.tight_layout()
        st.pyplot(fig)

        # -------------------------------
    # INTELLIGENT DASHBOARD (WEEK 10)
    # -------------------------------
    st.markdown("### 🧠 Cybersecurity Intelligence Summary")
    st.caption("Automated analysis and AI-assisted decision support")

    kpis = CyberAnalyticsService.compute_kpis(df)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Incidents", kpis["total"])
    col2.metric("Open Incidents", kpis["open"])
    col3.metric("Critical Incidents", kpis["critical"])
    col4.metric("Resolution Rate (%)", kpis["resolution_rate"])

    risk = CyberAnalyticsService.risk_score(df)
    st.markdown(f"**Overall Cyber Risk Level:** `{risk}`")

    st.markdown("### 🤖 AI-Generated Insights")
    for insight in CyberAnalyticsService.ai_insights(df):
        st.info(insight)

    st.divider()

        # -------------------------------
    # ADVANCED ANALYTICS & TRENDS (WEEK 11)
    # -------------------------------
    st.markdown("### 📊 Incident Trends and Analysis")
    st.caption("Temporal and severity-based analysis of cybersecurity incidents")

    trend_df = CyberAnalyticsService.incidents_over_time(df)

    # ---------- INCIDENT TREND VISUALIZATION ----------
    if not trend_df.empty:

        col_trend, _ = st.columns([1, 1])

        with col_trend:
           fig, ax = plt.subplots(figsize=(4.5, 3.0))

           ax.plot(
               trend_df["date"],
               trend_df["count"],
               marker="o",
               linewidth=2
           )

           ax.set_title("Incidents Over Time", fontsize=11)
           ax.set_xlabel("Date", fontsize=9)
           ax.set_ylabel("Number of Incidents", fontsize=9)

           ax.tick_params(axis="x", labelsize=8, rotation=45)
           ax.tick_params(axis="y", labelsize=8)

           plt.tight_layout()
           st.pyplot(fig, use_container_width=False)

        interpretation = CyberAnalyticsService.interpret_trends(trend_df)
        st.info(interpretation)

    else:
        st.info("Not enough data available to display incident trends")


    severity_dist = CyberAnalyticsService.severity_distribution(df)
    if severity_dist:
        st.markdown("**Severity Distribution**")
        for sev, count in severity_dist.items():
            st.write(f"- {sev}: {count} incidents")

        # -------------------------------
    # AI-ASSISTED INSIGHTS (WEEK 12)
    # -------------------------------
    st.divider()
    st.markdown("### 🤖 AI-Assisted Security Insights")
    st.caption("Automated risk assessment and decision support")

    insights = AIInsightsService.generate_insights(df)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Risk Level", insights.get("risk_level", "N/A"))
        st.write(insights.get("risk_reason", ""))

    with col2:
        st.metric("Operational Health", insights.get("operational_health", "N/A"))
        st.write(insights.get("operations_reason", ""))

    st.info(f"📌 **AI Recommendation:** {insights.get('recommendation', '')}")


    # -------------------------------
    # CRUD
    # -------------------------------
    st.markdown("### 🛠️ Incident Management (CRUD)")

    action = st.selectbox(
        "Choose an action",
        ["View All Incidents", "Create Incident", "Update Incident Status", "Delete Incident"]
    )

    if action == "View All Incidents":
        incidents = CyberIncidentService.load_all()
        if incidents:
            df_view = pd.DataFrame([i.to_dict() for i in incidents])
            st.dataframe(df_view, use_container_width=True)
        else:
            st.info("No incidents found")


    elif action == "Create Incident":
        with st.form("create_incident"):
            incident_id = st.number_input("Incident ID", min_value=1, step=1)
            severity = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
            category = st.text_input("Category")
            status = st.selectbox("Status", ["Open", "In Progress", "Resolved", "Closed"])
            description = st.text_area("Description")

            if st.form_submit_button("Create") :
                incident = CyberIncident(
                    incident_id=incident_id,
                    timestamp=datetime.now(),
                    severity=severity,
                    category=category,
                    status=status,
                    description=description
                )
                CyberIncidentService.add_incident(incident)
                st.success("Incident created successfully")

    elif action == "Update Incident Status":
        incident_id = st.number_input("Incident ID", min_value=1, step=1)
        new_status = st.selectbox("New Status", ["Open", "In Progress", "Resolved", "Closed"])

        if st.button("Update Status"):
           CyberIncidentService.update_incident_status(incident_id, new_status)
           st.success("Incident status updated")


    elif action == "Delete Incident":
        incident_id = st.number_input("Incident ID", min_value=1, step=1)
        if st.button("Delete"):
            CyberIncidentService.delete_incident(incident_id)
            st.success("Incident deleted")


# -------------------------------
# ROUTER
# -------------------------------
if not st.session_state.logged_in:
    login_ui()
else:
    if st.session_state.page is None:
        st.session_state.page = "login_success"

    if st.session_state.page == "login_success":
        login_success()
    elif st.session_state.page == "dashboard":
        dashboard()
    elif st.session_state.page == "cyber":
        cybersecurity_dashboard()
