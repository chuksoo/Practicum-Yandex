# Chapter Summary: Regression Metrics

## Coefficient of Determination

The **coefficient of determination** or the **R2** metric (*R-squared*) divides the Model *MSE* by the Mean *MSE* and then subtracts the obtained value from one. If the metric increases, the model’s quality also improves.

*R2* is calculated as follows:

![Chapter%20Summary%20Regression%20Metrics%203f143a4890ce45cda3219159acbe931b/R2.jpg](Chapter%20Summary%20Regression%20Metrics%203f143a4890ce45cda3219159acbe931b/R2.jpg)

- *R2* equals one only if the *MSE* value is zero. Such model would perfectly predict all the answers.
- *R2* is zero: the model works as well as the mean.
- When *R2* is negative, the model quality is very low.
- *R2* can't have values greater than one.

To calculate this metric, you can use the *r2_score()* function from the *sklearn.metrics* library:

```python
from sklearn.metrics import r2_score

print("R2 =", r2_score(target, predicted))
```

## Mean Absolute Error

We need to state the conventional notation for *Data Science*:

![Chapter%20Summary%20Regression%20Metrics%203f143a4890ce45cda3219159acbe931b/y1.jpg](Chapter%20Summary%20Regression%20Metrics%203f143a4890ce45cda3219159acbe931b/y1.jpg)

- The target value for the observation with serial number ***i*** in the sample used to measure the quality. The subscript indicates the serial number of the observation.

![Chapter%20Summary%20Regression%20Metrics%203f143a4890ce45cda3219159acbe931b/yi_(1).jpg](Chapter%20Summary%20Regression%20Metrics%203f143a4890ce45cda3219159acbe931b/yi_(1).jpg)

- The prediction value for the observation with serial number ***i*** (in the test sample, for instance).

**MAE** (*mean absolute error*) is another evaluation metric. It is somewhat similar to *MSE*, but it isn’t squared. Let's write it down using the conventional notations for Data Science. 

An observation's error is written as follows:

![Chapter%20Summary%20Regression%20Metrics%203f143a4890ce45cda3219159acbe931b.jpg](Chapter%20Summary%20Regression%20Metrics%203f143a4890ce45cda3219159acbe931b.jpg)

To cancel out the difference between underfitting and overfitting, **absolute error** is calculated:

![Chapter%20Summary%20Regression%20Metrics%203f143a4890ce45cda3219159acbe931b/_.jpg](Chapter%20Summary%20Regression%20Metrics%203f143a4890ce45cda3219159acbe931b/_.jpg)

To collect the errors throughout the sample, let's add the following notation:

![Chapter%20Summary%20Regression%20Metrics%203f143a4890ce45cda3219159acbe931b/N_(1).jpg](Chapter%20Summary%20Regression%20Metrics%203f143a4890ce45cda3219159acbe931b/N_(1).jpg)

- The number of observations in the sample.

![Chapter%20Summary%20Regression%20Metrics%203f143a4890ce45cda3219159acbe931b/I.jpg](Chapter%20Summary%20Regression%20Metrics%203f143a4890ce45cda3219159acbe931b/I.jpg)

- Summation over all observations of the sample (***i*** varies in the range from 1 to *N*).

The formula for **MAE or Mean Absolute Error is:**

![Chapter%20Summary%20Regression%20Metrics%203f143a4890ce45cda3219159acbe931b/MAE.jpg](Chapter%20Summary%20Regression%20Metrics%203f143a4890ce45cda3219159acbe931b/MAE.jpg)

To calculate this metric, you can use the *mean_absolute_error()* function from the *sklearn.metrics* library:

```python
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(target, predicted))
```

To calculate the *MSE* value*,* we used the mean value as a constant. 

The constant model should be picked in the manner that allows you to obtain the lowest possible *MAE* metric value. We need to find the value ***a***, at which the minimum is reached:

![Chapter%20Summary%20Regression%20Metrics%203f143a4890ce45cda3219159acbe931b/MAE2.jpg](Chapter%20Summary%20Regression%20Metrics%203f143a4890ce45cda3219159acbe931b/MAE2.jpg)

The minimum is reached when ***a*** is equal to the target median.

Unlike *MAE*, the *RMSE* metric is more **sensitive to large values**: significant errors strongly affect the final *RMSE* value. That way you can change the value of one metric without changing another.