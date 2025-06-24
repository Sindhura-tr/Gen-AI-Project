# Load the packages
import streamlit as st
from groq import Groq

# Provide a title for streamlit website
st.set_page_config(page_title="GEN AI PROJECT")

# Load the API key
api_key = st.secrets["API_KEY"]

# Intialize the Groq client
client = Groq(api_key=api_key)

# Function to generate the model responses based on user inputs
def get_response(text,model_name="llama-3.3-70b-versatile"):
    stream = client.chat.completions.create(
        messages =[
            {
                "role":"system",
                "content":"You are a helpful assistant"
            },
            {
                "role":"user",
                "content":text
            }
        ],
        model=model_name,
        stream=True
    )

    for chunk in stream:
        response = chunk.choices[0].delta.content
        if response is not None:
            yield response
# Add the title to streamlit website
st.title("Gen AI Project using llama-3.3-70b-versatile")
st.subheader("By Sindhura Nadendla")

# Provide a text box area for users to provide their inputs
user_ip = st.text_area("Ask your question here ")

# Create the button (submit)
submit = st.button("Generate Response",type="primary")

# Write the code that passes the user input to get_response function and receives the response. Write the response on website
if submit:
    st.subheader("Model Reponse: ")
    st.write_stream(get_response(user_ip))