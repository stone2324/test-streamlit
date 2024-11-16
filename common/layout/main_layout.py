import streamlit as st
from common.layout.auth_layout import render_auth_page
from common.layout.navigation import render_navigation
from common.components.profile import render_profile
from quote_tool.quote_tool import render_quote_tool
from tests_generator.tests_generator import render_tests_generator

def render_main_layout():
    """Render the main application layout when user is logged in"""
    # Navigation
    nav = render_navigation()
    nav.run()
    
    # Render logout button at the bottom
    with st.sidebar:
        render_logout_button()

def render_logout_button():
    if st.button("Logout", type="secondary"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.navigation([st.Page(render_auth_page, title="Login")])
        # pg.run()
        st.rerun() 