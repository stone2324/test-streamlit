import streamlit as st
import re

def render_register():
    """Render the registration form"""
    if st.button("Create Account"):
        show_register_dialog()

@st.dialog("Register New Account")
def show_register_dialog():
    reg_username = st.text_input("Username", key="reg_username")
    reg_name = st.text_input("Full Name", key="reg_name")
    reg_email = st.text_input("Email", key="reg_email")
    reg_password = st.text_input("Password", type="password", key="reg_password")
    reg_password_confirm = st.text_input("Confirm Password", type="password", key="reg_password_confirm")
    
    # Show password strength feedback
    if reg_password:
        is_valid, message = st.session_state.user_manager.validate_password(reg_password)
        if is_valid:
            st.success(message)
        else:
            st.warning(message)
    
    if st.button("Register", type="primary"):
        if not reg_username or not reg_name or not reg_email or not reg_password:
            st.error("Please fill in all fields")
        elif reg_password != reg_password_confirm:
            st.error("Passwords do not match")
        else:
            is_valid, message = st.session_state.user_manager.validate_password(reg_password)
            if not is_valid:
                st.error(message)
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", reg_email):
                st.error("Please enter a valid email address")
            else:
                if st.session_state.user_manager.register_user(reg_username, reg_password, reg_email, reg_name):
                    st.success("Registration successful! Please login.")
                    st.balloons()
                else:
                    st.error("Username already exists") 