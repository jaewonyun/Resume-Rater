import streamlit as st
from app_functions import get_matches_resume

# openApiKey = st.secrets["OPENAI_API_KEY"]
# openai.api_key = openApiKey

st.title("Resume Rater")

with st.sidebar:
    # st.image(image, width=100)
    st.title('Toggle options')
    # st.write('Select the options to get the best match for your job description')
    matchtype = st.radio('Select match type', ['resume', 'skills', 'work experience'])
    top_k = st.slider('Select the number of candidates to return', 1, 20, 10)

user_input = st.text_input('Enter the description of perfect candidate for hire')
st.write('You entered: ', user_input)
matches = get_matches_resume(user_input, k=top_k, match_type=matchtype)

st.dataframe(matches[['full_name', 'distance']])


