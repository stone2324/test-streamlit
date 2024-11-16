import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔐")

def render_login():
    st.title("Login 🔐")
    
    if st.session_state.get('logged_in'):
        st.success(f"You are already logged in as {st.session_state.get('username')}")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = None
            st.rerun()
        return

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        submitted = st.form_submit_button("Login", type="primary")
        
        if submitted:
            if st.session_state.user_manager.verify_user(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid username or password")