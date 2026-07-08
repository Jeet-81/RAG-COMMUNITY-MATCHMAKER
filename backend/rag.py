from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from embeddings import get_embedding
from pinecone_db import search_profiles
from config import GROQ_API_KEY

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0.3,
)

prompt = ChatPromptTemplate.from_template(
"""
You are an AI community matchmaker.

A user is looking for teammates.

User Skills:
{user_skills}

User Interests:
{user_interests}

User Bio:
{user_bio}

Below are the retrieved candidate teammates.

{candidates}

Select the BEST 3 teammates.

Explain:

1. Why they match.
2. What complementary skills they bring.
3. How they could work together.

Return your answer in markdown.
"""
)


def find_matches(skills, interests, bio):

    query = f"""
    Skills: {", ".join(skills)}

    Interests: {", ".join(interests)}

    Bio: {bio}
    """

    embedding = get_embedding(query)

    results = search_profiles(embedding, top_k=5)

    candidates = ""

    for person in results:

        metadata = person.metadata

        candidates += f"""
Name: {metadata['name']}

College: {metadata['college']}

Skills: {metadata['skills']}

Bio: {metadata['bio']}

Similarity Score: {person.score}

--------------------------
"""

    chain = prompt | llm

    response = chain.invoke(
        {
            "user_skills": ", ".join(skills),
            "user_interests": ", ".join(interests),
            "user_bio": bio,
            "candidates": candidates,
        }
    )

    return response.content