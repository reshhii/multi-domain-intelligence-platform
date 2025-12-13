import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Unified Intelligence Platform",
    layout="wide"
)

st.title("Unified Intelligence Platform")
st.write(
    """
    This platform provides analytical insights for multiple technical user groups.
    The initial implementation focuses on structured data ingestion and exploration.
    """
)

st.subheader("System Status")
st.success("Environment and dependencies loaded successfully.")
st.divider()

st.subheader("Cybersecurity Incident Dataset")

@st.cache_data
def load_cyber_data():
    return pd.read_csv("data/cyber_incidents.csv")

df = load_cyber_data()

st.write("Preview of ingested data:")
st.dataframe(df.head())

st.markdown("**Dataset Overview**")
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Records", df.shape[0])

with col2:
    st.metric("Total Features", df.shape[1])
