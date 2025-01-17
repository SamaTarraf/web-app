from openai import OpenAI
import EmbeddingsFunction
from pinecone import Pinecone
import os

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
pc = Pinecone(api_key= os.getenv("PINECONE_API_KEY"))
index = pc.Index("docs")

##takes the question and returns the related chunks
def get_docs(question):
    ##get embedding of the question and get a list of rows that are related
    embedding = EmbeddingsFunction.embed_text(question)
    docs = index.query(vector=embedding, top_k=3, include_metadata=True)
    
    ##creates a list of text from the rows
    context = []
    for match in docs['matches']:
        context.append(match['metadata']['text'])
    
    return(context)

def generate_text(question):
    context = get_docs(question)
    context = "\n".join(context)
    
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
        ]
    )

    print(completion)

#if __name__ == '__main__':
#    generate_text("how to train the halfpass?")