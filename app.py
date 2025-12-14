import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

from models.cyber_incident import CyberIncident
from services.cyber_services import CyberIncidentService
from services.cyber_analytics import CyberAnalyticsService
from services.ai_insights_services import AIInsightsService

from models.it_ticket import ITTicket
from services.it_services import ITTicketService
from services.it_analytics_service import ITOperationsAnalyticsService
from services.it_ai_insights import ITAIInsights

from services.ai_openai_service import OpenAIAssistant


# -------------------------------
# CONFIG
# -------------------------------
st.set_page_config(
    page_title="Multi-Domain Intelligence Platform",
    layout="wide"
)

DATA_PATH = Path("data/cyber_incidents.csv")
USERS_PATH = Path("data/users.csv")

DOMAINS = [
    "Cybersecurity Intelligence",
    "IT Operations",
    "Data Science"
]

# -------------------------------
# SESSION STATE
# -------------------------------
for key in ["logged_in", "page"]:
    if key not in st.session_state:
        st.session_state[key] = None


# -------------------------------
# USER STORAGE
# -------------------------------
def load_users():
    if not USERS_PATH.exists():
        return pd.DataFrame(columns=["username", "password"])
    return pd.read_csv(USERS_PATH)


def save_users(df):
    df.to_csv(USERS_PATH, index=False)


# -------------------------------
# AUTH
# -------------------------------
def login_ui():
    st.markdown("## 🔐 Welcome")
    st.caption("Secure access to the Multi-Domain Intelligence Platform")

    choice = st.radio("Select an option:", ["New User", "Existing User"])
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    users_df = load_users()

    if choice == "New User":
        if st.button("Register"):
            if not username or not password:
                st.error("Username and password are required.")
                return

            if username in users_df["username"].values:
                st.error("User already exists.")
            else:
                users_df = pd.concat(
                    [users_df, pd.DataFrame([{"username": username, "password": password}])],
                    ignore_index=True
                )
                save_users(users_df)
                st.success("Registration successful. Please log in.")

    else:
        if st.button("Login"):
            user = users_df[users_df["username"] == username]
            if user.empty or user.iloc[0]["password"] != password:
                st.error("Invalid credentials.")
            else:
                st.session_state.logged_in = True
                st.session_state.page = "dashboard"


# -------------------------------
# DASHBOARD HOME
# -------------------------------
def dashboard():
    st.markdown("# 📊 Main Dashboard")
    st.caption("Select an intelligence domain to explore insights")

    cols = st.columns(3)
    for i, domain in enumerate(DOMAINS):
        with cols[i]:
            st.subheader(domain)
            if domain == "Cybersecurity Intelligence":
                if st.button("Explore", key=f"cyber_{i}"):
                    st.session_state.page = "cyber"
            elif domain == "IT Operations":
                if st.button("Explore", key=f"it_{i}"):
                    st.session_state.page = "it"
            else:
                st.button("Coming Soon", disabled=True)


# -------------------------------
# CYBERSECURITY DASHBOARD
# -------------------------------
def cybersecurity_dashboard():
    st.markdown("## 🛡️ Cybersecurity Intelligence")
    st.caption("Operational visibility into organisational cyber incidents")

    if st.button("⬅ Back"):
        st.session_state.page = "dashboard"
        return

    df = pd.read_csv(DATA_PATH)

    # -------------------------------
    # BAR CHART ANALYTICS
    # -------------------------------
    st.markdown("### 📊 Incident Overview")
    st.caption("High-level distribution of incidents by severity and status")

    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(5, 5))
        df["severity"].value_counts().plot(kind="bar", ax=ax)
        ax.set_title("Incidents by Severity", fontsize=11)
        ax.tick_params(labelsize=9)
        plt.tight_layout()
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots(figsize=(5, 5))
        df["status"].value_counts().plot(kind="bar", ax=ax)
        ax.set_title("Incidents by Status", fontsize=11)
        ax.tick_params(labelsize=9)
        plt.tight_layout()
        st.pyplot(fig)

    # -------------------------------
    # KPIs
    # -------------------------------
    st.markdown("### 📌 Key Risk Indicators")
    st.caption("Automated metrics supporting situational awareness")

    kpis = CyberAnalyticsService.compute_kpis(df)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Incidents", kpis["total"])
    c2.metric("Open", kpis["open"])
    c3.metric("Critical", kpis["critical"])
    c4.metric("Resolution %", kpis["resolution_rate"])

    st.info(CyberAnalyticsService.risk_score(df))

    # -------------------------------
    # 🤖 AI-ASSISTED INSIGHTS (CYBERSECURITY)
    # -------------------------------
    st.markdown("### 🤖 AI-Assisted Insights")
    st.caption("Automated and AI-supported interpretation of cybersecurity data")

    # Rule-based AI insights
    ai_insights = CyberAnalyticsService.ai_insights(df)
    for insight in ai_insights:
        st.info(insight)

    # Optional OpenAI-powered summary
    if st.button("Generate AI Summary"):
        summary = OpenAIAssistant.generate(
            "Provide a concise cybersecurity risk summary based on incident trends."
        )
        st.success(summary)


    # -------------------------------
    # TREND ANALYSIS 
    # -------------------------------
    st.markdown("### 📈 Incident Trends")
    st.caption("Temporal analysis highlighting changes in incident frequency")

    trend_df = CyberAnalyticsService.incidents_over_time(df)
    if not trend_df.empty:
        fig, ax = plt.subplots(figsize=(4.5, 2.8))
        ax.plot(trend_df["date"], trend_df["count"], marker="o")
        ax.set_title("Incidents Over Time", fontsize=11)
        ax.tick_params(axis="x", rotation=45, labelsize=8)
        ax.tick_params(axis="y", labelsize=8)
        plt.tight_layout()
        st.pyplot(fig, use_container_width=False)
        st.info(CyberAnalyticsService.interpret_trends(trend_df))
    else:
        st.warning("Not enough data for trend analysis.")

    # -------------------------------
    # CRUD (NOW WORKS)
    # -------------------------------
    st.markdown("### 🛠️ Incident Management (CRUD)")
    st.caption("Create, update and manage cybersecurity incidents")

    action = st.selectbox(
        "Choose Action",
        ["View All Incidents", "Create Incident", "Update Incident Status", "Delete Incident"]
    )

    if action == "View All Incidents":
        incidents = CyberIncidentService.load_all()
        st.dataframe(pd.DataFrame([i.to_dict() for i in incidents]), use_container_width=True)

    elif action == "Create Incident":
        with st.form("create_incident"):
            incident_id = st.number_input("Incident ID", min_value=1)
            severity = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
            category = st.text_input("Category")
            status = st.selectbox("Status", ["Open", "In Progress", "Resolved", "Closed"])
            description = st.text_area("Description")

            if st.form_submit_button("Create"):
                CyberIncidentService.add_incident(
                    CyberIncident(
                        incident_id,
                        datetime.now(),
                        severity,
                        category,
                        status,
                        description
                    )
                )
                st.success("Incident created successfully.")

    elif action == "Update Incident Status":
        incident_id = st.number_input("Incident ID", min_value=1)
        new_status = st.selectbox("New Status", ["Open", "In Progress", "Resolved", "Closed"])
        if st.button("Update"):
            CyberIncidentService.update_incident_status(incident_id, new_status)
            st.success("Status updated.")

    elif action == "Delete Incident":
        incident_id = st.number_input("Incident ID", min_value=1)
        if st.button("Delete"):
            CyberIncidentService.delete_incident(incident_id)
            st.success("Incident deleted.")

# -------------------------------
# IT OPERATIONS DASHBOARD
# -------------------------------
def it_dashboard():
    st.markdown("## 🖥️ IT Operations")
    st.caption("Monitoring operational workload and service efficiency")

    if st.button("⬅ Back"):
        st.session_state.page = "dashboard"
        return

    # -------------------------------
    # LOAD DATA
    # -------------------------------
    tickets = ITTicketService.load_all()

    if not tickets:
        st.info("No IT tickets available.")
        return

    df = pd.DataFrame([t.to_dict() for t in tickets])

    # -------------------------------
    # KPIs
    # -------------------------------
    st.markdown("### 📊 Operational KPIs")
    st.caption("Snapshot of service health")

    kpis = ITOperationsAnalyticsService.ticket_kpis(df)
    cols = st.columns(len(kpis))
    for col, (key, value) in zip(cols, kpis.items()):
        col.metric(key, value)

    # -------------------------------
    # TRENDS (FORCED RENDER – FINAL)
    # -------------------------------
    st.markdown("### 📈 Ticket Trends")
    st.caption("Monthly ticket volume trends based on creation date")

    trend_df = ITOperationsAnalyticsService.ticket_trends(df)

    # Always show underlying data (prevents Streamlit silent failure)
    st.write("Trend data preview:")
    st.dataframe(trend_df)

    if trend_df.empty:
        st.warning("Trend data unavailable.")
    else:
        fig, ax = plt.subplots(figsize=(4.5, 3.0))

        ax.bar(
            trend_df["date"].astype(str),
            trend_df["count"].astype(int),
            color="#4F81BD"
        )

        ax.set_title("Ticket Volume Over Time", fontsize=11)
        ax.set_xlabel("Month", fontsize=9)
        ax.set_ylabel("Number of Tickets", fontsize=9)

        ax.tick_params(axis="x", rotation=45, labelsize=8)
        ax.tick_params(axis="y", labelsize=8)

        plt.tight_layout()
        st.pyplot(fig, use_container_width=False)

    # -------------------------------
    # AI INSIGHTS
    # -------------------------------
    st.markdown("### 🤖 AI-Assisted Insights")
    st.caption("Automated analysis of operational workload and risks")

    insights = ITAIInsights.generate(df)
    st.info(insights["load"])
    st.info(insights["risk"])
    st.success(insights["recommendation"])

    # -------------------------------
    # CRUD
    # -------------------------------
    st.divider()
    st.markdown("### 🛠️ IT Ticket Management (CRUD)")
    st.caption("Create, update, and manage IT service tickets")

    action = st.selectbox(
        "Choose Action",
        ["View All Tickets", "Create Ticket", "Update Ticket Status", "Delete Ticket"]
    )

    if action == "View All Tickets":
        st.dataframe(df, use_container_width=True)

    elif action == "Create Ticket":
        with st.form("create_ticket"):
            ticket_id = st.number_input("Ticket ID", min_value=1)
            priority = st.selectbox("Priority", ["Low", "Medium", "High"])
            description = st.text_area("Description")
            status = st.selectbox("Status", ["Open", "In Progress", "Resolved", "Closed"])
            assigned_to = st.text_input("Assigned To")
            created_at = st.date_input("Created At")
            resolution_time = st.number_input("Resolution Time (hours)", min_value=0.0)

            if st.form_submit_button("Create Ticket"):
                ITTicketService.add_ticket(
                    ITTicket(
                        ticket_id,
                        priority,
                        description,
                        status,
                        assigned_to,
                        created_at,
                        resolution_time
                    )
                )
                st.success("Ticket created successfully.")

    elif action == "Update Ticket Status":
        ticket_id = st.number_input("Ticket ID", min_value=1)
        new_status = st.selectbox(
            "New Status",
            ["Open", "In Progress", "Resolved", "Closed"]
        )

        if st.button("Update Status"):
            ITTicketService.update_ticket_status(ticket_id, new_status)
            st.success("Ticket status updated.")

    elif action == "Delete Ticket":
        ticket_id = st.number_input("Ticket ID", min_value=1)

        if st.button("Delete Ticket"):
            ITTicketService.delete_ticket(ticket_id)
            st.success("Ticket deleted.")

# -------------------------------
# ROUTER
# -------------------------------
if not st.session_state.logged_in:
    login_ui()
else:
    if st.session_state.page is None:
        st.session_state.page = "dashboard"

    if st.session_state.page == "dashboard":
        dashboard()
    elif st.session_state.page == "cyber":
        cybersecurity_dashboard()
    elif st.session_state.page == "it":
        it_dashboard()
