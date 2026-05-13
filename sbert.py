from sentence_transformers import SentenceTransformer
import json

sentences = []
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


with open("thread_comments.json", 'r', encoding='utf-8') as f:
    comments = json.load(f)

for comment in comments[:10]:
    sentences.append(comment["body"])

embeddings = model.encode(sentences)
print(embeddings.shape)

similarities = model.similarity(embeddings, embeddings)
print(similarities)