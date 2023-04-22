# lunch_is_not_free
some odds and ends work

# Black-Scholes Pricing Formulas

Price of a non-dividend paying European call option:  
$c = S_0N(d_1) - Ke^{-rT}N(d_2)$  

Price of a non-dividend paying European put option:  
$p = Ke^{-rT}N(-d_2) - S_0N(-d_1)$

where:  
$S_0$ is the stock price at time zero, $t_0$  
K is the strike price  
r is the continously compounded risk-free rate  
$\sigma$ is the stock price volatility  
T is the time to maturity  
...add dividends too...

$d1 = \frac{ln(S_0/K)+(r+\sigma^2/2)T}{\sigma\sqrt{T}}$

$d2 = \frac{ln(S_0/K)+(r-\sigma^2/2)T}{\sigma\sqrt{T}} = d_1-\sigma\sqrt{T}$

$N(d_2)$ is the probability that the call option will be exercised in a risk-neutral world  
$KN(d_2)$ is the strike price times the probability that it will be paid