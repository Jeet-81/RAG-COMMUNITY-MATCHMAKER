from embeddings import get_embedding
from pinecone_db import search_profiles

query = """
Python
Machine Learning
Statistics
Looking for AI teammates
"""

embedding = get_embedding(query)

matches = search_profiles(embedding)

print()

print("Top Matches")

print("-" * 40)

for match in matches:

    print(match.metadata["name"])

    print(match.metadata["skills"])

    print("Score:", round(match.score, 3))

    print()