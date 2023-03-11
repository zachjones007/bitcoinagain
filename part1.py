import requests

def get_news_sentiment():
    url = "https://newsapi.org/v2/everything?q=bitcoin&from=2022-02-08&sortBy=publishedAt&apiKey=YOUR_API_KEY"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data["articles"]
        total_articles = len(articles)
        positive_articles = 0
        for article in articles:
            title = article["title"].lower()
            if "bitcoin" in title and ("high" in title or "increase" in title or "rise" in title):
                positive_articles += 1
        positive_ratio = positive_articles / total_articles
        if positive_ratio >= 0.5:
            return 1
        else:
            return -1
    else:
        raise Exception(f"Error retrieving news: {response.status_code} - {response.text}")

def bullishorbearish():
    sentiment = get_news_sentiment()
    if sentiment == 1:
        return "Bullish"
    else:
        return "Bearish"
