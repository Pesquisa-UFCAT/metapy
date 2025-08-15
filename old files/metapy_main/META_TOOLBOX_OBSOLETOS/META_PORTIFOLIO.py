import yfinance as yf
import numpy as np
import pandas as pd

def STOCKS_RISK_AND_RETURN(STOCKS, START_DAY, END_DAY):
    """
    """
    PORTIFOLIO_RETURNS = []
    AUX_DATA = yf.Ticker(STOCKS[0])
    AUX_DATA = AUX_DATA.history(start = START_DAY, end = END_DAY).reset_index()
    STOCK_RETURNS = np.zeros((len(AUX_DATA) - 1, len(STOCKS)))
    # Stock performance
    # Data load in Yahoo Finance
    for I in range(len(STOCKS)):
        STOCK_DATA = yf.Ticker(STOCKS[I])
        STOCK_DATA = STOCK_DATA.history(start = START_DAY, end = END_DAY).reset_index()
        # Return
        for J in range(len(STOCK_DATA)):
            try:                
                AUX = (STOCK_DATA['Close'][J + 1] / STOCK_DATA['Close'][J] - 1)
                STOCK_RETURNS[J, I] = AUX
            except Exception as e:
                break
        STOCK_I_RETURN = np.mean(STOCK_RETURNS[:, I])
        PORTIFOLIO_RETURNS.append(STOCK_I_RETURN) 
        DF_STOCK_RETURNS = pd.DataFrame (STOCK_RETURNS, columns = STOCKS)
        AUX_RISK = DF_STOCK_RETURNS.cov()
        PORTIFOLIO_RISK = AUX_RISK.to_numpy()
    return PORTIFOLIO_RETURNS, PORTIFOLIO_RISK

def RET_VAR(X, NULL_DIC):
    """
    """
    # Input 
    RISK = NULL_DIC["RISK"]
    RETURN = NULL_DIC["RETURN"]

    # Portifolio risk ()
    VAR = 0
    for I in range(len(X)):
        if X[I] != 0:
            for J in range(len(X)):
                if X[J] != 0:
                    VAR += X[I] * X[J] * RISK[I, J] * 252
    VOL = np.sqrt(VAR)

    # Portifolio return
    RET = 0
    for I in range(len(X)):
        if X[I] != 0:
            RET += X[I] * RETURN[I] * 252
    
    #Convert to percentage
    RET = RET * 100
    VOL = VOL * 100

    return RET, VOL

def SHARP(RETURN, VAR, RISK_FREE_ASSET):
    """
    """
    # Sharp index
    if VAR != 0:
        SHARP_INDEX = (RETURN - RISK_FREE_ASSET) / VAR
    else:
        SHARP_INDEX = -1000

    return SHARP_INDEX

def PORTIFOLIO_TICKERS(INSTANCE):
    if INSTANCE == 'USA-1':
        PORT = ['AAPL','AMZN','META','GOOGL']
        START_DAY = '2016-01-01'
        END_DAY = '2017-12-31' 
        RISK_FREE = 1.78 / 100
    return PORT, START_DAY, END_DAY, RISK_FREE

def PORTIFOLIO_DIMENSION(INSTANCE):
    """
    """
    if INSTANCE == 'USA-1':
        D = 4
    return D

def PORTIFOLIO(X, RISK, RETURN):
    """
    """
    # Annual portifolio risk
    VAR = 0
    for I in range(len(X)):
        if X[I] != 0:
            for J in range(len(X)):
                if X[J] != 0:
                    VAR += X[I] * X[J] * RISK[I, J] * 252
    VOL = np.sqrt(VAR)

    # Annual portifolio return
    RET = 0
    for I in range(len(X)):
        if X[I] != 0:
            RET += X[I] * RETURN[I] * 252   
   
    return RET, VOL 