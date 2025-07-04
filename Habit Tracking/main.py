import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
Token = "58e6d7c1-8e5a-4b4b-8e6d-586e5a4b4b4b"
User= "shubhmrj"
user_params = {
    "token": Token,
    "username":User ,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{User}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": Token
}
# response=requests.post(url=graph_endpoint, json=graph_config , headers=headers)
# print(response.text)

today=datetime.now().strftime("%Y%m%d")
print(today)

date_config = {
    "date": today,
    "quantity": "7.5"
}
pixel_endpoint = f"{graph_endpoint}/graph1"
# response=requests.post(url=pixel_endpoint, json=date_config , headers=headers)
# print(response.text)
update_endpoint = f"{pixel_endpoint}/{today}"
upddate_config = {
    "quantity": "85"
}
# response=requests.put(url=update_endpoint, json=upddate_config , headers=headers)
# print(response.text)

delete_endpoint = f"{pixel_endpoint}/{today}"
response=requests.delete(url=delete_endpoint , headers=headers)
print(response.text)
