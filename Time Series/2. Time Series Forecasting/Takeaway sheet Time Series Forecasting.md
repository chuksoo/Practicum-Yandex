# Takeaway sheet: Time Series Forecasting

Practice

```python
# splitting data into training and test sets for time series (without shuffling)
from sklearn.model_selection import train_test_split
train, test = train_test_split(data, shuffle=False, test_size=0.2)
```

```python
# creating calendar features
# this feature contains years as numeric values
data['year'] = data.index.year

# this feature contains weekdays as numeric values
data['dayofweek'] = data.index.dayofweek
```

```python
# forming lag features

data['lag_1'] = data['target'].shift(1)
data['lag_2'] = data['target'].shift(2)
data['lag_3'] = data['target'].shift(3)
```

```python
# adding the rolling mean feature

data['rolling_mean'] = data['target'].rolling(5).mean()
```

Theory

The point of **time series forecasting** is developing a model which predicts the future values of a time series based on previous data.

The length of time into the future for which the forecast is prepared is called a **forecast horizon**.