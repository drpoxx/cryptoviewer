from django.shortcuts import render
from crypto.config_file import api_key

# API and data from https://www.cryptocompare.com/
def home(request):
    import requests
    import json 

    # Grab Crypto Price Data
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
    import requests
    import json 
    if request.method == 'POST':
        quote = request.POST['quote']
        quote = quote.upper()

        # Grab Crypto Price Data
        crypto_request = requests.get(f"https://min-api.cryptocompare.com/data/pricemultifull?fsyms={quote}&tsyms=GBP&api_key={api_key}")
        crypto = json.loads(crypto_request.content)

        return render(request, 'prices.html', {
            'quote': quote,
            'crypto': crypto
            })
    else:
        notfound = "Please enter the crypto currence into the 'Lookup Crypto' field to search for the latest price. \nPlease use the short-name tags. \nIf you want to search for multiple crypto currency type them seperated by a comma."
        return render(request, 'prices.html', {'notfound': notfound})

