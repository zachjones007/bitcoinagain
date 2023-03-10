import requests

def get_federal_reserve_data():
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
                sentiment = 1
            else:
                sentiment = -1
            break
    return sentiment
