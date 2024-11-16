import streamlit as st
from common.models.user_manager import UserManager
from common.components.login import render_login
from common.components.register import render_register
from common.components.profile import render_profile

def main():
    st.title("Welcome to the App 👋")
    
    # Initialize session state
    if 'user_manager' not in st.session_state:
        st.session_state.user_manager = UserManager()
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    if not st.session_state.logged_in:
        tab1, tab2 = st.tabs(["Login", "Register"])
        
        with tab1:
            render_login()
        
        with tab2:
            render_register()
    
    else:
        # Show profile when logged in
        render_profile()
        
        # Add logout button at the bottom
        st.divider()
        if st.button("Logout", type="secondary"):
            st.session_state.logged_in = False
            st.session_state.username = None
            st.rerun()

if __name__ == "__main__":
    st.set_page_config(
        page_title="Login App",
        page_icon="🔒",
        layout="centered"
    )
    main()