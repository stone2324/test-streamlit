import streamlit as st

def render_login():
    """Render the login form"""
    st.subheader("Login")
    login_username = st.text_input("Username", key="login_username")
    login_password = st.text_input("Password", type="password", key="login_password")
    
    if st.button("Login", type="primary"):
        if st.session_state.user_manager.verify_user(login_username, login_password):
            st.session_state.logged_in = True
            st.session_state.username = login_username
            st.success("Logged in successfully!")
            st.rerun()
        else:
            st.error("Invalid username or password") 