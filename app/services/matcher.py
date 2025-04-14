mood_weather_map = {
    "happy": ["clear", "sunny"],
    "sad": ["rain", "drizzle", "fog"],
    "angry": ["storm", "thunderstorm"],
    "calm": ["clouds", "mist"],
    "anxious": ["wind", "extreme"]
}

def is_mood_matching_weather(mood: str, weather: str) -> bool:
    possible_weathers = mood_weather_map.get(mood, [])
    return weather in possible_weathers
