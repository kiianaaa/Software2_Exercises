import json
import requests

# 1 random Chuck Norris joks

response = "https://api.chucknorris.io/jokes/random"
joke = requests.get(response)
json = joke.json()
print(json["value"])


# 2 weather API

city = input("Please enter the name of the city you want to check: ")
key = ("I didn't register :) ")

request = "https://api.openweathermap.org/data/2.5/weather?q=" + \
    city + "&appid=" + key + "&units=metric"

try:
    response = requests.get(request)
    if response.status_code == 200:
        json_response = response.json()

    except requests.exceptions.RequestException as e:
        print("We countered an error. Try again.")
