import requests # type: ignore
import os

def get_weather(city: str) -> dict:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError("Could not fetch weather data.")

    data = response.json()
    weather_main = data["weather"][0]["main"].lower()

    return {"weather": weather_main}
