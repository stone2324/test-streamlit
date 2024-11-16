import streamlit as st
from common.state.session_state import initialize_session_state
from common.layout.auth_layout import render_auth_page
from common.layout.main_layout import render_main_layout

def main():
    # Initialize session state
    initialize_session_state()
    
    # Render main content based on auth state
    if not st.session_state.logged_in:

        render_auth_page()
    else:
        render_main_layout()

if __name__ == "__main__":

    st.set_page_config(
        page_title="Lumos App",
        page_icon="🔒",
        layout="centered"
    )

    main()