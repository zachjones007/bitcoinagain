#part 1 

import requests
import json
import datetime

def get_fed_data():
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": "EFFR",
        "limit": "1",
        "api_key": "FRED_API_KEY",
        "file_type": "json",
    }
    response = requests.get(url, params=params)
    response_data = response.json()
    data = response_data.get("observations", [])
    sentiment = 0
    for d in data:
        value = float(d.get("value", 0))
        sentiment = 25 if value > 2.25 else -25
    return sentiment

def analyze_data():
    today = datetime.date.today()
    if today.weekday() == 0:
        yesterday = today - datetime.timedelta(days=3)
    else:
        yesterday = today - datetime.timedelta(days=1)
    current_sentiment = get_fed_data_for_date(today)
    prev_sentiment = get_fed_data_for_date(yesterday)
    current_bias = "Unbiased" if current_sentiment == 0 else "Hawkish" if current_sentiment > 0 else "Dovish"
    print(f"Current Bias: {current_sentiment}")
    return current_sentiment

def get_fed_data_for_date(date):
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": "EFFR",
        "observation_start": date,
        "observation_end": date,
        "api_key": "FRED_API_KEY",
        "file_type": "json",
    }
    response = requests.get(url, params=params)
    response_data = response.json()
    data = response_data.get("observations", [])
    sentiment = 0
    for d in data:
        value = float(d.get("value", 0))
        sentiment = 25 if value > 2.25 else -25
    return sentiment

analyze_data()

