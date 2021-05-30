from django.shortcuts import render
from .FunctionDictt import callFunction_object
from .ProphetFun import Okey
from django.conf import settings
from .testermodulepopular import function
import yfinance as yf
# from .testerModuleFunction import tester_function
# Create your views here.
def homepage(request) :
    dictt = callFunction_object()
    #dictt = 0

    return render(request , 'Home.html',{'content':dictt})

def StockPrimary(request ,slug) :
    
    msft = yf.Ticker(slug)
    Heading = {
        "tsla" :  "Tesla, Inc. is an American electric vehicle and clean energy company based in Palo Alto, California. Tesla's current products include electric cars, battery energy storage from home to grid-scale, solar panels and solar roof tiles, as well as other related products and services ",
        "BABA" :"Alibaba Group Holding Limited, also known as Alibaba Group and Alibaba.com, is a Chinese multinational technology company specializing in e-commerce, retail, Internet, and technology",
        "gme":"GameStop Corp. is an American video game, consumer electronics, and gaming merchandise retailer. The company is headquartered in Grapevine, Texas, United States, and is the largest video game retailer worldwide." ,
        "irbt" : "iRobot Corporation is an American technology company that designs and builds consumer robots. It was founded in 1990 by three members of MIT's Artificial Intelligence Lab, who designed robots for space exploration and military defense",
        "msft":"Microsoft Corporation is an American multinational technology company with headquarters in Redmond, Washington. It develops, manufactures, licenses, supports, and sells computer software, consumer electronics, personal computers, and related services",
        "aapl":"Apple Inc. is an American multinational technology company headquartered in Cupertino, California, that designs, develops, and sells consumer electronics, computer software, and online services",
        "sq":"Square, Inc. is an American financial services and digital payments company based in San Francisco, California. The company was founded in 2009 by Jack Dorsey and Jim McKelvey and launched its first platform in 2010"
    }
    contents = {
            "slug" : slug ,
            "info":msft.info  ,
            "heading":Heading[slug] 
        }
    if request.method == 'GET':
        
        return render(request , "Stock.html",{'content':contents})
    else :
        Okey(slug)
        return render(request , "Stock.html",{'content':contents})
    
def Graph_1(request,slug) :
    divv = function(slug)
    return render(request , "StockGraph1.html",{'GRAPH':divv})