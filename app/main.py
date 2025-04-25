from fastapi import FastAPI, HTTPException # type: ignore
from app.models import MoodRequest, MoodResponse
from app.services.weather import get_weather
from app.services.music import get_song_for_mood
from app.services.matcher import is_mood_matching_weather
from app.utils import load_env

#Hello Ishwar Bali

load_env()

app = FastAPI(title="Mood Weather Song Recommender")

@app.post("/mood-check", response_model=MoodResponse)
def mood_check(payload: MoodRequest):
    city = payload.city
    mood = payload.mood.lower()

    try:
        weather_data = get_weather(city)
        matched = is_mood_matching_weather(mood, weather_data["weather"])
        song = get_song_for_mood(mood)

        return MoodResponse(
            mood=mood,
            city=city,
            weather=weather_data["weather"],
            mood_matches_weather=matched,
            recommended_song=song
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Something went wrong.")
