from openai import OpenAI
from config import EMBEDDING_MODEL, OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def get_embedding(text):
    response = client.embeddings.create(
        input=[text],
        model=EMBEDDING_MODEL,
    )
    return response.data[0].embedding
