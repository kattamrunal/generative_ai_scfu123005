
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(
    api_key=GROQ_API_KEY
)

systemprompt = {
    "role": "system",
    "content": """
You are a customer support reply generator.

Your task is to generate a professional, polite, clear, and helpful reply to a customer message.

You will receive:
- Company name
- Customer message

Write the reply as if you are a customer support representative of the company.

Rules:
1. Address the customer's issue directly.
2. Be polite and empathetic.
3. Keep the response concise.
4. Do not invent policies, refunds, prices, guarantees, or facts that are not provided.
5. If information is missing, politely ask for the required details.
6. Do not mention that you are an AI.
7. Return only the final customer support reply.

Format:
Dear Customer,

[Support reply]

Best regards,
Customer Support Team
[Company Name]
"""
}

message=input("Enter customer message:")
company_name = input("Enter company name: ")

user_prompt=f"""
to={company_name}
customer_message={message}

"""

chat_completion=client.chat.completions.create(
    messages=[
        systemprompt,
        {
            "role":"user",
            "content":user_prompt
        }
    ],
    model="openai/gpt-oss-120b",
)
print(chat_completion.choices[0].message.content)