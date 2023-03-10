#part 1 


import requests
from bs4 import BeautifulSoup

def get_fed_statements():
    # Define the URL for the Federal Reserve newsroom
    url = 'https://www.federalreserve.gov/newsevents/pressreleases.htm'

    # Make a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the latest news release
    release = soup.find('div', class_='col-xs-12 col-sm-8 col-md-8')
    if release is None:
        return None

    # Extract the date and text of the news release
    date = release.find('span', class_='date').get_text()
    content = release.find('div', class_='col-xs-12 col-sm-8 col-md-8').get_text().strip()

    # Create a DataFrame with the date and content of the news release
    df = pd.DataFrame({'date': [date], 'content': [content]})

    return df
