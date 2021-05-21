
import yfinance as yf
ADA_USD = yf.Ticker("ADA-USD")
BNB_USD = yf.Ticker("BNB-USD")
BTC_USD = yf.Ticker("BTC-USD")
DOGE_USD = yf.Ticker("DOGE-USD")
ETH_USD = yf.Ticker("ETH-USD")

def callFunction_object() :
   

    dictt = {
        'ADA_USD' : ADA_USD.info ,
        'BNB_USD' : BNB_USD.info ,
        'BTC_USD' : BTC_USD.info ,
        'DOGE_USD' : DOGE_USD.info ,
        'ETH_USD' : ETH_USD.info ,
        
  
    }
    
    return dictt