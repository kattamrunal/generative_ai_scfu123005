# Build an app that summarizes a research paper abstract at two levels.
# Required functionality:
# Accepts one block of text as input
# Produces a 2-line summary and a separate 5-line summary from that single input, in one run

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage

load_dotenv()

model=ChatGroq(model="openai/gpt-oss-120b")

abstract="""Artificial intelligence (AI) is increasingly being used in healthcare to support disease diagnosis. This study investigates the use of deep learning models for detecting lung diseases from chest X-ray images. The proposed model was trained on a large dataset and achieved high classification accuracy. Results show that deep learning can assist doctors by providing fast and consistent predictions. However, further validation on diverse clinical datasets is required before real-world deployment."""

messages=[
    SystemMessage(content="""You are a research paper summarization assistant.
        Generate two summaries from the given abstract:
        1. A concise 2-line summary.
        2. A detailed 5-line summary.
        Clearly separate both outputs and use only the provided text."""),
    HumanMessage(
    content=f"""Summarize this research paper abstract:{abstract}"""
)
]

result=model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(result.content)
