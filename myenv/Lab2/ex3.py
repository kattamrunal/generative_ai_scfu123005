# Exercise 3 — Coding Assistant
# Build an app that debugs Python code.
# Required functionality:
# Accepts two separate inputs: a broken code snippet and its error message
# Returns the corrected code and a one-line explanation, clearly separated in the output
# Correctly handles at least 3 different error types when tested

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
load_dotenv()

model=ChatGroq(model="openai/gpt-oss-120b")

messages=[
    SystemMessage(
    content="""You are a Python debugging assistant. 
        Given broken code and its error, return:
        1. Corrected code
        2. One-line explanation

        Clearly separate both outputs and handle different Python error types."""
        )
]

# code=str(input("Enter Code"))
code = 'print(name)'
error = "NameError: name 'name' is not defined"

messages.append(HumanMessage(content=f"code {code}, error {error}"))
result=model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(result.content)