import requests # type: ignore
import os

def get_song_for_mood(mood: str) -> str:
    api_key = os.getenv("LASTFM_API_KEY")
    url = f"http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag={mood}&api_key={api_key}&format=json"
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError("Failed to fetch song data.")

    data = response.json()
    tracks = data.get("tracks", {}).get("track", [])

    if not tracks:
        return "No song found for this mood."

    return f"{tracks[0]['name']} by {tracks[0]['artist']['name']}"
