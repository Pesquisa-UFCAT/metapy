"""benchmark functions for optimization problems"""
import numpy as np
import pandas as pd
import yfinance as yf


def sphere(x, none_variable=None):
    """
    The Sphere function has d local minima except for the global one. It is continuous, convex and unimodal.

    Args:
        x (List): Design variables.
    
    Returns:
        of (Float): Objective function value.
    """

    n_dimensions = len(x)
    of = 0
    for i in range(n_dimensions):
        x_i = x[i]
        of += x_i ** 2

    return of


def rosenbrock(x, none_variable=None):
    """
    The Rosenbrock function is unimodal, and the global minimum lies in a narrow, parabolic valley.
    
    See documentation in https://wmpjrufg.github.io/METAPY/BENCH_ROSENBROCK.html

    Args:
        x (List): Design variables.

    Returns:
        of (Float): Objective function value.
    """

    n_dimensions = len(x)
    sum = 0
    for i in range(n_dimensions - 1):
        x_i = x[i]
        x_next = x[i + 1]
        new = 100 * (x_next - x_i ** 2) ** 2 + (x_i - 1) ** 2
        sum += new
    of = sum

    return of


def rastrigin(x, none_variable=None):
    """
    The Rastrigin function has several local minima. It is highly multimodal, 
    but locations of the minima are regularly distributed.

    See documentation in https://wmpjrufg.github.io/METAPY/BENCH_RASTRIGIN.html

    Args:
        x (List): Design variables.

    Returns:
        of (Float): Objective function value.
    """

    n_dimensions = len(x)
    sum = 0
    for i in range(n_dimensions):
        x_i = x[i]
        sum += (x_i ** 2 - 10 * np.cos(2 * np.pi * x_i))
    of = 10 * n_dimensions + sum

    return of


def ackley(x, none_variable=None):
    """
    The Ackley function in its two-dimensional form, it is characterized 
    by a nearly flat outer region, and a large hole at the centre.

    See documentation in https://wmpjrufg.github.io/METAPY/BENCH_ACKLEY.html

    Args:
        x (List): Design variables.
    
    Returns:
        of (Float): Objective function value.
    """

    n_dimensions = len(x)
    sum1 = 0
    sum2 = 0
    a = 20
    b = 0.2
    c = 2 * np.pi
    for i in range(n_dimensions):
        x_i = x[i]
        sum1 += x_i ** 2
        sum2 += np.cos(c * x_i)
    term_1 = -a * np.exp(-b * np.sqrt(sum1 / n_dimensions))
    term_2 = -np.exp(sum2 / n_dimensions)
    of = term_1 + term_2 + a + np.exp(1)

    return of


def griewank(x, none_variable=None):
    """
    The Griewank function has many widespread local minima, 
    which are regularly distributed.

    See documentation in https://wmpjrufg.github.io/METAPY/BENCH_GRIEWANK.html

    Args:
        x (List): Design variables.
    
    Returns:
        of (Float): Objective function value.
    """

    n_dimensions = len(x)
    sum = 0
    prod = 1
    for i in range(n_dimensions):
        x_i = x[i]
        sum += (x_i ** 2) / 4000
    prod *= np.cos(x_i / np.sqrt(i+1))
    of = sum - prod + 1

    return of


def zakharov(x, none_variable=None):
    """
    The Zakharov function has no local minima except the global one.

    See documentation in https://wmpjrufg.github.io/METAPY/BENCH_ZAKHAROV.html

    Args:
        x (List): Design variables.
    
    Returns:
        of (Float): Objective function value.
    """

    n_dimensions = len(x)
    sum_1 = 0
    sum_2 = 0
    for i in range(n_dimensions):
        x_i = x[i]
        sum_1 += x_i ** 2
        sum_2 += (0.5 * i * x_i)
    of = sum_1 + sum_2**2 + sum_2**4

    return of


def easom(x, none_variable=None):
    """
    The Easom function has several local minima. It is unimodal, 
    and the global minimum has a small area relative to the search space.

    See documentation in https://wmpjrufg.github.io/METAPY/BENCH_EASOM.html

    Args:
        x (List): Design variables.
    
    Returns:
        of (Float): Objective function value.
    """

    x_1 = x[0]
    x_2 = x[1]
    fact_1 = - np.cos(x_1) * np.cos(x_2)
    fact_2 = np.exp(- (x_1 - np.pi) ** 2 - (x_2 - np.pi) ** 2)
    of = fact_1*fact_2

    return of


def michalewicz(x, none_variable=None):
    """
    The Michalewicz function has d! local minima, and it is multimodal. 
    The parameter m defines the steepness of they valleys and ridges; 
    a larger m leads to a more difficult search.

    See documentation in https://wmpjrufg.github.io/METAPY/BENCH_MICHALEWICZ.html

    Args:
        x (List): Design variables.
    
    Returns:
        of (Float): Objective function value.
    """

    n_dimensions = len(x)
    sum = 0
    m = 10
    for i in range(n_dimensions):
        x_i = x[i]
        sum += np.sin(x_i) * (np.sin((i * x_i ** 2) / np.pi)**(2 * m))
    of = -sum

    return of


def dixon_price(x, none_variable=None):

    """
    Dimensions: d

    See documentation in https://wmpjrufg.github.io/METAPY/BENCH_DIXONPRINCE.html

    Args:
        x (List): Design variables.
    
    Returns:
        of (Float): Objective function value.
    """

    x1 = x[0]
    n_dimensions = len(x)
    term1 = (x1-1)**2
    sum = 0
    for i in range(1, n_dimensions):
        x_i = x[i]
        xold = x[i-1]
        new = i * (2*x_i**2 - xold)**2
        sum = sum + new
    of = term1 + sum

    return of


def goldstein_price(x, none_variable=None):
    """
    Dimensions: 2
    
    The Goldstein-Price function has several local minima.

    See documentation in https://wmpjrufg.github.io/METAPY/BENCH_GOLDSTAINPRICE.html

    Args:
        x (List): Design variables.
    
    Returns:
        of (Float): Objective function value.
    """

    x1 = x[0]
    x2 = x[1]
    fact1A = (x1 + x2 + 1)**2
    fact1B = 19 - 14*x1 + 3*x1**2 - 14*x2 + 6*x1*x2 + 3*x2**2
    fact1 = 1 + fact1A * fact1B
    fact2A = (2*x1 - 3*x2)**2
    fact2B = 18 - 32*x1 + 12*x1**2 + 48*x2 - 36*x1*x2 + 27*x2**2
    fact2 = 30 + fact2A * fact2B
    of = fact1*fact2

    return of


def powell(x, none_variable=None):
    """
    Dimensions: d

    See documentation in https://wmpjrufg.github.io/METAPY/BENCH_POWELL.html

    Args:
        x (List): Design variables.
    
    Returns:
        of (Float): Objective function value.
    """

    n_dimensions = len(x)
    sum = 0
    for i in range(1, n_dimensions//4 + 1):
        term1 = (x[4 * i - 3] + 10 * x[4 * i - 2])**2
        term2 = 5 * (x[4 * i-1] - x[4 * i])**2
        term3 = (x[4 * i - 2] - 2 * x[4 * i - 1])**4
        term4 = 10 * (x[4 * i - 3] - x[4 * i])**4
        sum = sum + term1 + term2 + term3 + term4
    of = sum

    return of


def stocks_data(stocks, start_date, end_date):
    """
    This function downloads the stock data from Yahoo Finance.

    Args:
        stocks (List): List of stock tickers
        start_date (String): Start date of the data
        end_date (String): End date of the data

    Returns:
        df (DataFrame): DataFrame with the stock data
    """
    
    values = []
    for i, stock in enumerate(stocks):
        aux = yf.download(stock, start=start_date, end=end_date, progress=False)
        aux = aux['Adj Close']
        values.append(aux)
    df = pd.concat(values,  join='outer', axis=1)
    df.columns = stocks.copy()
    df.index.name = None
    df.dropna(inplace=True)
    
    return df


def stock_return_and_covariance(df):
    """
    This function calculates the stock returns.

    Args:
        df (DataFrame): DataFrame with the stock data.

    Returns:
        df_return (DataFrame): DataFrame with the stock returns.
    """
    
    df_return = df.pct_change()
    df_return.dropna(inplace=True)
    mu = df_return.mean()
    mu = mu.values.tolist()
    sigma = df_return.cov()
    sigma = sigma.values.tolist()  
    
    return df_return, mu, sigma


def return_variance_portifolio(x, mu, sigma):
    """
    This function calculates the annualized return and volatility of a portifolio.
    
    Args:
        x (List): List with the weights of the stocks
        mu (List): List with the stock returns
        sigma (List): List with the stock covariance
    
    Returns:
        retu (Float): Portifolio return (%)
        voll (Float): Portifolio volatility (%)
    """

    # Portifolio volatility
    varr = 0
    for i, value_i in enumerate(x):
        if value_i != 0:
            for j, value_j in enumerate(x):
                if value_j != 0:
                    varr += value_i * value_j * sigma[i][j] * 252
    voll = np.sqrt(varr)

    # Portifolio return
    retu = 0    
    for i, value in enumerate(x):
        if value != 0:
            retu += i * mu[i] * 252

    # Convert to percentage
    retu *= 100
    voll *= 100

    return retu, voll


def sharp_index(ret, vol, risk_free_asset=0):
    """
    This function calculates the Sharp index.

    Args:
        ret (Float): Portifolio return (%)
        vol (Float): Portifolio volatility (%)
        risk_free_asset (Float): Risk free asset return (%)
    
    Returns:
        sharp (Float): Sharp index
    """

    sharp = (ret - risk_free_asset) / vol

    return sharp


if __name__ == '__main__':
    stocks = ['aapl', 'tsla', 'dis', 'amd']
    start_date = '2010-07-01'
    end_date = '2023-02-11'
    df = stocks_data(stocks, start_date, end_date)
    dfnew, mu, sigma = stock_return_and_covariance(df)
    x = [0.71, 0.30, 0.00, 0.00]
    ret, vol = return_variance_portifolio(x, mu, sigma)
    sharp = sharp_index(ret, vol, risk_free_asset=0)
    print(f'Return: {ret:.2f}%')
    print(f'Volatility: {vol:.2f}%')
    print(f'Sharp Index: {sharp:.2f}')