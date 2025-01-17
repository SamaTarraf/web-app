from pinecone import Pinecone
import pandas as pd
import EmbeddingsFunction
import os

pc = Pinecone(api_key= os.getenv("PINECONE_API_KEY"))
index = pc.Index("docs")

rows = pd.read_csv("content.csv")

embeddings = []

#puts together list of ids and embeddings from csv file
for i, row in rows.iterrows():
    embedding = EmbeddingsFunction.embed_text(row['content'])
    embeddings.append({"id" : str(row['id']), "metadata" : {"text" : row['content']}, "values" : embedding})

index.upsert(vectors=embeddings)

print("Embeddings stored in knowledge base")
