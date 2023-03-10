#part 1 

import requests
from bs4 import BeautifulSoup

def get_federal_reserve_data():
    url = "https://www.federalreserve.gov/newsevents/speeches.htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    speeches = soup.find_all('div', class_='col-xs-12 col-sm-6 col-md-4')
    return speeches

def analyze_federal_reserve(speeches):
    keywords = ['dovish', 'hawkish']
    speech_text = ''
    for speech in speeches:
        speech_text += speech.text.lower()
    if any(keyword in speech_text for keyword in keywords):
        if 'dovish' in speech_text:
            return -1 # bearish
        else:
            return 1 # bullish
    else:
        return 0 # neutral

