import requests
import datetime
my_latitude = 20.593683
my_longitude = 78.962883

parameters= {
    "lat":my_latitude,
    "lng":my_longitude,
    "formatted":0,
    "tzid":"Asia/Kolkata"
}

response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()
print(data["results"]["sunset"])
a=datetime.datetime.now()
print(a)