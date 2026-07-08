from sentence_transformers import SentenceTransformer

# Load model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def profile_to_text(profile):
    """
    Convert a profile dictionary/object into a searchable string.
    """
    return f"""
    Name: {profile.name}
    College: {profile.college}
    Skills: {', '.join(profile.skills)}
    Interests: {', '.join(profile.interests)}
    Experience: {profile.experience}
    Bio: {profile.bio}
    """


def get_embedding(text):
    """
    Convert text into a vector embedding.
    """
    embedding = model.encode(text)
    return embedding.tolist()