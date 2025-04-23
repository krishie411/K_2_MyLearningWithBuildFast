import streamlit as st
import openai
import os

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY", st.secrets.get("OPENAI_API_KEY", None))

# Streamlit UI
st.header("Raga Info Generator - Sinnakkrishnan")
st.subheader("Generate Info Bytes using Generative AI")

Raga = st.text_input("Raga")
number = st.number_input("Number of Info Bytes", min_value=1, max_value=10, value=1, step=1)

# Prompt template
prompt_template = "Give me {number} distinct characteristics of {raga} raga."

# Generate on button click
if st.button("Generate"):
    prompt = prompt_template.format(number=number, raga=Raga)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant knowledgeable in Indian classical music."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        st.write(response.choices[0].message.content)
    except Exception as e:
        st.error(f"Error: {e}")
