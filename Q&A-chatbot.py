import streamlit as st
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.document_loaders.csv_loader import CSVLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set the title of the app
st.title("Google Gemini Q&A Streamlit App")

# Configuration for Google Generative AI
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY not found. Please set it in your .env file.")
    st.stop()

# Initialize Google Generative AI
genai.configure(api_key=GOOGLE_API_KEY)
llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash', google_api_key=GOOGLE_API_KEY)

# Load the CSV file
loader = CSVLoader(file_path='questions.csv', source_column='prompt')
dataset = loader.load()

# Initialize embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Create the vector store (FAISS)
vectordb = FAISS.from_documents(documents=dataset, embedding=embeddings)
retriever = vectordb.as_retriever(score_threshold=0.3)

# Create the Retrieval QA chain
qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retriever=retriever, input_key='query', return_source_documents=True)

# App layout
st.header("Ask Your Questions")

# User input: Question
user_query = st.text_input("Ask a question:", "")

if user_query:
    with st.spinner("Searching for an answer..."):
        # Get the answer from the Q&A chain
        response = qa_chain(user_query)
        
        # Display the answer
        st.subheader("Answer:")
        st.write(response["result"])

