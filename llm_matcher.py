import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "your_groq_api_key_here")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def is_match(user_query, product_title):
    prompt = f"Does the product title '{product_title}' match the query '{user_query}'? Answer Yes or No."
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mixtral-8x7b-32768",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2
    }

    try:
        res = requests.post(GROQ_API_URL, headers=headers, json=data)
        return "yes" in res.json()["choices"][0]["message"]["content"].lower()
    except Exception as e:
        print("LLM error:", e)
        return False
