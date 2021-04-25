# Chapter Summary: Descriptive Statistics

# 

## Continuous and Discrete Variables

**Categorical (qualitative)** variables take their values from a limited set. If they are assigned numerical valuables, this is purely symbolic and only for ease of processing (e.g. red = 1, blue = 2).

**Quantitative (numerical)** variables take numerical values. They come in two forms:

- **Continuous variables,** which can take any value (to any degree of precision) within some range (e.g. any value between 0 and 1)
- **Discrete variables**, which are not continuous on any range (e.g. a variable that takes integer values between 0 and 100)

## Frequency Histograms

Histograms work well for **discrete** variables. To display the frequency of continuous variables, we need something else.

One way to visualize the distribution of continuous variables is to divide the set of possible values into intervals and count the number of values in each interval.

When plotting a histogram in pandas, you can set the number of intervals (bins) and set their boundaries explicitly:

```
data.hist(bins=[value1, value2, value3, value4, ..., valueN])
```

Always remember, though, that the success of this approach depends on how well you choose the bounds of the interval — a task that can be difficult even for experienced data analysts.

## Density Histograms

To overcome the difficulties of creating a histogram for a continuous variable, we can use a slightly different technique that represents frequency not as the height of a column, but as its area (the length of the interval times the height of the column). This area is the **frequency** of the continuous variable, and the height of the column is the **frequency density**. A histogram that uses frequency density is called a **density histogram.**

To estimate how many values fall in a particular interval, take two values and find the total area of the density histograms between them. The number you get will be an estimate of the number of values in that interval.

We can also display the frequency density for continuous variables using continuous lines. The same principle applies: the area under the curve between two values is proportional to the frequency of the values in a given interval.

## Measures of Location

We can use **measures of location,** like the median and mean, to estimate approximately *where* a dataset is located on the numerical axis.

The mean and median are more formally called the **algebraic measure of location** and the **structural measure of location**, respectively.

## Who Scattered the Data?

Measures of location aren't enough if you really want to understand the data. You also need to know how the data is **scattered** or **dispersed** around these measures. 

For medians, dispersion can be measured in terms of quartiles.

## Variance

Variance is another common measure of dispersion. It can be calculated as the average squared distance of data from the mean:

$$\sigma^{2} = \frac{\sum \left ( \mu - x_{i} \right )^{2}}{n}$$

where the Greek letter mu, *μ*, stands for the arithmetic mean of the data.

$$\mu = \frac{\sum \left (x_{i} \right )}{n}$$

The **NumPy** library in Python contains a large library of high-level mathematical functions. Here’s how you import it:

```
import numpy as np
```

Variance is calculated with the **var()** method:

```
import numpy as np
variance = np.var(x)
```

## Standard Deviation

Variance has a drawback: its units of measurement are squares of the variable's original units. To get back to the original units of measurement, we need to take the square root of the variance. The resulting value is called the **standard deviation**:

$$\sigma = \sqrt{\frac{\sum \left ( \mu - x_{i} \right )^{2}}{n}}$$

The standard deviation can be found with the `std()` method from NumPy:

```
import numpy as np
standard_deviation = np.std(x)
```

Also remember that if you already know the variance, you can use NumPy's `sqrt()` method to get the standard deviation. 

```
import numpy as np
variance = 2.9166666666666665
standard_deviation = np.sqrt(variance)
```

The rule of three standard deviations, or the **three-sigma** **rule,** holds true for the most commonly used distributions. This rule states that almost all values (approximately 99%) are found within three standard deviations of the mean:

(*μ* − 3*σ*, *μ* + 3*σ*)

This rule not only helps you find the interval where most of the values you are interested in fall, but also helps you find values outside that interval (**outliers**).

## Skewed Data

In many cases, data is distributed normally and symmetrically. But datasets can also be asymmetrical, or "skewed," in either a positive or negative direction. It’s easy to recognize skew if you look at a histogram. You can think of skew as a tail to one side of the other of the symmetrical "bulk" of the data.

![Chapter%20Summary%20Descriptive%20Statistics%20b5b427a026814b708c9b88ebc516ce19/Untitled.png](Chapter%20Summary%20Descriptive%20Statistics%20b5b427a026814b708c9b88ebc516ce19/Untitled.png)

A data distribution with additional values on the right is said to **skew to the right**. This is often called **positive skew**, because there are additional values as you move along the axis in a positive direction.

Conversely, a dataset that differs from a symmetrical one in that it has additional values on the left is said to **skew to the left**, or to have **negative skew**.

Box plots also show the skew of a distribution.

There is a way to determine the skew of a dataset without plotting graphs: just compare the mean and the median. Since the median is not affected by outliers as much as the mean, the mean is greater than the median for datasets skewed to the right, and vice versa for datasets skewed to the left.