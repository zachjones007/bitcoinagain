# Part 1
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_fed_statements():
    # Fetch the webpage containing the list of recent FOMC statements
    url = 'https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm'
    response = requests.get(url)

    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the URLs for the statements
    statement_links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('/newsevents/pressreleases/monetary20'):
            statement_links.append('https://www.federalreserve.gov' + href)

    # Fetch the content of the statements
    statements = []
    for link in statement_links:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.find('div', class_='col-xs-12 col-sm-8 col-md-8')
        if content is not None:
            content = content.get_text().strip()
            statements.append(content)

    # Create a Pandas DataFrame containing the statements
    data = {'text': statements}
    df = pd.DataFrame(data)

    return df
