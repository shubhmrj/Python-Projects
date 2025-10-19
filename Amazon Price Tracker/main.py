from bs4 import BeautifulSoup
import requests
import os
import smtplib
import datetime
from dotenv import load_dotenv

load_dotenv()
date=datetime.datetime.now().strftime("%d/%m/%Y")

# static url to get the price
url="https://appbrewery.github.io/instant_pot/"

# live url to get the price which is dyanmaic hard to parse so i take the static url
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# ADD header for look my requests more realistics rather than ai generated 
# requests.get(url, params=None, headers=None, cookies=None, auth=None, timeout=None) this is params of requests

# header

header={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
    "Dnt": "1",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Windows",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
}

response=requests.get(url=live_url,headers=header)
soup=BeautifulSoup(response.text,"html.parser")

# check whether what kind of requests i get
print(soup.prettify()[:2000])

price=soup.find(class_="a-price-whole").get_text()

price_without_currency = price.split("$")[1]

price_as_float=float(price_without_currency)

print(price_as_float)


# Send Email if price less than 100
if price_as_float<100:
    my_email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs="srnwda@gmail.com",
            msg=f"Subject:Amazon Price Alert\n\n{price}\n{live_url}\n at the time of {date}"
)
        
#  you can try with static becuase live might not run