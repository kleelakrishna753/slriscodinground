from openai import OpenAI
from config import OPENAI_API_KEY, CHAT_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def call_openai_chat(context_chunks, query):
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Use the provided context to answer the question."},
        {"role": "user", "content": f"Context:\n{context_chunks}\n\nQuestion:\n{query}"}
    ]
    
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=messages,
        temperature=0.2
    )
    
    return response.choices[0].message.content
