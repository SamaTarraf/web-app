from openai import OpenAI
import os

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

## Takes a string of text and returns a list of floats 
def embed_text(text):
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )

    return(response.data[0].embedding)
