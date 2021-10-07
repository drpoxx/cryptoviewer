from django.shortcuts import render
from crypto.config_file import api_key

# API and data from https://www.cryptocompare.com/
def home(request):
    import requests
    import json 
    api_request = requests.get(f"https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api})
