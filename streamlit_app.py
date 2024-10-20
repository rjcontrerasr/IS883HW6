import streamlit as st
from transformers import pipeline
import os

st.title("IS883_Homework6")

prompt = st.text_input("Enter a prompt", "Boston is a")
tokens = st.number_input("Enter number of output tokens, max 1000", min_value=1, max_value=1000, value=80)


### Create a GPT2 generator pipeline
generator = pipeline('text-generation', model='gpt2')

### Generate the answer to the question "Enter your prompt"
response1 = generator(prompt, max_length=tokens, temperature = 0.85, num_return_sequences=1, truncation=True)
response2 = generator(prompt, max_length=tokens, temperature = 0.25, num_return_sequences=1, truncation=True)


### Display
st.write("Response 1 *Creative* :sunglasses:")
st.write(
    response1[0]['generated_text']
)

st.write("Response 2 *Predictable* :disappointed:")
st.write(
    response2[0]['generated_text']
)

##References
##https://docs.streamlit.io/develop/api-reference/widgets/st.number_input
##https://medium.com/@imisri1/how-to-set-sampling-temperature-for-gpt-models-762887df1fac
##https://discuss.huggingface.co/t/why-cant-temperature-be-0-for-gpt2-and-gpt-neo/35583
##https://github.com/huggingface/transformers/issues/2029
