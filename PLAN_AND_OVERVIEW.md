# 🧠 Plan & Overview – Mood Weather Song Recommender

This document outlines the **design, planning, and architecture** behind the Mood-Weather Song Recommender application. Built for the Lobb Developer Task, the app combines real-time weather data with mood input and recommends music accordingly.

---

## ✅ Objective

To build a **FastAPI-based web service** that:
- Accepts user input: **city** and **mood**
- Fetches **real-time weather** for the city
- Determines if the **mood matches the weather**
- Recommends a **song** that fits the user's mood using a music API

---

## 🧱 System Architecture


---

## ⚙️ Tech Stack

| Tool        | Purpose                          |
|-------------|----------------------------------|
| Python 3.9+ | Programming language              |
| FastAPI     | Web framework (async, lightweight)|
| Requests    | HTTP client to call external APIs |
| Dotenv      | Environment variable management   |
| Pytest      | Unit testing                      |

---

## 🔧 Key Features

- **Modular Services:** Clean separation of concerns between weather, mood-matching, and music logic.
- **External APIs:**
  - [OpenWeatherMap](https://openweathermap.org/api) for current weather.
  - [Last.fm](https://www.last.fm/api) for song recommendations.
- **Validation & Typing:** Pydantic models for request/response.
- **Environment Variables:** Secure use of API keys via `.env`.
- **Error Handling:** Custom error messages for invalid cities, API failures, and rate limits.
- **Unit Testing:** Includes tests for each service with mocked API responses.
- **Postman Collection:** Included for easy manual testing.

---

## 🔍 Mood-to-Weather Mapping

A predefined logic in `matcher.py` maps moods to suitable weather types:

| Mood     | Matching Weather Types     |
|----------|----------------------------|
| happy    | clear, sunny               |
| sad      | rain, fog, drizzle         |
| angry    | storm, thunderstorm        |
| calm     | clouds, mist               |
| anxious  | wind, extreme              |

---

## 📦 Folder Structure


---

## 🧪 Testing Strategy

Tests are written using `pytest`, focusing on:

- ✅ Successful weather fetch
- ✅ Mood-weather logic validation
- ✅ Successful song recommendation
- ✅ Error scenarios for invalid city / API failure

Mocked responses are used to simulate external APIs and ensure fast and consistent test runs.

---

## 🔐 Notes

- This project uses **only free-tier APIs** and handles common errors such as rate limits and invalid inputs.
- All code follows **PEP8 standards**, includes **docstrings**, and is structured for future scalability (e.g., you can easily plug in another song provider).
- The project is built with **readability, testability, and extendability** in mind.

---

## ✅ Summary

This app is a clean example of a service-based API system that combines multiple data sources to produce a fun, real-time result. It’s built to be:
- Easy to understand
- Modular and testable
- API-driven and maintainable

---

Feel free to reach out for any clarifications or improvements.

👨‍💻 Built with ❤️ for Lobb.
