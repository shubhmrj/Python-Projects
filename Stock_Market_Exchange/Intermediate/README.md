# Stock Market Exchange - Intermediate

This project builds on the Easy version by integrating more advanced logic for stock and news analysis.

## Features

- Detects significant stock price changes (5% threshold).
- Fetches the top 3 news articles about the company when a significant change is detected.
- Prepares formatted messages for each news article.

## Requirements

- Python 3.x
- `requests`
- Alpha Vantage API key
- NewsAPI key

## Setup

1. Install dependencies:
   ```sh
   pip install requests
   ```
2. Add your API keys to the script or a `.env` file as needed.
3. Run the script:
   ```sh
   python main.py
   ```

## License

For educational purposes only.
