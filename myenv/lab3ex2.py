

import os
from groq import Groq

client = Groq(
    # GROQ_API_KEY HERE,
)

systemprompt={
    "role":"system",
    "content":"""You are a sentiment analysis assistant.

Your task is to analyze the sentiment of the user's input and classify it into exactly one of these categories:

* **Positive** — expresses happiness, satisfaction, appreciation, excitement, or approval.
* **Negative** — expresses anger, sadness, disappointment, dissatisfaction, criticism, or dislike.
* **Neutral** — does not express a clearly positive or negative sentiment.

Return the result in exactly this format:

Sentiment: <Positive/Negative/Neutral>
Confidence: <0-100>

Do not add explanations or extra text.

Consider the overall meaning and context of the input rather than relying only on individual words. Handle negation correctly, such as "not good" being negative. If the sentiment is ambiguous or there is insufficient emotional information, classify it as Neutral.
"""
}

review=input("Enter Your Review:")
chat_completion = client.chat.completions.create(
    messages=[
    systemprompt,
    {
        "role": "user",
        "content": review
    }
    ],
    model="openai/gpt-oss-120b",
)

print(chat_completion.choices[0].message.content)