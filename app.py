import streamlit as st
import pandas as pd
from fuzzywuzzy import process

# Load FAQ data
faq = pd.read_csv("faq.csv")

st.title("FAQ Chatbot")
st.write("Ask me anything from the FAQ 👇")

# Function to get best answer
def get_answer(user_input, faq_df):
    questions = faq_df['question'].tolist()
    best_match, score = process.extractOne(user_input, questions)
    if score > 70:  # 70% similarity threshold
        return faq_df[faq_df['question'] == best_match]['answer'].values[0]
    else:
        return "Sorry, I don’t know the answer to that yet."

# Input box
user_input = st.text_input("You:")

if user_input:
    answer = get_answer(user_input, faq)
    st.write("🤖 Bot:", answer)