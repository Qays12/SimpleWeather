import requests
import apikeys

api_key = apikeys.api_key


def city_search():
    city_name = input("Enter a city name... ")
    try:

        url_get_lats = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},&limit=3&appid={api_key}"

        response = requests.get(url_get_lats)
        data = response.json()

        get_lats = data[0]
        lat = get_lats['lat']
        lon = get_lats['lon']

        url_search = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

    except IndexError:
        print("City name could not be found!")
        return

    except UnboundLocalError:
        print("City name could not be found!")
        return

    response2 = requests.get(url_search)
    data2 = response2.json()

    weather_information = data2
    temp = weather_information['main']['temp']
    humidity = weather_information['main']['humidity']
    description = weather_information['weather'][0]['description']

    temp_cel = temp - 273.15

    print(f"""
{city_name}
Description: {description}
Temperature: {round(temp_cel)}°C
Humidity: {humidity}
""")


city_search()
