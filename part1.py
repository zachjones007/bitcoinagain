#part 1 

import requests
import json
import datetime

def get_fed_data():
    url = "https://api.thomsonreuters.com/permid/calais"
    headers = {
        "X-AG-Access-Token": "YOUR_API_KEY_HERE",
        "Content-Type": "text/raw",
        "outputformat": "application/json"
    }
    data = "Federal Reserve"
    params = {"reltag.base": "Federal Reserve"}
    response = requests.post(url, headers=headers, params=params, data=data.encode("utf-8"))
    response_data = response.json()
    entities = response_data.get("entities", {})
    sentiment = 0
    for entity in entities.values():
        entity_sentiment = entity.get("_typeGroup", "").lower()
        if "sentiment" in entity_sentiment:
            entity_sentiment_value = entity.get("sentiment", {}).get("score", 0)
            if entity_sentiment_value > 0:
                sentiment = 25
            elif entity_sentiment_value < 0:
                sentiment = -25
            else:
                sentiment = 0
            break
    return sentiment

def analyze_data():
    fed_sentiment = get_fed_data()
    previous_bias = ""
    if fed_sentiment == 0:
        current_bias = "Unbiased"
    elif fed_sentiment > 0:
        current_bias = "Hawkish"
    else:
        current_bias = "Dovish"
    today = datetime.date.today()
    if today.weekday() == 0:
        yesterday = today - datetime.timedelta(days=3)
    else:
        yesterday = today - datetime.timedelta(days=1)
    print(f"Sentiment changed on: {yesterday}")
    prev_day_sentiment = get_fed_data_for_date(yesterday)
    if prev_day_sentiment == 0:
        previous_bias = "Unbiased"
    elif prev_day_sentiment > 0:
        previous_bias = "Hawkish"
    else:
        previous_bias = "Dovish"
    print(f"Previous bias: {previous_bias}")
    with open("previous_sentiment.txt", "w") as f:
        f.write(current_bias)
    print(f"Current bias: {current_bias}")
    return fed_sentiment

def get_fed_data_for_date(date):
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": "EFFR",
        "observation_start": date,
        "observation_end": date,
        "api_key": "YOUR_API_KEY_HERE",
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

sentiment = analyze_data()
print(sentiment)

