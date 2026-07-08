try:
    from pydantic import BaseModel
except ImportError:
    class BaseModel:
        pass

from typing import List


class UserProfile(BaseModel):
    id: str
    name: str
    college: str
    skills: List[str]
    interests: List[str]
    experience: str
    github: str
    bio: str


class MatchRequest(BaseModel):
    skills: List[str]
    interests: List[str]
    bio: str