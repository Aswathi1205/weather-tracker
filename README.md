---

# 🌦 Weather Forecast & Alerts  

A Python script to fetch current weather conditions, 7-day forecasts, and severe weather alerts using OpenWeatherMap and Open-Meteo APIs.  

## 📌 Features  
✔ Fetch current weather data for any city  
✔ 7-day and hourly weather forecasts  
✔ Severe weather alerts based on user location  
✔ Temperature units: Celsius (°C) & Fahrenheit (°F)  

## 🛠 Installation  
1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/weather-app.git
   cd weather-app
   ```
2. Install dependencies:  
   ```bash
   pip install requests
   ```
3. Get an API key from [OpenWeatherMap](https://home.openweathermap.org/api_keys)  
4. Update `API_KEY` in `weather.py`  

## 🚀 Usage  
Run the script:  
```bash
python weather.py
```
Enter a city name when prompted and choose the preferred temperature unit. The script will display:  
- Temperature  
- Atmospheric pressure  
- Humidity  
- Weather conditions  
- Severe weather alerts (if any)  

## 📌 Example Output  
```
Enter the name of the city: New York
Would you like to see the temperature in Celsius (C) or Fahrenheit (F)? C
Temperature in New York: 18.25 °C
Atmospheric Pressure: 1015 hPa
Humidity: 67%
Weather Description: Clear sky
Weather Alerts: Temperature: 18.2°C, Windspeed: 10 km/h, Weather Code: 1
```

## 📜 License  
This project is licensed under the MIT License.  

---
