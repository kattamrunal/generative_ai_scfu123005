from groq import Groq

# GROQ_API_KEY = "API KEY HERE"

client = Groq(
    api_key=GROQ_API_KEY
)

systemprompt = {
    "role": "system",
    "content": """
You are a professional translation assistant.

Translate the given sentence into the specified target language
while following the requested formality level.

Rules:
1. Preserve the original meaning accurately.
2. Use natural and grammatically correct language.
3. Follow the requested formality level: formal, neutral, or informal.
4. Do not add or remove information.
5. Return only the translated sentence.
"""
}

sentence = input("Enter sentence: ")
target_language = input("Enter target language: ")
formality = input("Enter formality level: ")

user_prompt = f"""
Sentence: {sentence}
Target language: {target_language}
Formality level: {formality}
"""

chat_completion = client.chat.completions.create(
    messages=[
        systemprompt,
        {
            "role": "user",
            "content": user_prompt
        }
    ],
    model="openai/gpt-oss-120b"
)

print(chat_completion.choices[0].message.content)