# Stock Market Exchange - Hard

This advanced project combines stock price monitoring, news aggregation, and SMS notifications.

## Features

- Monitors stock price changes using Alpha Vantage.
- Fetches and formats the top 3 news articles about the company using NewsAPI.
- Sends SMS alerts for significant stock price changes using Twilio.

## Requirements

- Python 3.x
- `requests`
- Alpha Vantage API key
- NewsAPI key
- Twilio account and credentials

## Setup

1. Install dependencies:
   ```sh
   pip install requests
   ```
2. Add your API keys and Twilio credentials to a `.env` file or directly in the script.
3. Run the script:
   ```sh
   python main.py
   ```

## License

For educational purposes only.

## Detailed Description

This project is designed to help users keep track of stock market changes and relevant news about specific companies. It uses the Alpha Vantage API to monitor stock price changes, the NewsAPI to fetch the latest news articles, and Twilio to send SMS notifications to users.

### Alpha Vantage

Alpha Vantage provides real-time and historical data on stocks, ETFs, mutual funds, and cryptocurrencies. In this project, we use Alpha Vantage to get the latest stock price and monitor any significant changes.

### NewsAPI

NewsAPI is a simple HTTP REST API for searching and retrieving live articles from all over the web. We use it to fetch the top news articles related to the company whose stock price we are monitoring.

### Twilio

Twilio is a cloud communications platform that allows you to send and receive SMS messages through its web service APIs. We use Twilio to send SMS alerts to users when there is a significant change in the stock price.

## How It Works

1. The user specifies the stock ticker symbol and the threshold for significant price changes.
2. The script fetches the latest stock price from Alpha Vantage.
3. If the price change is significant, the script fetches the top 3 news articles about the company from NewsAPI.
4. The script sends an SMS alert to the user with the stock price change and the top news articles.

## Customization

Users can customize the following parameters in the script:

- `STOCK_TICKER`: The stock ticker symbol for the company you want to monitor.
- `PRICE_CHANGE_THRESHOLD`: The threshold for significant price changes (in percentage).
- `SMS_TO`: The phone number to send SMS alerts to.
- `SMS_FROM`: The Twilio phone number to send SMS alerts from.

## Troubleshooting

- Ensure that you have installed all the required dependencies.
- Check that your API keys and Twilio credentials are correct.
- If you encounter any issues, refer to the documentation for Alpha Vantage, NewsAPI, and Twilio for troubleshooting tips.

## Acknowledgments

- [Alpha Vantage](https://www.alphavantage.co/) for the stock market data.
- [NewsAPI](https://newsapi.org/) for the news articles.
- [Twilio](https://www.twilio.com/) for the SMS notifications.
- [Python](https://www.python.org/) for the programming language.
- [Requests](https://docs.python-requests.org/en/master/) for the HTTP library.
