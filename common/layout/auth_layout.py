import streamlit as st
from common.components.login import render_login
from common.components.register import render_register

def render_auth_page():
    """Render the authentication page with login/register tabs"""
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        render_login()
    
    with tab2:
        render_register() 