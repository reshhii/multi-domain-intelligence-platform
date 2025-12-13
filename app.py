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
