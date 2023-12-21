import streamlit as st
from send_email import send_email

st.header("Contact me")

with st.form(key="contact_form"):
    user_email = st.text_input("Enter your email address")
    raw_message = st.text_area("your message")
    message = f"""\
    Subject: New email from: {user_email}

    From: {user_email}
    {raw_message}
    """
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email has been sent successfully")
