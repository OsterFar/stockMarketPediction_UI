from django.shortcuts import render
from .FunctionDictt import callFunction_object
from .ProphetFun import Okey
from .testerModuleFunction import tester_function
# Create your views here.
def homepage(request) :
    dictt = callFunction_object()
    #dictt = 0
    
    return render(request , 'Home.html',{'content':dictt})

def StockPrimary(request ,slug) :
    if request.method == 'GET':
        return render(request , "Stock.html")
    else :
        Okey(slug)
        return render(request , "Stock.html")
    
def Graph_1(request,slug) :
    divv = tester_function('tsla')
    return render(request , "StockGraph1.html",{'GRAPH':divv})