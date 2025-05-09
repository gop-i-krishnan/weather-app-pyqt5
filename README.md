# 🌤️ Weather App (PyQt5)

A simple and elegant desktop weather application built using **PyQt5** and the **OpenWeatherMap API**. Enter a city name to get real-time temperature, weather description, and an emoji icon representing the current weather condition.

---

## 🖥️ Features

- Clean, user-friendly GUI with PyQt5
- Real-time weather data using OpenWeatherMap
- Weather condition displayed as:
  - Temperature in °C
  - Weather description
  - Emoji icon (☀️🌧️❄️ etc.)
- Robust error handling for network/API issues

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/weather-app-pyqt5.git
cd weather-app-pyqt5
```

### 2. Install dependencies

```bash
pip install PyQt5 requests
```

### 3. Get an API Key

- Sign up at [https://openweathermap.org/api](https://openweathermap.org/api)
- Replace the `api_key` in the Python script with your actual key:

```python
api_key = "YOUR_API_KEY"
```

---

## ▶️ Run the Application

```bash
python weather_app.py
```

---

## 🧠 How It Works

- User enters a city name
- App sends a request to OpenWeatherMap API
- If successful, the GUI displays:
  - Temperature in Celsius
  - Weather description (e.g. clear sky)
  - Emoji based on weather condition code

---

## ❗ Error Handling

Handles multiple error types with clear messages:
- Invalid city names
- No internet connection
- API/server errors (400, 401, 404, 500, etc.)

---

## 📌 Example Output

```
+-----------------------------+
|         Weather App         |
|-----------------------------|
| [ Enter your city name... ] |
| [     Get Weather        ]  |
|                             |
|           22.34°C           |
|              ☀️              |
|         clear sky           |
+-----------------------------+
```

---

## 📝 License

This project is open-source and available under the MIT License.
