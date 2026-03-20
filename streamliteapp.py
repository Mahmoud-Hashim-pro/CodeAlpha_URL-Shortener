import streamlit as st ##good for UI
import requests

st.title("🔗 URL Shortener")


url = st.text_input("Enter your URL")

expires_at = st.text_input("Expiration (optional) e.g. 2026-04-01 12:00:00")

if st.button("Shorten"):
    if url:
        data = {
            "url": url
        }

        if expires_at:
            data["expires_at"] = expires_at

        response = requests.post(
            "http://127.0.0.1:5000/shorten",
            json=data
        )

        if response.status_code == 200:
            short_url = response.json()['short_url']
            st.success(f"Short URL: {short_url}")
        else:
            st.error("Something went wrong")
    else:
        st.warning("Please enter a URL")
