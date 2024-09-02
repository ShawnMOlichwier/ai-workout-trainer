"""
Initial script for display to the user

Will eventually be depricated for a better, TBD, frontend.

"""


# import sys
import streamlit as st
st.set_page_config(layout="wide")
# sys.path.append("../..")

from src.llm import LLMClient

client = LLMClient()



st.title("Welcome to your AI Personal Trainer!")


prompt = st.chat_input("What type of workout are you looking for today?")
st.markdown("---")

if prompt:
    llm_response = client.generate(prompt)
    st.write(llm_response.choices[0].message.content)

    prompt = False