
import requests
import smtplib
from datetime import datetime

my_latitude=22.700720
my_longitude=75.934700


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data=response.json()
    current_latitude=float(data["iss_position"]["latitude"])
    current_longitude=float(data["iss_position"]["longitude"])

    if my_longitude+5==current_longitude <=my_longitude-5 and my_latitude+5==current_latitude<=-5:
        return True

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


my_email = "shubmrj@gmail.com"
password = "vcwsqfzbmgjpgjkx"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs="srnwda@gmail.com",
            msg="Subject:ISIS\n\n Hello , ISIS on your head. "
        )
print("Successful Executed")


