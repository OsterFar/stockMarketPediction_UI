
import yfinance as yf
msft = yf.Ticker("MSFT")
tsla = yf.Ticker("TSLA")
BABA = yf.Ticker("BABA")
gme = yf.Ticker("GME")
irbt = yf.Ticker("IRBT")
sq = yf.Ticker("SQ")
aadp = yf.Ticker("AAPL")
    
def callFunction_object() :
   

    dictt = {
        'tsla' : tsla.info ,
        'BABA' : BABA.info ,
        'gme' : gme.info ,
        'irbt' : irbt.info ,
        'sq' : sq.info ,
        'aadp' : aadp.info ,#change
        "msft" : msft.info 
  
    }
    
    return dictt