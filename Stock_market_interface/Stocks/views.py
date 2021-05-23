from django.shortcuts import render
from .FunctionDictt import callFunction_object
from .ProphetFun import Okey
from django.conf import settings
from .testermodulepopular import function
# from .testerModuleFunction import tester_function
# Create your views here.
def homepage(request) :
    dictt = callFunction_object()
    #dictt = 0
    
    return render(request , 'Home.html',{'content':dictt})

def StockPrimary(request ,slug) :
    if request.method == 'GET':
        return render(request , "Stock.html",{'content':slug})
    else :
        Okey(slug)
        return render(request , "Stock.html",{'content':slug})
    
def Graph_1(request,slug) :
    divv = function(slug)
    
    # divv= '{0}/Stock_market_interface/Stocks/popularModels'.format( settings.BASE_DIR )
    # print('{0}/Stock_market_interface/Stocks/popularModels'.format( settings.BASE_DIR ) )
    return render(request , "StockGraph1.html",{'GRAPH':divv})