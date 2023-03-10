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
    current_sentiment = get_fed_data()
    current_bias = "Unbiased" if current_sentiment == 0 else "Hawkish" if current_sentiment > 0 else "Dovish"
    with open("previous_sentiment.txt", "r") as f:
        previous_bias = f.read().strip()
    if current_bias != previous_bias:
        with open("previous_sentiment.txt", "w") as f:
            f.write(current_bias)
        print(f"Unique bias change to {current_bias} on {datetime.date.today()}")
    else:
        print(f"Current bias: {current_bias}")

def get_bias_changes():
    bias_changes = []
    for i in range(10):
        today = datetime.date.today() - datetime.timedelta(days=i)
        if today.weekday() == 0:
            yesterday = today - datetime.timedelta(days=3)
        else:
            yesterday = today - datetime.timedelta(days=1)
        current_sentiment = get_fed_data_for_date(today)
        prev_sentiment = get_fed_data_for_date(yesterday)
        current_bias = "Unbiased" if current_sentiment == 0 else "Hawkish" if current_sentiment > 0 else "Dovish"
        prev_bias = "Unbiased" if prev_sentiment == 0 else "Hawkish" if prev_sentiment > 0 else "Dovish"
        if current_bias != prev_bias:
            bias_changes.append((yesterday, prev_bias, current_bias))
    for i in range(len(bias_changes) - 1, -1, -1):
        change_date, prev_bias, current_bias = bias_changes[i]
        print(f"{change_date}: {prev_bias} -> {current_bias}")

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
get_bias_changes()
