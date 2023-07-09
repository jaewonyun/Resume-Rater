import streamlit as st

st.title("Resume Rater")

st.sidebar.title("sidebar")

user_input = st.text_input('Enter the description of perfect candidate for hire')
st.write(user_input)
