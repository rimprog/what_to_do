from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    gender: str
    age: str
    activity: str
    mood: str
    budget: str