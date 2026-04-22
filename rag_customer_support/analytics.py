import streamlit as st

def init_metrics():
    if "queries" not in st.session_state:
        st.session_state.queries = 0
    if "escalations" not in st.session_state:
        st.session_state.escalations = 0

def add_query():
    st.session_state.queries += 1

def add_escalation():
    st.session_state.escalations += 1