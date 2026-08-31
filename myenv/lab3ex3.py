# GROQ_API_KEY = "API KEY HERE"

import os
from groq import Groq

client = Groq(
    api_key=GROQ_API_KEY,
)

systemprompt = {
    "role": "system",
    "content": """You are a resume information extraction assistant.

Your task is to extract only the fields requested by the user from the provided resume.

Rules:
1. Extract only the requested fields.
2. Use only information explicitly present in the resume.
3. Do not guess or infer missing information.
4. If a requested field is not found, use null.
5. Return valid JSON only.
6. Do not include explanations or extra text.
7. Use the exact field names requested by the user.
8. If a field contains multiple values, represent them as a JSON array.
"""
}

resume = input("Enter resume details: ")

fields = input("Enter fields to extract: ")
user_prompt = f"""
Extract these fields:
{fields}

Resume:
{resume}
"""

chat_completion = client.chat.completions.create(
    messages=[
        systemprompt,
        {
            "role": "user",
            "content": user_prompt
        }
    ],
    model="openai/gpt-oss-120b",
)

print(chat_completion.choices[0].message.content)