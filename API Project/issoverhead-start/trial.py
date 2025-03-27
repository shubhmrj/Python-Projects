import requests

# from main import latitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")

data=response.json()

current_latitude=data["iss_position"]["latitude"]
current_longitude=data["iss_position"]["longitude"]

