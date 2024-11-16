import streamlit as st

from common.components.profile import render_profile
from quote_tool.quote_tool import render_quote_tool
from tests_generator.tests_generator import render_tests_generator

def render_navigation():
    """Render the navigation menu using st.navigation"""
    pages = {
        "User": [
            st.Page(render_profile, title="Profile"),
        ],
        "Tools": [
            st.Page(render_quote_tool, title="Quote Tool"),
            st.Page(render_tests_generator, title="Test Generator"),
        ],
    }
    
    return st.navigation(pages) 