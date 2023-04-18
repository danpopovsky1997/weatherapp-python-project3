import requests
import json

with open('creds.json') as f:
    creds = json.load(f)

WEATHER_API_KEY = creds['WEATHER_API_KEY']
TIMEZONE_API_KEY = creds['TIMEZONE_API_KEY']

# Prompt the user to enter a city name or location.
user_input = input("Enter a name of a city, please be precise: ")

# Construct the URL for the OpenWeatherMap API.
url = f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={WEATHER_API_KEY}"

# Send a GET request to the API and store the response.
response = requests.get(url)

# Check if the API returned an error code.
if response.status_code == 404:
    print("No city found.")
else:
    # Parse the response JSON and extract the weather and temperature data.
    data = response.json()
    weather = data['weather'][0]['main']
    temperature = round(data['main']['temp'])

    # Get the latitude and longitude of the city.
    lat = data['coord']['lat']
    lon = data['coord']['lon']

    # Construct the URL for the TimezoneDB API.
    time_url = f"http://api.timezonedb.com/v2.1/get-time-zone?key={TIMEZONE_API_KEY}&format=json&by=position&lat={lat}&lng={lon}"

    # Send a GET request to the API and store the response.
    time_response = requests.get(time_url)

    # Check if the API returned an error code.
    if time_response.status_code == 404:
        print("Could not retrieve current time.")
    else:
        # Parse the response JSON and extract the current time data.
        time_data = time_response.json()
        current_time = time_data['formatted']

        # Display the weather, temperature, and current time data to the user.
        print(f"The weather in {user_input.title()} is {weather.lower()}.")
        print(f"The temperature in {user_input.title()} is {temperature}°C.")
        print(f"The current time in {user_input.title()} is {current_time}.")

