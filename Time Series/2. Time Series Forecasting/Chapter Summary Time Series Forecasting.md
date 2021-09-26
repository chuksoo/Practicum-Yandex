# Chapter Summary: Time Series Forecasting

## Time Series Forecasting

The point of **time series forecasting** is developing a model which predicts the future values of a time series based on previous data. The length of time into the future for which the forecast is prepared is called a **forecast horizon**. We will use a one-step horizon for the tasks in this chapter. 

If the values of either a time series or the function `x(t)` (where t = time) are numbers, then you're facing a regression task for the time series. If they are categories, it will be a classification task.

Using the initial data, we will create a training set and a test set. You can't mix the sets in time series forecasting, and the training set data must precede the test set data. Otherwise, model testing will be flawed: the model shouldn't be trained on future data after all. The `train_test_split()` function from the `sklearn.model_selection` module mixes data by default, so let's set the **`shuffle`** argument to `False` so the data can be separated correctly into training and test sets:

```python
import pandas as pd
from sklearn.model_selection import train_test_split

train, test = train_test_split(data, shuffle=False, test_size=0.2)
```

## Forecast Accuracy

We'll be using the *MAE* metric to evaluate the models in our tasks because this metric is easily interpretable.

There are two ways to forecast time series without training:

1. All values of the test sample are predicted with the same number (a constant). For the *MAE* metric, this number is the median.
2. The new value *x(t)* is predicted by the previous value in the series, defined as *x(t-1)*. This method is metric-independent.

## Creating Features

**1. Calendar features**

Usually trends and seasonality are linked to a specific date. The `datetime64` type in pandas already contains the necessary information, and all that remains is to present it as separate columns. Let's consider this example:

```python
# this feature contains years as numeric values
data['year'] = data.index.year

# this feature contains weekdays as numeric values
data['dayofweek'] = data.index.dayofweek
```

**2. Lag features**

The previous values in the time series will tell you whether the function `x(t)` will grow or decrease. Let's get the lag values using the `shift()` **function:

```python
data['lag_1'] = data['target'].shift(1)
data['lag_2'] = data['target'].shift(2)
data['lag_3'] = data['target'].shift(3)
```

Not all lag values are available for the first dates, so these lines contain `NaN`.

**3. Rolling mean**

The rolling mean feature sets the general trend of the time series. Here's a reminder of how to calculate it:

```python
data['rolling_mean'] = data['target'].rolling(5).mean()
```

The rolling mean at *t* takes into account the current value of the *x(t)* series. This is incorrect: target "slipped" into the features. The rolling mean calculation should not include the current value of the series.