import streamlit as st
from common.models.user_manager import UserManager

def initialize_session_state():
    """Initialize all session state variables"""
    if 'user_manager' not in st.session_state:
        st.session_state.user_manager = UserManager()
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "Profile" 