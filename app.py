## Streamlit code gos here....(website)

import streamlit as st
from models import gemini

st.header('Gemini LLM Application')

prompt = st.text_area(
    'Enter Prompt',
    placeholder='ask question?'
)

# success -> green, warning -> yellow, error -> red
if st.button('Send Prompt🛩️'):
    if prompt.strip() == "":
        st.warning('Enter Valid Prompt.')
    else:
        with st.spinner('Thinking...🤔'):
            answer = gemini(prompt)
            st.write(answer)
        