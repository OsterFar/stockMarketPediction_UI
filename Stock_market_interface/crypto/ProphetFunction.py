#!/usr/bin/env python
# coding: utf-8

# # **Functions**

# In[2]:
import numpy as np 
import sys
import subprocess
#subprocess.check_call([sys.executable, "-m", "pip", "install", "fbprophet"])
#subprocess.check_call([sys.executable, "-m", "pip", "install", "yfinance"])
import yfinance as yf
from fbprophet import Prophet
import pandas as pd 
import matplotlib.pyplot as plt
from fbprophet.plot import plot_plotly, plot_components_plotly


def get_ticker_hist(ticker):
  label = yf.Ticker(ticker)
  history = label.history(period='10y')
  history.reset_index(inplace=True)
  return history


def get_frame(history):
    #Select Date and Price and rename the features: These are required for the model fitting
    df = history[["Date","Close"]] 
    df = df.rename(columns = {"Date":"ds","Close":"y"}) 
    return df


def prophet_pred(df):
    # The Prophet class (model)
    fbp = Prophet(daily_seasonality = True) 
    # Fit the model 
    fbp.fit(df)
    # We need to specify the number of days in future We'll be predicting the full 2021 stock prices
    fut = fbp.make_future_dataframe(periods=365) 
    forecast = fbp.predict(fut)
    return forecast, fbp


def plotter_prophet(model, frcst):
    fig = plot_plotly(model, frcst, figsize=(900,600), xlabel='Time period', ylabel='Price')
    fig.update_layout(hovermode='x')
    fig.show()

def Okey(slug) :
    history = get_ticker_hist(slug)
    frame = get_frame(history)
    f, m = prophet_pred(frame)
    plotter_prophet(m, f)