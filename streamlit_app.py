import streamlit as st
from transformers import pipeline
import os

st.title("IS883_Homework6")

prompt = st.text_input("Enter a prompt", "Today")
tokens = st.number_input("Enter number of output tokens, max 1000", min_value=1, max_value=1000, value=80)


### Create a GPT2 generator pipeline
generator = pipeline('text-generation', model='gpt2')

### Generate the answer to the question "Enter your prompt"
response = generator(prompt, max_length=tokens, num_return_sequences=1, truncation=True)


### Display
st.write(
    response[0]['generated_text']
)


##References
##https://docs.streamlit.io/develop/api-reference/widgets/st.number_input
