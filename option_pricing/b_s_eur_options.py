import math
from scipy.stats import norm

# create a class where all variables are shared

def dOne(underlying_price, strike_price, time_to_expiration, 
         volatility, risk_free_rate, dividends):

    dOne = (math.log(underlying_price / strike_price) 
            + (risk_free_rate + volatility**2 / 2) 
            * time_to_expiration) / (volatility * time_to_expiration**0.5)

    return dOne

def NdOne(a, b, c):
    return

def dTwo(a, b, c):
    return

def NdTwo(a, b, c):
    return

def call_option(a, b, c):
    return

def put_option(a, b, c):
    return