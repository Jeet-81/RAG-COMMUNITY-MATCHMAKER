from pinecone import Pinecone
from config import PINECONE_API_KEY, PINECONE_INDEX_NAME

pc = Pinecone(api_key=PINECONE_API_KEY)

index = pc.Index(PINECONE_INDEX_NAME)


def upload_profile(profile, embedding):
    """
    Upload a single profile to Pinecone.
    """

    index.upsert(
        vectors=[
            {
                "id": profile.id,
                "values": embedding,
                "metadata": {
                    "name": profile.name,
                    "college": profile.college,
                    "skills": ", ".join(profile.skills),
                    "bio": profile.bio,
                },
            }
        ]
    )


def search_profiles(query_embedding, top_k=3):
    """
    Search similar profiles.
    """

    result = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True,
    )

    return result.matches