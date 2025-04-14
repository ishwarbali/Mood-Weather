from pydantic import BaseModel # type: ignore

class MoodRequest(BaseModel):
    city: str
    mood: str

class MoodResponse(BaseModel):
    mood: str
    city: str
    weather: str
    mood_matches_weather: bool
    recommended_song: str
