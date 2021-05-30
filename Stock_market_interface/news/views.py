from django.shortcuts import render
import requests
import json

from requests.sessions import get_environ_proxies
# Create your views here.
def newshomepage(request) :
    response = requests.get('https://newsapi.org/v2/everything?q=stock&from=2021-05-2&sortBy=publishedAt&apiKey=375cf386b7f34d84b6b3d6a0174bcb7f&fbclid=IwAR1rDFVwAptNEW-e8z9jq9aH2q5ZtDKMEAbMGMGztv6e-sg5Brcu1sWNYF8')
    geodata = response.json()
    
    #print(geodata['articles'][0]['title'])
    return render(request, 'news.html',{'data' :geodata['articles']})