import streamlit as st


st.set_page_config(page_title="World Cities", page_icon="🌍")

st.title("🌍 World Cities")
st.write("Welcome to the World Cities Streamlit app!")
st.write("Explore cities from around the world using the app.")

if st.button("Go to the app"):
    st.switch_page("app.py")
