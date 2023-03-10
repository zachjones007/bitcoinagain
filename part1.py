#part 1 

import requests
import pandas as pd

def get_fed_statements():
    url = "https://wireapi.reuters.com/v8/feed/rcom/us/marketnews/N2MhQzEyNjM5Mw==?format=json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    articles = data["wireitems"]
    articles = [article for article in articles if article["type"] == "story"]
    df = pd.DataFrame(articles, columns=["date", "headline", "summary"])
    df["date"] = pd.to_datetime(df["date"])
    return df
