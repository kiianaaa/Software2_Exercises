import json
import requests

# 1 random Chuck Norris joks
response = "https://api.chucknorris.io/jokes/random"
joke = requests.get(response)
json = joke.json()
print(json["value"])