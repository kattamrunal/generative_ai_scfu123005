# Exercise 5 — AI Tutor
# Build an app that tutors a first-year student on one topic.
# Required functionality:
# Accepts a topic name and gives an initial explanation
# Detects when the user says something like "I don't get it" and re-explains differently
# Tracks how many times it has re-explained the same topic in the session
# Runs in a loop until the user says they understand or exits

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage

load_dotenv()

model=ChatGroq(model="openai/gpt-oss-120b")

topic=input("Enter the topic:")

message=[
    SystemMessage(content="""You are a friendly tutor for first-year students.
        Explain the given topic simply.
        If the student says they don't understand, re-explain it using a different approach.
        Track the number of re-explanations for the topic.
        Stop when the student says they understand or exits."""),
    HumanMessage(content=f"Teach me this topic: {topic}")
]

result=model.invoke(message)
message.append(AIMessage(content=result.content))
print(result.content)
