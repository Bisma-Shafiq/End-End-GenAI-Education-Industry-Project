# Q&A GenAI ChatBot


This app leverages **Google Generative AI (Gemini-1.5)** and **LangChain** to provide intelligent, real-time answers to user questions. It retrieves answers based on a custom CSV dataset, making it easy to integrate into any knowledge base.

## Features

- **Real-Time Q&A**: Ask any question and receive a smart, context-aware response.
- **Document-Based**: Retrieve answers from your own dataset loaded from a CSV.
- **Customizable Workflow**: Modify the dataset or AI model as needed.
- **AI-Powered**: Uses **Google Gemini** and **LangChain** for robust AI workflows.

## Technologies

- **Google Generative AI (Gemini-1.5)**: For text generation and understanding.
- **LangChain**: A framework to streamline AI workflows.
- **GoogleGenerativeEmbeddingAI**: A word Embedding open-source
- **FAISS**: For efficient document retrieval.
- **dotenv**: To securely manage environment variables.

### Core Tools:
- **[Google Generative AI (Gemini-1.5)](https://developers.generativeai.google/)**: Generates high-quality text outputs with contextual understanding.
- **LangChain**: A framework for building applications powered by language models.

### Python Libraries:
- `google.generativeai`: Python SDK for interacting with Google Generative AI.
- `langchain_google_genai`: LangChain integration with Google Generative AI.
- `langchain`: Orchestrates prompts and chains for AI workflows.
- `dotenv`: Loads environment variables securely from a `.env` file.

---

## Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Set Up Virtual Environment (Optional)**:
   ```bash
   python -m venv env
   source env/bin/activate   # For Linux/Mac
   env\Scripts\activate     # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Add Your Google API Key**:
   - Create a `.env` file in the project root directory.
   - Add your Google Generative AI API key to the file:
     ```env
     GOOGLE_API_KEY=your_google_api_key_here
     ```

---

## Usage

### Run the Application

streamlit run app.py


3. Example Output:
   ```
   Ask a question:
    Why I trust ABC?
    Answer:
        Over 9000 learners have benefited from the quality of ABC's courses. You can check the review section and connect with learners via their provided LinkedIn profiles to ask about their experiences directly.
   ```

---

## Project Structure
```
.

├── app.py                # Main app script
├── .env                  # API key file
├── requirements.txt      # Dependencies
├── questions.csv         # Dataset with questions
├── README.md             # This file

```

---

## How It Works


The app is powered by **Google Generative AI (Gemini-1.5)** and **LangChain**, using the following steps to deliver intelligent answers:

1. **Environment Setup**: The app uses an API key from Google Generative AI, which is loaded from a `.env` file. The API key allows access to the AI model for generating text-based responses.

2. **CSV Dataset**: The app loads a custom CSV dataset containing prompts (questions) using **LangChain's CSVLoader**. The dataset is pre-structured with questions that are later used for the AI to retrieve answers.

3. **Embedding Generation**: The text data from the CSV is embedded into a vector format using **GoogleGenerativeAIEmbeddings**. These embeddings are used to search for the most relevant documents based on the user's query.

4. **Document Retrieval with FAISS**: Using **FAISS (Facebook AI Similarity Search)**, the app creates a vector store and retrieves relevant documents from the dataset. FAISS is designed for high-performance, similarity-based document retrieval.

5. **Question Answering (QA)**: The app uses **RetrievalQA** from LangChain to orchestrate the process. When the user asks a question, the QA chain first retrieves relevant documents from the dataset and then passes those documents to the **Google Gemini** model, which generates a context-aware answer.

6. **Display Results**: The response from **Google Gemini** is displayed in the app interface, along with the retrieved documents, providing a clear and informative answer to the user.

This workflow ensures that the app delivers intelligent, accurate, and contextually relevant answers based on the data it’s provided.

---

## Requirements
- Python 3.9+
- A valid Google Generative AI API key

---

## Contributing
Feel free to contribute to this project by submitting issues or pull requests. Please follow the [contribution guidelines](CONTRIBUTING.md) if you want to get involved.


---

## Acknowledgments
Special thanks to:
- **Google Generative AI Team** for providing such powerful AI tools.
- The creators of **LangChain** for simplifying AI workflows.

---

## Author
**Bisma Shafiq**

Connect with me on [LinkedIn](https://www.linkedin.com/in/bisma-shafiq-3a3b31242/)!
