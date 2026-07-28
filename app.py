import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


st.set_page_config(
    page_title = "Agriculture ChatBot",
    page_icon = "😎"
)
st.title("🌽Agriculture AI Chatbot")
st.write("This is an AI Agriculture Chatbot, It is useful for acquiring knowledge about agriculture")

st.write("Ask anything related to Agriculture")

question = st.text_area(
    "Enter Your Agri Question"
)
if st.button("ASK AI"):
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.3
    )

    prompt = ChatPromptTemplate.from_template(
        """
You are an Agriculture Expert

Your job is to answer ONLY agriculture related questions.

Topics include:
-Crops
-Soil
-Fertilizers
-Irrigation
-Seeds
-Farming
-Pest Control
-Organic Farming
-Plant Diseases
-Harvesting

if the user asks anything outside agriculture, 
reply:
"Sorry, I only answer agriculture related questions"
Question
{question}

Provide:
1.Simple Explaination
2.Step-by-Step guidance
3.Best Practices
4.Precautions if needed
"""
    )
    chain = prompt | llm
    response = chain.invoke(
        {
            "question":question
        }
    )
    st.success(response.content)