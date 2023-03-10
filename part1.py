#part 1 

import requests
import json

def get_fed_statements(api_key):
    url = "https://api.thomsonreuters.com/permid/calais"
    headers = {
        "Content-Type": "text/raw",
        "X-AG-Access-Token": api_key,
        "outputformat": "application/json"
    }

    # Fetch the latest news articles from Reuters
    response = requests.get("https://www.reuters.com", headers=headers)
    articles = []
    if response.ok:
        articles = response.json().get("value", [])

    # Extract statements from the Reuters articles using the Thomson Reuters API
    statements = []
    for article in articles:
        if article.get("_type", "") == "Article":
            content = article.get("body", "")
            if content:
                payload = content.encode("utf-8")
                response = requests.post(url, headers=headers, data=payload)
                if response.ok:
                    data = response.json()
                    for key in data:
                        if "http://d.opencalais.com/persorg" in key and "policy" in data[key]:
                            statements.append(data[key]["policy"])

    return statements

