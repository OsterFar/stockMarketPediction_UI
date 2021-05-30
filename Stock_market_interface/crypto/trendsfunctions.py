import copy
import matplotlib.pyplot as plt
from sklearn import model_selection
import numpy as np
import pandas as pd 
import sys
import subprocess
# subprocess.check_call([sys.executable, "-m", "pip", "install", "yfinance"])
# subprocess.check_call([sys.executable, "-m", "pip", "install", "plotly"])
import yfinance as yf
import plotly.graph_objects as go
import sys
import subprocess
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout


sc = MinMaxScaler(feature_range = (0, 1))


def download_stock_data(stock, start, end):
  stock_data = yf.download(stock, start, end)
  return stock_data


def plotter(newtest, testdata, predicted_stock_df, stock_ticker):
  trace1 = {
    'x': newtest.index,
    'close': testdata['Close'],'open': testdata['Open'],'high': testdata['High'],
    'low': testdata['Low'],'type': 'candlestick','name': stock_ticker,'showlegend': True
  }
  trace3 = {
    'x': predicted_stock_df.index, 
    'y': predicted_stock_df['y_pred'],'type': 'scatter','mode': 'lines',
    'line': {
        'width': 1,
        'color': 'blue'
    },
    'name': 'predicted'
  }
  data = [trace1, trace3]
  layout = go.Layout({
    'title': {
        'text': 'LSTM'+stock_ticker+'Trends',
    }
  })
  fig = go.Figure(data=data, layout=layout)
  fig.update_layout(barmode='group', hovermode='x')
  fig.show()
  return fig


def get_df(stk_data):
  data2 = pd.DataFrame()
  stk_data['Date'] = stk_data.index
  data2 = pd.DataFrame(columns = ['Date', 'Open', 'High', 'Low', 'Close'])
  data2['Date'] = stk_data['Date']
  data2['Open'] = stk_data['Open']
  data2['High'] = stk_data['High']
  data2['Low'] = stk_data['Low']
  data2['Close'] = stk_data['Close']
  return data2
  
  
def get_test_set(stock_train_data, testdata):
  train_set, training_set_scaled = 0, 0
  train_set = stock_train_data.iloc[:, 4:5].values
  training_set_scaled = sc.fit_transform(train_set)
  test_data_shape = testdata.shape[0]
  real_stock_price = 0
  real_stock_price = testdata.iloc[:, 4:5].values
  dataset_total = pd.concat((stock_train_data['Close'], testdata['Close']), axis = 0)
  inputs = dataset_total[len(dataset_total) - len(testdata) - 60:].values
  inputs = inputs.reshape(-1,1)
  inputs = sc.transform(inputs)
  X_test = []
  for i in range(60, test_data_shape+60):
    X_test.append(inputs[i-60:i, 0])
  X_test = np.array(X_test)
  X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
  return X_test


def revert_stock_price(predicted_stock_price):
  pred_stk_p = sc.inverse_transform(predicted_stock_price)
  return pred_stk_p