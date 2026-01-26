import requests
import os
from dotenv import load_dotenv

"load .env folder"
load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY=os.getenv("API_KEY")

# You can now use api_key in your application
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
parameter={
	"function":"TIME_SERIES_DAILY",
	"symbol":"IBM",
	"apikey":API_KEY
}
response = requests.get(STOCK_ENDPOINT,params=parameter)
data = response.json()
Daily_Time_series=data["Time Series (Daily)"]
specific_data=[value for (key,value) in Daily_Time_series.items()]
yesterday_data=specific_data[0]["4. close"]
print(yesterday_data)


# print(yesterday)
# print(data)
#TODO 2. - Get the day before yesterday's closing stock price
a_day_before_yesterday=specific_data[1]["4. close"]
print(a_day_before_yesterday)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference=abs(float(yesterday_data)-float(a_day_before_yesterday))
print(difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

difference_percentage = (difference/float(yesterday_data))*100
print("yesterday_percentage :",difference_percentage)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if difference_percentage> 5:
	print("getnews")

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

news_api_key=os.getenv("news_api_key")
news_parameters={
	"q":"IBM",
	"from":"2025-06-01",
	"sortedBy":"publishedAt",
	"apikey":news_api_key
}
news_data=requests.get(NEWS_ENDPOINT,params=news_parameters)
print(news_data.json())

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
first_3=news_data[:2]
print(first_3)

## STEP 3: Use twilio.com/docs/sms/quickstart/python
#to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 


#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
