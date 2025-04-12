# app.py

import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# Set up prompt and model
template = """Question: {question}

Answer: Let's think step by step."""
prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.2", base_url="http://localhost:11434")

chain = prompt | model

# Streamlit UI
st.title("💬 Ask Llama3 via LangChain")

user_question = st.text_input("Enter your question:")

if user_question:
    with st.spinner("Thinking..."):
        response = chain.invoke({"question": user_question})
        st.markdown("### 🧠 Answer:")
        st.write(response)
