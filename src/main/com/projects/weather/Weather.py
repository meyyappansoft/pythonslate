import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
API_KEY = "aaf1e52c64445b07dece7f91fa090c12"

city = input("Enter city name : ")

if city == "":
    print("Not a valid city name!")
    quit()

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print("Weather is :", weather)
    temp = round(data['main']['temp'] - 273.15, 2)
    print("Temperature is ",temp, "celsicus")

else:
    print("Error getting data for the city! Try again.")
