from django.shortcuts import render
from .ProphetFunction import Okey
from .FunctionDictt import callFunction_object
from .testermodulecrypto import tester_Cryto_function
import yfinance as yf
# Create your views here.
def cryptohomepage(request) :
   # AMZN = yf.ticker('AMZN')
    if request.method =="GET" :
        dictt = callFunction_object()
        #dictt = 0
        
        
        return render(request , 'CrytoMain.html',{'content':dictt})
    else :
        
        dictt = callFunction_object()
        #dictt = 0
        
        
        return render(request , 'CrytoMain.html',{'content':dictt})

def cryptoPrimary(request,slug) :
    
    msft = yf.Ticker("{0}-USD".format(slug.upper()))
    
    contents = {
            "slug" : slug ,
            "info":msft.info  
        }
    if request.method == 'GET':
        return render(request , "Cryto.html",{'content':contents})
    else :
        
        Okey("{0}-USD".format(slug))
        return render(request , "Cryto.html",{'content':contents})


def GraphView(request , slug) :
    print(slug)
    okey = tester_Cryto_function(slug)
    divv = "hello "
    return render(request , "CrytoGraph1.html",{'GRAPH':divv})