# Exercise 2 — Content Generator
# Build an app that generates Instagram captions for a college fest.
# Required functionality:
# Accepts two inputs: fest name and fest theme
# Generates exactly 3 caption options, each under 30 words
# Each caption includes at least one relevant hashtag

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage

load_dotenv()

model=ChatGroq(model="openai/gpt-oss-20b")

chat_history=[
    SystemMessage(
        content="""You are an Instagram caption generator for college fests.

    Your task is to create engaging, creative, and student-friendly Instagram captions based on:

    * Fest name
    * Fest theme"""
    )
]

festname=input("Fest Name:")
festtheme=input("Fest Theme:")
chat_history.append(HumanMessage(content=f"Fest Name: {festname}\nFest Theme: {festtheme}"))
result=model.invoke(chat_history)
chat_history.append(AIMessage(content=result.content))
print(result.content)
