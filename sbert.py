import numpy as np
from sentence_transformers import SentenceTransformer
import json

with open("thread_comments.json", 'r', encoding='utf-8') as f:
    comments = json.load(f)

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def attach_embeddings(comment):
    comment['embedding'] = model.encode(comment['body']).tolist()

    for reply in comment.get('replies', []):
        attach_embeddings(reply)

for comment in comments:
    attach_embeddings(comment)

with open("thread_embeddings.json", 'w', encoding='utf-8') as f:
    json.dump(comments, f, ensure_ascii=False, indent=4)