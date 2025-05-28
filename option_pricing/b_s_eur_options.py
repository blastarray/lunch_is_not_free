import math
from scipy.stats import norm

# create a european option class

def dOne(underlying_price, strike_price, time_to_expiration, 
         volatility, risk_free_rate, dividend_yield):

    dOne = (math.log(underlying_price / strike_price) 
            + (risk_free_rate - dividend_yield + 0.5 * volatility**2) 
            * time_to_expiration) / (volatility * time_to_expiration**0.5)

    return dOne

def NdOne(underlying_price, strike_price, time_to_expiration, 
         volatility, risk_free_rate, dividend_yield):

    NdOne = norm.cdf(dOne(underlying_price, strike_price, time_to_expiration, 
         volatility, risk_free_rate, dividend_yield))
    
    return NdOne

def dTwo(underlying_price, strike_price, time_to_expiration, 
         volatility, risk_free_rate, dividend_yield):

    dTwo = (dOne(underlying_price, strike_price, time_to_expiration, 
                volatility, risk_free_rate, dividend_yield) 
                - volatility * math.sqrt(time_to_expiration))

    return dTwo

def NdTwo(underlying_price, strike_price, time_to_expiration, 
          volatility, risk_free_rate, dividend_yield):

    NdTwo = norm.cdf(dTwo(underlying_price, strike_price, time_to_expiration, 
         volatility, risk_free_rate, dividend_yield))

    return NdTwo

def call_option(underlying_price, strike_price, time_to_expiration, 
                volatility, risk_free_rate, dividend_yield):

    a = (underlying_price * math.exp(-dividend_yield * time_to_expiration) 
        * NdOne(underlying_price, strike_price, time_to_expiration, volatility, risk_free_rate, dividend_yield))
    b = (strike_price * math.exp(-risk_free_rate * time_to_expiration)
        * NdTwo(underlying_price, strike_price, time_to_expiration, volatility, risk_free_rate, dividend_yield))

    call_option = a - b

    return call_option

def put_option(underlying_price, strike_price, time_to_expiration, 
               volatility, risk_free_rate, dividend_yield):

    a = (strike_price * math.exp(-risk_free_rate * time_to_expiration)
        * norm.cdf(-dTwo(underlying_price, strike_price, time_to_expiration, 
         volatility, risk_free_rate, dividend_yield)))

    b = (underlying_price * math.exp(-dividend_yield * time_to_expiration)
        * norm.cdf(-dOne(underlying_price, strike_price, time_to_expiration, 
         volatility, risk_free_rate, dividend_yield)))

    put_option = a - b

    return put_option