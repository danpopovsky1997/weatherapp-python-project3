import requests

API_KEY = '9a1c17942dd0228bf3921afcac0459e6'

# Prompt the user to enter a city name or location.
user_input = input("Enter a city name or location: ")

# Construct the URL for the OpenWeatherMap API.
url = f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={API_KEY}"

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

    # Display the weather and temperature data to the user.
    print(f"The weather in {user_input.title()} is {weather.lower()}.")
    print(f"The temperature in {user_input.title()} is {temperature}°C.")