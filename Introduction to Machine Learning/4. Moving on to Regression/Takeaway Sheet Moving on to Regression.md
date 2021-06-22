# Takeaway Sheet: Moving on to Regression

# Practice

```python
# Calculating the mean of squared errors (MSE) and the square root of the mean of the squared errors (RMSE)

from sklearn.metrics import mean_squared_error 

mse = mean_squared_error(answers, predictions)
rmse = mse ** 0.5
```

```python
# Initializing the decision tree model for regression

from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor(random_state=54321)
```

```python
# Initializing the random forest model for regression

from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(random_state=54321, n_estimators=3)
```

```python
# Initializing the linear regression model

from sklearn.linear_model import LinearRegression

model = LinearRegression()
```