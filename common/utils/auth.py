import streamlit as st
from typing import Optional

def require_auth() -> Optional[str]:
    """
    Require authentication to access a page
    Returns username if authenticated, None if not
    """
    if not st.session_state.get('logged_in'):
        st.error("Please login to access this page")
        st.stop()
    return st.session_state.get('username')