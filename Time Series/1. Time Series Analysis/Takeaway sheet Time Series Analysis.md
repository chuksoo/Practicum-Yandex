# Takeaway sheet: Time Series Analysis

Practice

```python
# date recognition and formation of new indices
# values of index_col = the list of column numbers or column names
# values of parse_dates = the list of column numbers or column names
data = pd.read_csv('filename.csv', index_col=[0], parse_dates=[0])
```

```python
# checking that the index is monotonic
print(data.index.is_monotonic)
```

```python
# resampling - mean for each hour
data.resample('1H').mean()

# resampling - maximum for each two weeks
data.resample('2W').max()
```

```python
# rolling mean with window size = 7
data.rolling(7).mean()
```

```python
# decomposing the time series into trend, seasonality, and residuals
from statsmodels.tsa.seasonal import seasonal_decompose

decomposed = seasonal_decompose(data)

decomposed.trend # trend
decomposed.seasonal # seasonality
decomposed.resid # residuals
```

```python
# one step shift with filling the zero value
print(data.shift(fill_value=0))
```

Theory

**Time series** are the sequences of numbers along the time axis. The interval between the values of the series is constant.

**Resampling** means changing the interval with the values of the series. It is performed in two steps:

1. Choose the new interval length. Note that the values from the existing interval are grouped.  
2. In each group, the aggregated value of the series is calculated. It can be median, mean, maximum or minimum. 

**Rolling mean** or **moving average** is a method of smoothing the data in a time series. The method involves finding the values least susceptible to fluctuations, that is, the arithmetic mean.

A **trend** is a smooth change of the mean value of the series without repeating patterns.

**Seasonality** means cyclically repeating patterns in a time series.

S**tochastic process** has random variation, and its distribution changes over time.

A stochastic process is **stationary** if its distribution does not change over time. If the distribution does change, then the *stochastic* process is **nonstationary.**

**Time series differences** are a set of differences between neighboring elements of a time series — i.e., the previous value is subtracted from each value.