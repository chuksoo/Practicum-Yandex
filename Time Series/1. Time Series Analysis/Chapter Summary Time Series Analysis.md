# Chapter Summary: Time Series Analysis

## **Time series**

**Time series** are the sequences of numbers along the time axis. The interval between the values of the series is constant.

in pandas, proper working with date and time requires changing the data type in the column from `object` to `datetime64`. It can be done when reading, using the `parse_dates` argument. Also we have to set the dataframe index by specifying the desired columns in the `index_col` argument:

```python
# values of parse_dates = list of column numbers or column names
data = pd.read_csv('filename.csv', index_col=[0], parse_dates=[0])
```

To check if the dates and times are in chronological order, look at the **`is_monotonic`** attribute of the table index. If the order is chronological, the attribute will return `True`; if not, `False`.

```python
print(data.index.is_monotonic)
```

We can specify date and time as index and select the data by date:

```python
data = data['2016':'2017'] 
data = data['2016-01':'2016-06'] 
data = data['2016-01-01':'2016-01-10'] 
```

## Resampling

**Resampling** means changing the interval with the values of the series. It is performed in two steps:

1. Choose the new interval length. Note that the values from the existing interval are grouped.  
2. In each group, the aggregated value of the series is calculated. It can be median, mean, maximum or minimum. 

![Chapter%20Summary%20Time%20Series%20Analysis%2050e65eed1011414d98a66b2bdd357782/resample.jpg](Chapter%20Summary%20Time%20Series%20Analysis%2050e65eed1011414d98a66b2bdd357782/resample.jpg)

To change the interval and group the values, call the `resample()` function. Specify the new interval in the argument. Here's an example:

```python
# 1H = one hour
data.resample('1H') 

# 2W = two weeks
data.resample('2W')
```

The `resample()` function is similar to the `groupby()` function. After grouping, call functions `mean()` and `max()` to aggregate the values:

```python
# mean for each hour
data.resample('1H').mean()

# maximum for each two weeks
data.resample('2W').max()
```

## Rolling Mean

**Rolling mean** or **moving average** is a method of smoothing the data in a time series. The method involves finding the values least susceptible to fluctuations, that is, the arithmetic mean.

Here's how the method works: The interval for averaging (**window size**) is selected experimentally. The larger the interval, the stronger the smoothing. Then the window starts to "roll" almost from the beginning to the end of the time series. The mean value is calculated at each point.

In the moving average, the windows overlap and cannot go beyond the series. So the number of obtained means will be slightly less than the number of the initial values of the series.

![Chapter%20Summary%20Time%20Series%20Analysis%2050e65eed1011414d98a66b2bdd357782/Untitled.png](Chapter%20Summary%20Time%20Series%20Analysis%2050e65eed1011414d98a66b2bdd357782/Untitled.png)

In pandas, the rolling mean is calculated in two steps:

1. Call the `rolling()` function to create a rolling window. Specify the window size in the argument:

```python
# window size 7
data.rolling(7)

```

2. Call the `mean()` function to aggregate the values:

```python
# rolling mean with window size 7
data.rolling(7).mean()

```

## Trends and Seasonality

A **trend** is a smooth change of the mean value of the series without repeating patterns. For example, annual increase in sales of airline tickets.

**Seasonality** means cyclically repeating patterns in a time series. For instance, the growth of airline tickets sales each summer.

Trends and seasonality depend on the scale of the data. You cannot see the patterns repeating every summer if there is data only for one year.

Look at the `rolling_mean` **graph. The increase in electricity consumption in the winter and in the summer is a trend.

![Chapter%20Summary%20Time%20Series%20Analysis%2050e65eed1011414d98a66b2bdd357782/Untitled%201.png](Chapter%20Summary%20Time%20Series%20Analysis%2050e65eed1011414d98a66b2bdd357782/Untitled%201.png)

If these data is analyzed on the scale of several years, the increase in the winter and in the summer are seasonal changes.

The **tsa.seasonal** (tsa stands for time series analysis) module of the **statsmodels** library contains function **`seasonal_decompose()`.** This function breaks the series into three components: trend, seasonality, and residuals. The residuals component cannot be explained by trend and seasonality and is essentially noise.

```python
from statsmodels.tsa.seasonal import seasonal_decompose

decomposed = seasonal_decompose(data)
```

`seasonal_decompose()` takes a time series and returns an instance of the `**DecomposeResult**` class. It contains the required attributes:

- `decomposed.trend` — trend;
- `decomposed.seasonal` — seasonal component;
- `decomposed.resid` — residuals.

## Stationary Series

In statistics, the time series is described as a **stochastic process**. It has random variation, and its distribution changes over time. It has a mean and variance, and these values change, too.

A stochastic process is **stationary** if its distribution does not change over time. An example of stationary stochastic process is periodic fluctuations of values.

![Chapter%20Summary%20Time%20Series%20Analysis%2050e65eed1011414d98a66b2bdd357782/stationary_stochastic_process.jpg](Chapter%20Summary%20Time%20Series%20Analysis%2050e65eed1011414d98a66b2bdd357782/stationary_stochastic_process.jpg)

If the distribution does change, then the *stochastic* process is **nonstationary.**

We can't find out the distribution of a time series. So the stationary time series is a series where the mean and standard deviation do not change. Out of the two series, the one where the mean and standard deviation change more slowly, is "more stationary".

**Nonstationary time series** are harder to forecast because their properties change too quickly.

## Time Series Differences

**Time series differences** are a set of differences between neighboring elements of a time series — i.e., the previous value is subtracted from each value.

The **`shift()`** method is used to find the differences of time series. All values are shifted one step forward along the time axis:

```python
data = pd.Series([0.5, 0.7, 2.4, 3.2])
print(data)
print(data.shift())
```

```python
0    0.5
1    0.7
2    2.4
3    3.2
dtype: float64
0    NaN
1    0.5
2    0.7
3    2.4
dtype: float64
```

The last value of the series is lost because there is no place to shift it to. Zero value is `NaN`, since there's no value for it. Add an argument to fill the missing values.

```python
import pandas as pd

data = pd.Series([0.5, 0.7, 2.4, 3.2])
print(data)
print(data.shift(fill_value=0))
```

```python
0    0.5
1    0.7
2    2.4
3    3.2
dtype: float64
0    0.0
1    0.5
2    0.7
3    2.4
dtype: float64
```

Time series differences are more stationary than the series itself. For example, a nonlinear trend is converted to a linear one:

![Chapter%20Summary%20Time%20Series%20Analysis%2050e65eed1011414d98a66b2bdd357782/series.png](Chapter%20Summary%20Time%20Series%20Analysis%2050e65eed1011414d98a66b2bdd357782/series.png)