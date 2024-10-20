import streamlit as st
from transformers import pipeline
import os

st.title("IS883_Homework6")

prompt = st.text_input("Enter a prompt", "Today")


### Create a GPT2 generator pipeline
generator = pipeline('text-generation', model='gpt2')

### Generate the answer to the question "Enter your prompt"
response = generator(prompt, max_length=20, num_return_sequences=10, truncation=True)


### Display
st.write(
    response[0]['generated_text']
)
