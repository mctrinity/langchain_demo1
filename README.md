# 🚀 Conda Environment Setup for LangChain

## 📌 Step 1: Install Python 3.11 Using Conda
```bash
conda create -n langchain_env python=3.11
```
🔹 This creates a new Conda environment named `langchain_env` with **Python 3.11**.

## 📌 Step 2: Activate the Conda Environment
```bash
conda activate langchain_env
```
🔹 Always run this command before working on a LangChain app.

## 📌 Step 3: Install LangChain and Dependencies
```bash
pip install langchain openai faiss-cpu python-dotenv pipreqs
```
🔹 **Packages:**
- `langchain` → AI framework
- `openai` → OpenAI API support
- `faiss-cpu` → Vector search (use `faiss-gpu` if on a compatible system)
- `python-dotenv` → Manage API keys
- `pipreqs` → Auto-generate `requirements.txt` with only necessary dependencies

## 📌 Step 4: Create a New Project Folder
```bash
mkdir my_langchain_app && cd my_langchain_app
```
🔹 This keeps your LangChain apps organized.

## 📌 Step 5: Create a Python Script (`app.py`)
```bash
touch app.py
```
🔹 Open it in VS Code:
```bash
code app.py
```

## 📌 Step 6: Write a Simple LangChain App

🔹 **Important Note on Deprecation:**
Recent LangChain updates have changed how models are imported. If you see warnings about deprecated imports, update your code to use `langchain_openai` instead of `langchain`. The `OpenAI` class for chat models has also been moved to `ChatOpenAI`.

Paste this into `app.py`:
```python
# ✅ New (Correct Import)
from langchain_openai import ChatOpenAI

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI model
llm = ChatOpenAI(model_name="gpt-4", openai_api_key=api_key)

# Simple chatbot
while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    response = llm.invoke(query)
    print("AI:", response.content)
```

## 📌 Step 7: Generate a Clean `requirements.txt`
```bash
pipreqs . --force
```
🔹 This creates a minimal `requirements.txt` containing only necessary dependencies.

## 📌 Step 8: Run Your LangChain App
```bash
python app.py
```
🔹 This will execute the script inside the Conda environment.

## 📌 Step 9: Deactivate Conda When Done
```bash
conda deactivate
```
🔹 This exits the Conda environment and returns to the system's default Python.

---

## 💡 Enhancing Your Chatbot with Memory
If you want your chatbot to **remember past interactions**, you can add memory capabilities. Here are some options:

### 🔹 **Short-Term Memory (In-Memory Storage)**
- Use `ConversationBufferMemory` from LangChain to store recent messages in memory.
- Data is lost when the script stops.

**Example:**
```python
from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory()
```

### 🔹 **Long-Term Memory (Database or Vector Storage)**
- Store conversation history in **SQLite, PostgreSQL, or MongoDB**.
- Use **Pinecone or FAISS** for vector-based retrieval.

**Example:**
```python
from langchain.memory import ConversationSummaryBufferMemory
memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=100)
```

### 🔹 **When to Use Memory?**
- If you want **conversational context** (like remembering past questions).
- If you’re building a **customer support AI** or an **AI assistant**.

---

## 🔔 Important: Handling LangChain Deprecation Warnings
- If you see warnings like `Importing LLMs from langchain is deprecated`, ensure you're using `from langchain_openai import ChatOpenAI`.
- The `OpenAI` class should be used only for non-chat models. For chat models, use `ChatOpenAI`.
- Always keep `langchain_openai` updated using:
  ```bash
  pip install -U langchain_openai
  ```

## 🎯 Summary: Conda Workflow for LangChain
| **Task** | **Command** |
|----------|------------|
| **Create Conda Env** | `conda create -n langchain_env python=3.11` |
| **Activate Conda Env** | `conda activate langchain_env` |
| **Install Dependencies** | `pip install langchain openai faiss-cpu python-dotenv pipreqs` |
| **Create Project Folder** | `mkdir my_langchain_app && cd my_langchain_app` |
| **Create Script** | `touch app.py && code app.py` |
| **Generate Clean `requirements.txt`** | `pipreqs . --force` |
| **Run LangChain App** | `python app.py` |
| **Exit Conda Env** | `conda deactivate` |

🚀 Now you're ready to build LangChain-powered AI apps with Conda! 🎉
