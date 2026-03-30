import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    # NOTE: Do NOT log user location data to protect privacy.
    # Logging city names can violate privacy regulations like GDPR
    # (General Data Protection Regulation), which treats location
    # data as personal data.

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 429:
            print("Error: Too many requests. Please try again later.")
            return

        if response.status_code != 200:
            print(f"Error: Unable to fetch data (Status Code: {response.status_code})")
            return

        data = response.json()

        temperature = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]

        print(f"Temperature: {temperature}°C")
        print(f"Condition: {weather_desc}")

    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
    except KeyError:
        print("Error: Unexpected response format from API.")


if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
