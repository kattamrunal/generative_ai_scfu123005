from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")

draft_text = input("Enter draft text: ")
issue_to_fix = input("Issue to fix: ")

for round_number in range(1, 4):

    messages = [
        SystemMessage(
            content="""You are a content editor.Fix only the given issue in the draft.Keep the original meaning."""),
        HumanMessage(content=f"""Draft:{draft_text} Issue:{issue_to_fix}""")
    ]

    result = model.invoke(messages)
    draft_text = result.content

    print(f"\n--- Round {round_number} ---")
    print(draft_text)

print("\nFinal revised draft:")
print(draft_text)