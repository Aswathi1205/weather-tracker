import requests

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    return (kelvin - 273.15) * 9/5 + 32


def get_weather_data(city, api_key):
    """Get weather data for a given city using OpenWeatherMap API."""
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None


def get_weather_alerts_open_meteo(lat, lon):
    """Get weather alerts using Open-Meteo API."""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        current_weather = data.get('current_weather', {})
        temperature = current_weather.get('temperature', 'N/A')
        windspeed = current_weather.get('windspeed', 'N/A')
        weathercode = current_weather.get('weathercode', 'N/A')
        return f"Temperature: {temperature}°C, Windspeed: {windspeed} km/h, Weather Code: {weathercode}"
    else:
        print("Error:", response.status_code, response.text)
        return None


def main():
    API_KEY = '393c61c1df129b5aba7950853f0d5913' 

    city = input("Enter the name of the city: ")

    weather_data = get_weather_data(city, API_KEY)

    if weather_data is not None and weather_data["cod"] != "404":
   
        kelvin_temperature = weather_data['main']['temp']

  
        pressure = weather_data['main']['pressure']
        humidity = weather_data['main']['humidity']


        weather_description = weather_data['weather'][0]['description']

     
        lat = weather_data['coord']['lat']
        lon = weather_data['coord']['lon']

     
        choice = input("Would you like to see the temperature in Celsius (C) or Fahrenheit (F)? ").strip().upper()

        if choice == 'C':
            celsius_temperature = kelvin_to_celsius(kelvin_temperature)
            print(f'Temperature in {city}: {celsius_temperature:.2f} °C')
        elif choice == 'F':
            fahrenheit_temperature = kelvin_to_fahrenheit(kelvin_temperature)
            print(f'Temperature in {city}: {fahrenheit_temperature:.2f} °F')
        else:
            print("Invalid choice. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

        
        print(f'Atmospheric Pressure: {pressure} hPa')
        print(f'Humidity: {humidity}%')
        print(f'Weather Description: {weather_description.capitalize()}')

     
        weather_alerts = get_weather_alerts_open_meteo(lat, lon)

        if weather_alerts:
            print(f"Weather Alerts: {weather_alerts}")
        else:
            print("No weather alerts for this location.")
    else:
        print("City Not Found")


if __name__ == "__main__":
    main()
