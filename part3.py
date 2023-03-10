# Import necessary libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# Define a function to get the text of recent Federal Reserve statements
def get_fed_statements():
    # Send a request to the Federal Reserve's press release page
    url = 'https://www.federalreserve.gov/newsevents/pressreleases.htm'
    response = requests.get(url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the link to the most recent press release
    latest_link = soup.find('a', string=re.compile('Press Release')).get('href')
    
    # Send a request to the press release page and get the content
    response = requests.get(latest_link)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the content of the press release
    content = soup.find('div', class_='col-xs-12 col-sm-8 col-md-8').get_text().strip()
    
    return content

# Print the text of the most recent Federal Reserve statement
print(get_fed_statements())
