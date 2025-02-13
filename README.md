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
pip install langchain openai faiss-cpu python-dotenv
```
🔹 **Packages:**
- `langchain` → AI framework
- `openai` → OpenAI API support
- `faiss-cpu` → Vector search (use `faiss-gpu` if on a compatible system)
- `python-dotenv` → Manage API keys

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
Paste this into `app.py`:
```python
from langchain.llms import OpenAI
import os

# Set API Key
os.environ["OPENAI_API_KEY"] = "your-api-key-here"

# Initialize LangChain with OpenAI
llm = OpenAI(model_name="text-davinci-003")

# Simple chatbot
query = input("Ask something: ")
response = llm(query)
print("AI Response:", response)
```

## 📌 Step 7: Run Your LangChain App
```bash
python app.py
```
🔹 This will execute the script inside the Conda environment.

## 📌 Step 8: Deactivate Conda When Done
```bash
conda deactivate
```
🔹 This exits the Conda environment and returns to the system's default Python.

---

## 🎯 Summary: Conda Workflow for LangChain
| **Task** | **Command** |
|----------|------------|
| **Create Conda Env** | `conda create -n langchain_env python=3.11` |
| **Activate Conda Env** | `conda activate langchain_env` |
| **Install Dependencies** | `pip install langchain openai faiss-cpu` |
| **Create Project Folder** | `mkdir my_langchain_app && cd my_langchain_app` |
| **Create Script** | `touch app.py && code app.py` |
| **Run LangChain App** | `python app.py` |
| **Exit Conda Env** | `conda deactivate` |

🚀 Now you're ready to build LangChain-powered AI apps with Conda! 🎉
