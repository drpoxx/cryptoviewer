from django.shortcuts import render
from crypto.config_file import api_key

# API and data from https://www.cryptocompare.com/
def home(request):
    import requests
    import json 
    # Grab Crypto Price Data
    #
    price_request = requests.get(f"https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,SHIB,DOT,SOL,ADA,DODGE,FTM,XRP,BUSD&tsyms=GBP&api_key={api_key}")
    price = json.loads(price_request.content)
    
    # Grab Crypto News
    api_request = requests.get(f"https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key={api_key}")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {
        'api': api,
        'price': price
        })

def prices(request):
    return render(request, 'prices.html', {})
