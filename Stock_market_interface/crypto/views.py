from django.shortcuts import render
from .ProphetFunction import Okey
from .FunctionDictt import callFunction_object
# Create your views here.
def cryptohomepage(request) :
   # AMZN = yf.ticker('AMZN')
    dictt = callFunction_object()
    #dictt = 0
    
    return render(request , 'CrytoMain.html',{'content':dictt})



def cryptoPrimary(request,slug) :
    
    
    if request.method == 'GET':
        return render(request , "Cryto.html")
    else :
        Okey(slug)
        return render(request , "Cryto.html")
