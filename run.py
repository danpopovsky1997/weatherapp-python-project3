import requests

parameter = "t_2m:C"
location = input("Enter your desired location(latitude,longitude): ")
api_key = "#"

url = f"https://api.meteomatics.com/{parameter}/now/json?latlon={location}&apikey={api_key}"

response = requests.get(url)

if response.status_code == 200:
weather_data = response.json()

else:
    print("Error: Could not retrieve weather data.")

