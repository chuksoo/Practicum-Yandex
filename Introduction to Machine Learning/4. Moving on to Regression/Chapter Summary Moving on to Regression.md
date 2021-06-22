# Chapter Summary: Moving on to Regression

# Mean square error

The most commonly used evaluation metric for regression tasks is the **Mean Squared Error or MSE.**

To find *MSE*, calculate the error of each observation first:

![Chapter%20Summary%20Moving%20on%20to%20Regression%2065b79a2a2c034b0bb6a35da525c5940f/otklonenie.jpg](Chapter%20Summary%20Moving%20on%20to%20Regression%2065b79a2a2c034b0bb6a35da525c5940f/otklonenie.jpg)

Calculate *MSE* using the following formula: 

![Chapter%20Summary%20Moving%20on%20to%20Regression%2065b79a2a2c034b0bb6a35da525c5940f/mse.jpg](Chapter%20Summary%20Moving%20on%20to%20Regression%2065b79a2a2c034b0bb6a35da525c5940f/mse.jpg)

Let's analyze these calculations:

1. The observation error shows the extent of the discrepancy between the correct answer and the prediction. If the error is much greater than zero, the model has overpriced the apartment; if the error is much less than zero, then the model underpriced it.

2. It would be pointless to add up the errors as they are, since positive errors would cancel out negative ones. To make them all count, we need to get rid of the signs by squaring each of them.

3. We find the mean to obtain data for all the observations.

*MSE* should be as low as possible.

# MSE calculation

To calculate mean squared error, import the `mean_squared_error()` function from `sklearn.metrics` **module*:*

```python
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(answers, predictions)
```

As a result, you'll get square units (for example, "square dollars"). To get an evaluation metric in the regular units, find the square root of *MSE*. Then, you will get *RMSE* (*root mean squared error*):

```python
rmse = mse ** 0.5
```

# Decision tree regression

For regression tasks, decision trees are trained in a manner similar to classification, but they predict a number, not a class.

The decision tree for regression tasks is called `DecisionTreeRegressor` and is located in the `sklearn.tree` **module.

```python
from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor(random_state=54321)
```

# Linear regression

**Linear regression** is similar to logistic regression in several ways. The name comes from linear algebra. Linear regression is less susceptible to overfitting because it doesn't have many parameters. 

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
```