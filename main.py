from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import streamlit as st
import os

api_key = os.getenv("GOOGLE_API_KEY", st.secrets.get("GOOGLE_API_KEY", None))

# Create prompt template for generating tweets

tweet_template = "Give me {number} distinct characteristics of {raga} raga"

tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ['number', 'raga'])

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")


# Create LLM chain using the prompt template and model
tweet_chain = tweet_prompt | gemini_model


import streamlit as st

st.header("Raga Info Generator - Sinnakkrishnan")

st.subheader("Generate Info Bytes using Generative AI")

Raga = st.text_input("Raga")

number = st.number_input("Number of Info Bytes", min_value = 1, max_value = 10, value = 1, step = 1)

if st.button("Generate"):
    tweets = tweet_chain.invoke({"number" : number, "raga" : Raga})
    st.write(tweets.content)
    
