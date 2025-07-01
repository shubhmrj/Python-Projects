# Stock Market Exchange - Easy

This project demonstrates how to fetch stock prices and related news articles using public APIs.

## Features

- Fetches daily stock prices for a given symbol using Alpha Vantage.
- Calculates percentage change between consecutive days.
- If the change exceeds 5%, fetches the latest news articles about the company using NewsAPI.

## Requirements

- Python 3.x
- `requests`
- `python-dotenv`
- Alpha Vantage API key
- NewsAPI key

## Setup

1. Install dependencies:
   ```sh
   pip install requests python-dotenv
   ```
2. Create a `.env` file with your API keys:
   ```
   API_KEY=your_alpha_vantage_key
   news_api_key=your_newsapi_key
   ```
3. Run the script:
   ```sh
   python main.py
   ```

## License

For educational purposes only.
