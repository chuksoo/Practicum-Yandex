# Takeaway sheet: Regression Metrics

## Practice

```python
# To calculate R2 metric 

from sklearn.metrics import r2_score

print("R2 =", r2_score(target, predicted))
```

```python
# To calculate MAE metric 

from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(target, predicted))
```

## Theory

The **coefficient of determination** or the **R2** metric (*R-squared*) divides the Model *MSE* by the Mean *MSE* and then subtracts the obtained value from one.

The formula is: 

![Takeaway%20sheet%20Regression%20Metrics%209634cd3cf31b4469946aa027968befff/R2.jpg](Takeaway%20sheet%20Regression%20Metrics%209634cd3cf31b4469946aa027968befff/R2.jpg)

**Mean Absolute Error (MAE)** is ****regression evaluation metrics to calculate it use:  

$$MAE = \frac{1}{N} \sum_{i=1}^N |y_i - \hat y_i|$$

## The conventional notations for Data Science

$y_i$ is the target value for the observation with serial number ***i*** in the sample 

$\hat y_i$ is the prediction value for the observation with serial number ***i***  

$y_i - \hat y_i$ is the observation error

$|y_i - \hat y_i|$ is the observation absolute error

$N$ is the number of observations in the sample

$\sum_{i=1}^N$ is summation over all observations of the sample (***i*** varies in the range from 1 to *N*).