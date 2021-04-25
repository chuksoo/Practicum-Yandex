# Takeaway Sheet: Testing Hypotheses

## Practice

```python
# testing a hypothesis about population mean equaling a given value
# array is the sample
# interested_value is the proposed mean for the test

from scipy import stats as st

results = st.ttest_1samp(
    array, 
    interested_value)

print('p-value: ', results.pvalue)

# Testing a hypothesis about the means of two statistical populations based on samples taken from them
# sample_1 is the sample from the first statistical population
# sample_2 is the sample from the second statistical population
# equal_var defines whether or not the variances of the samples are considered equal; default value is True

from scipy import stats as st

sample_1 = [...]
sample_2 = [...]

results = st.ttest_ind(
    sample_1, 
    sample_2,
        equal_var = True)

print('p-value: ', results.pvalue)

# Testing a hypothesis about the means of two statistical populations being equal for dependent (paired) samples
# pair_1 is the first paired sample
# pair_2 is the second paired sample

from scipy import stats as st

results = st.ttest_rel(
    before, 
    after)

print('p-value: ', results.pvalue)
```

## Theory

**Statistical population** is a large set of data for statistical studies.

A **sample** is a selected portion of the statistical population.

A **representative sample** is a portion of the data that represents the entire statistical population.

A **random sample** is a portion of the statistical population selected randomly.

**Strata** are groups in a statistical population that are united by a common feature.

A **stratified sample** is a sample made up of proportional samples from different strata.

The **sample mean** is the mean of a sample.

The **sample variance** is the variance of a sample.

The **estimated standard error** is the standard deviation of the sample mean from the real mean of the statistical population (**S** is the estimated standard deviation of the statistical population; **n** is sample size):

$$E.S.E. = \frac{S}{\sqrt{n}}$$

The **null hypothesis** (**H₀)** is a hypothesis that is tested with the sample.

The **alternative hypothesis** (**H₁)** is the hypothesis opposite in meaning to the null hypothesis.

The **statistical significance** is the total probability that an empirically measured value will be distant from the mean.

The **difference statistic** is the number of standard deviations between compared values, if both distributions are converted to a standard normal distribution with mean 0 and standard deviation 1.

The **p-value** is the probability of getting a result at least as extreme as the one you're considering, assuming that the null hypothesis is correct.

A **paired sample** is a sample used to measure some variable for the same units.