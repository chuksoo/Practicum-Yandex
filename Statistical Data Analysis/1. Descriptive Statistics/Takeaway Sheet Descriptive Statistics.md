# Takeaway Sheet: Descriptive Statistics

## Practice

```python
# Building histograms with set interval boundaries

data.hist(bins=[value1, value2, value3, value4, ..., valueN])

# Importing a library of high-level mathematical functions

import numpy as np

# Finding dispersion

import numpy as np
np.var(x)

# Taking the square root

import numpy as np
np.sqrt(x)
```

## Theory

**Quantitative (numerical) variables** take numeric values.

**Qualitative (categorical) variables** take non-numeric values.

A **continuous variable** is a quantitative variable that can take any numeric value (to any degree of precision) in some range (e.g. any value between 0 and 1).

A **discrete variable** is any variable that is not continuous on any range (e.g. a variable that takes the integer values from 0 to 100).

**Frequency density** — a value equal to the height of a histogram column whose area reflects the relative frequency of a continuous variable.

**Density histogram** — a histogram that uses frequency density.

**Location metrics** help you estimate approximately where the data set is located on the numerical axis.

**Algebraic metric of location** — The mean, often denoted by the Greek letter mu, μ.

**Structural metric of location** — The median.

**Variance** is used to measure how "spread out" the data is from the mean. It is calculated by taking the average squared distance from the mean of all the points in the dataset:

$$\sigma^{2} = \frac{\sum \left ( \mu - x_{i} \right )^{2}}{n}$$

The **standard deviation** is the square root of the variance, and is denoted by the Greek letter sigma, σ. It is calculated with the following equation:

$$\sigma = \sqrt{\frac{\sum \left ( \mu - x_{i} \right )^{2}}{n}}$$

**Three-sigma rule:** almost all the values (99.7%) are found inside the interval:

(*μ* − 3*σ*, *μ* + 3*σ*)

**Skew** is a measure of a data set's asymmetry.

Data with **positive skew (skewed to the right)** has a mean that is greater than the median. The data will have more values greater than the mean than below it.

Data with **negative skew (skewed to the left)** has a mean that is less than the median. The data will have more values below the mean than above it.