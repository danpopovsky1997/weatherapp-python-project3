import requests

location = input("Enter your desired location(post or city name): ")
api_key = "#"

url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
weather_data = response.json()

else:
    print("Error: Could not retrieve weather data.")

