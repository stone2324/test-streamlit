import streamlit as st
from utils.auth import require_auth
from datetime import datetime

st.set_page_config(page_title="Profile", page_icon="👤")

def render_profile():
    st.title("Profile 👤")
    
    # Require authentication
    username = require_auth()
    if not username:
        return
    
    # Get user info
    user_info = st.session_state.user_manager.get_user_info(username)
    
    # Display user information
    st.subheader("User Information")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("Username:", username)
        st.write("Email:", user_info.get('email'))
    
    with col2:
        created_at = datetime.fromisoformat(user_info.get('created_at', ''))
        st.write("Account Created:", created_at.strftime("%Y-%m-%d %H:%M"))
        
        last_login = user_info.get('last_login')
        if last_login:
            last_login = datetime.fromisoformat(last_login)
            st.write("Last Login:", last_login.strftime("%Y-%m-%d %H:%M"))
