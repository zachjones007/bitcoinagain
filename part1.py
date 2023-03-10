import requests
import json
from datetime import datetime

def get_bart_data():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    data = json.loads(response.text)
    rate = data['bpi']['USD']['rate']
    return float(rate.replace(',', ''))

def get_federal_reserve_data():
    url = 'https://www.federalreserve.gov/releases/h3/current/h3.htm'
    response = requests.get(url)
    table_start = '<table cellpadding="3" cellspacing="0" width="100%">'
    table_end = '</table>'
    table_data = response.text.split(table_start)[1].split(table_end)[0]
    row_start = '<tr>'
    row_end = '</tr>'
    cell_start = '<td'
    cell_end = '</td>'
    rows = table_data.split(row_start)[1:]
    last_row = rows[-1]
    cells = last_row.split(cell_start)[1:]
    interest_rate = cells[1].split(cell_end)[0]
    return float(interest_rate)

def predict_market():
    bart = get_bart_data()
    interest_rate = get_federal_reserve_data()
    if bart > 50000 and interest_rate < 0.25:
        return 'Bullish'
    else:
        return 'Bearish'

if __name__ == '__main__':
    market_prediction = predict_market()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'Market prediction at {current_time}: {market_prediction}')

