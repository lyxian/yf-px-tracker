import pendulum
import requests
import json 
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
file_handler = logging.FileHandler(filename='logs/px.log', mode='a', encoding='utf-8')
logger.addHandler(file_handler)

TICKERS = [
    "TSLA",
    "ETSY"
]

# CHECK IF MARKET IS OPEN
def getMarketPrice(tickers):
    for ticker in tickers:
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Mobile Safari/537.36'
        }

        URL = f"https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}"
        
        currentTime = pendulum.now(tz="Asia/Singapore").format("YYYY-MM-DD HH:mm:ss")
        response = requests.get(URL, headers=headers)
        data = json.loads(response.text.split('App.main = ')[1].split(';\n')[0])

        cashflowStatements = data['context']['dispatcher']['stores']['QuoteSummaryStore']['cashflowStatementHistory']['cashflowStatements']
        marketPrice = data['context']['dispatcher']['stores']['StreamDataStore']['quoteData'][ticker]['regularMarketPrice']['raw']

        msg = f'Current market price of {ticker} = {marketPrice} @ {currentTime}'
        logger.info(msg)
        print(msg)

# YAHOO-FINANCE (HELP)
# TTM values in QuoteTimeSeriesStore > timeSeries > trailing / annual (last 4 years)

if __name__ == '__main__':
    pass