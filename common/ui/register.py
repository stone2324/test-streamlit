import streamlit as st
import re

st.set_page_config(page_title="Register", page_icon="📝")

def render_register():
    st.title("Register 📝")
    
    if st.session_state.get('logged_in'):
        st.warning("You are already logged in. Please logout first to register a new account.")
        return

    with st.form("registration_form"):
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        password_confirm = st.text_input("Confirm Password", type="password")
        
        # Show password strength feedback
        if password:
            is_valid, message = st.session_state.user_manager.validate_password(password)
            if is_valid:
                st.success(message)
            else:
                st.warning(message)
        
        submitted = st.form_submit_button("Register")
        
        if submitted:
            if not username or not email or not password:
                st.error("Please fill in all fields")
            elif password != password_confirm:
                st.error("Passwords do not match")
            else:
                is_valid, message = st.session_state.user_manager.validate_password(password)
                if not is_valid:
                    st.error(message)
                elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    st.error("Please enter a valid email address")
                else:
                    if st.session_state.user_manager.register_user(username, password, email):
                        st.success("Registration successful! Please login.")
                        st.balloons()
                    else:
                        st.error("Username already exists")