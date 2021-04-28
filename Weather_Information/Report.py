import requests
from pprint import pprint   # help to turn json file to tree like structure

apiKey = '71f59f8657e7fbdf97f6cb9bcf47f856'

city = input("Enter your Current City: ")

baseUrl = "https://api.openweathermap.org/data/2.5/weather?appid="+apiKey+"&q="+city

weatherData = requests.get(baseUrl).json()

pprint(weatherData)