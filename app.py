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
