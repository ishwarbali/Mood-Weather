# 🎵 Mood-Weather Song Recommender API

This application takes a **user's current mood and city**, checks if the **current weather matches the mood**, and recommends a **song** that fits the user's mood.

---

## 🚀 Features

- ✅ Fetches real-time weather using **OpenWeatherMap API**
- ✅ Mood-to-weather matching logic
- ✅ Recommends songs using **Last.fm API**
- ✅ Built with **FastAPI** (lightweight, modern framework)
- ✅ Modular architecture with unit tests
- ✅ Swagger/OpenAPI documentation auto-generated
- ✅ Error handling, clean code, and easy to extend

---

## 📦 Tech Stack

- **Python 3.9+**
- **FastAPI**
- **Requests**
- **dotenv**
- **Pytest**

---

## 📥 Installation

### 1. Clone the project
```bash
git clone <repo-url>
cd lobb_mood_app


2. Create virtual environment & install dependencies
bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
3. Set up environment variables
Create a .env file in the root directory using .env.example as a reference:

ini
OPENWEATHER_API_KEY=your_openweather_api_key
LASTFM_API_KEY=your_lastfm_api_key
▶️ Running the App
bash

uvicorn app.main:app --reload
Now open your browser at:

📍 http://127.0.0.1:8000/docs – Interactive Swagger UI
📍 http://127.0.0.1:8000/redoc – ReDoc API Docs

📬 Example API Usage
Endpoint: POST /mood-check
Request Body:

json
Copy
Edit
{
  "city": "London",
  "mood": "happy"
}
Response:

json
Copy
Edit
{
  "mood": "happy",
  "city": "London",
  "weather": "clear",
  "mood_matches_weather": true,
  "recommended_song": "Happy by Pharrell Williams"
}
🧠 Architecture Diagram
mermaid
Copy
Edit
graph TD
    A[User] -->|POST /mood-check| B[FastAPI App (main.py)]

    B --> C[Weather Service]
    C -->|GET Weather by City| D[OpenWeatherMap API]
    D -->|Weather Data| C

    B --> E[Mood-Weather Matcher]
    E -->|Checks Mood vs Weather| B

    B --> F[Music Service]
    F -->|Get Top Track by Mood| G[Last.fm API]
    G -->|Song Data| F

    B -->|JSON Response| A[User]
🧪 Running Tests
bash
Copy
Edit
pytest tests/
Unit tests are located in the /tests folder and cover:

Weather API logic

Mood matching logic

Music recommendation logic

