import os
from tkinter.constants import CURRENT

import dotenv
import requests
import time

Current_Date=time.strftime("%Y/%m/%d")
Current_Time=time.strftime("%H:%M:%S")


dotenv.load_dotenv()

API_KEY = os.getenv("API_KEY")
APP_ID = os.getenv("APP_ID")
print(f"API_KEY: {API_KEY}, APP_ID: {APP_ID}")

url = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("What do you want to do: ")
print(f"User Input: {query}")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

parameters = {
    "query": query,
    "gender": "male",
    "weight_kg": 72,
    "height_cm": 172,
    "age": 24
}

response = requests.post(url, json=parameters, headers=headers)

print(f"Status Code: {response.status_code}")
print("Response JSON:")
result=response.json()
print(result)

# For post data on google sheet.

for exercise in result["exercises"]:
    body = {
        "workout":{
        "Date": Current_Date,
        "Time": Current_Time,
        "exercise": exercise["name"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
    }
}

google_sheet=os.getenv("post_url")

response_sheet = requests.post(google_sheet, json=body)

print(response_sheet.text)
