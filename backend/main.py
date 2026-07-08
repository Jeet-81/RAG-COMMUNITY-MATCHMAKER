from fastapi import APIRouter
from app.models import UserProfile, MatchRequest
from app.embeddings import profile_to_text, get_embedding
from app.pinecone_db import upload_profile
from app.rag import find_matches

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "healthy"}


@router.post("/register")
def register(profile: UserProfile):
    """
    Register a new community member.
    """

    text = profile_to_text(profile)

    embedding = get_embedding(text)

    upload_profile(profile, embedding)

    return {
        "message": "Profile uploaded successfully",
        "user": profile.name
    }


@router.post("/match")
def match(request: MatchRequest):
    """
    Find top teammates using RAG.
    """

    result = find_matches(
        request.skills,
        request.interests,
        request.bio,
    )

    return {
        "matches": result
    }