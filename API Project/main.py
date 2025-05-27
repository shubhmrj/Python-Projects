import requests

response=requests.get("http://api.open-notify.org/iss-now.json")

# if response.status_code==404:
#     raise Exception("That Resource Does not Exist.")
# elif response.status_code==401:
#     raise Exception("You are not Authorize to access this data.")
response.raise_for_status()

data= response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position =(longitude,latitude)

print(iss_position)