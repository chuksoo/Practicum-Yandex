# Chapter Summary: Implementing New Functionality

## Implementation planning

**A/B testing** or **Split testing** is a technique for hypothesis testing that helps to monitor the impact of service or product changes on the users. It is performed as follows: the population is split into control group (*A*) and treatment group (*B*). Group *A* uses the regular service with no changes. Group *B* uses the new version, the one we need to test.

The experiment lasts for a fixed period of time (e.g. — two weeks). The objective is to collect visitor behavior data in both groups. If the key metric in the treatment group improves compared to the control group, then the new functionality will be implemented.

![Chapter%20Summary%20Implementing%20New%20Functionality%20c3839cb748a14f2d86655a9210e5d454/viruchka.jpg](Chapter%20Summary%20Implementing%20New%20Functionality%20c3839cb748a14f2d86655a9210e5d454/viruchka.jpg)

Before the A/B test, often the A/A test or validity check is used, where the visitors are split into two control groups that both are exposed to the same version of the service. The key metric should match between the two groups, otherwise you might want to look for an error.

## A/B test duration

Implementing new functionality inevitably changes user behaviour. Usually users need time to get used to the changes. Once they are fully accustomed, we can evaluate with certainty whether the experiment was a success. The more data we have, the lower the probability of error when testing statistical hypotheses.

A/B testing suffers from the so-called **peeking problem**: the overall result is distorted when new data is added at the beginning of the experiment. Even a small fragment of new data is large relative to the data already accumulated, and statistical significance is achieved in a short time.

This is one of the manifestations of the law of large numbers. For a small number of observations, the dispersion tends to be greater. On the other hand, when we have many observations, the impact of any outliers will be reduced. So if the sample is too small, the differences are easy to see. For a statistical test, it is a p-value decrease down to the values small enough to reject the null hypothesis of no difference. 

To address the peeking problem, sample size must be set before the start of the test.

Here's the correct procedure of *A/B* testing:

![Chapter%20Summary%20Implementing%20New%20Functionality%20c3839cb748a14f2d86655a9210e5d454/collect_X.jpg](Chapter%20Summary%20Implementing%20New%20Functionality%20c3839cb748a14f2d86655a9210e5d454/collect_X.jpg)

And that's how you should not conduct an *A/B* test:

![Chapter%20Summary%20Implementing%20New%20Functionality%20c3839cb748a14f2d86655a9210e5d454/collect_X.1.jpg](Chapter%20Summary%20Implementing%20New%20Functionality%20c3839cb748a14f2d86655a9210e5d454/collect_X.1.jpg)

The easiest way to calculate the sample size is to use an online calculator like this one: [https://vwo.com/tools/ab-test-duration-calculator/](https://vwo.com/tools/ab-test-duration-calculator/)

## Comparing the means

Let's analyze the *A/B* testing results: value of the metric describes the behavior of all users. 

Measurement results and mean values contain an element of randomness. Therefore, they have a random error component. We can not predict each observation's exact value with precise accuracy but we may estimate them using statistical methods

Suppose our null hypothesis **H₀** says: New functionality does not improve metrics. Then our corresponding hypothesis **H₁** will be: New functionality improves metrics.

At the stage of hypothesis testing, two types of errors are possible:

1. **Type I error** — when the null hypothesis is correct but it is rejected (*false positive* result; new functionality is approved hence *positive*)
2. **Type II error** — when the null hypothesis is wrong but it is accepted (*false negative* result)

![Chapter%20Summary%20Implementing%20New%20Functionality%20c3839cb748a14f2d86655a9210e5d454/vernaya_gipoteza.jpg](Chapter%20Summary%20Implementing%20New%20Functionality%20c3839cb748a14f2d86655a9210e5d454/vernaya_gipoteza.jpg)

To accept or reject the null hypothesis, let's calculate the significance level, also known as the **p-value** (probability value). It shows the probability of type I error but doesn't tell anything about the type II error.

Note that if p-value is greater than the **threshold value**, then the null hypothesis should not be rejected. If it is less than the threshold, the the null hypothesis may be not worth accepting. The generally accepted thresholds are 5% and 1%. But only the data scientist makes the final decision on which threshold should be considered sufficient.

The mean values are compared using the methods for testing one-sided hypotheses. The one-sided hypothesis is accepted if the value being tested is either much greater or much less than the one in the null hypothesis. We are interested in deviation in only one direction — greater than.

If the data distribution is close to normal (no significant outliers in the data), the standard *t*-test is used to compare the means. This method assumes a normal distribution of means from all samples and determines whether the difference among the compared values is great enough to reject the null hypothesis.

## Confidence interval

A **confidence interval** is a segment of the number axis, which the population parameter of interest falls into with a predetermined probability. The parameter is unknown, but it can be estimated from the sample. If the value falls into the range from 300 to 500 with 99% probability, then the 99-percent confidence interval for this value is **(300, 500)**.

When calculating the confidence interval, we usually drop the same portion of extreme values from each of its ends.

The confidence interval is not just a range of random values. The value that we estimate is not random by design. The probability arises from the fact that the number is unknown and is estimated from the sample. Randomness of the sample introduces randomness into the estimate. The confidence interval measures the confidence of such estimate.

![Chapter%20Summary%20Implementing%20New%20Functionality%20c3839cb748a14f2d86655a9210e5d454/99.jpg](Chapter%20Summary%20Implementing%20New%20Functionality%20c3839cb748a14f2d86655a9210e5d454/99.jpg)

## Calculating the confidence interval

We can build a confidence interval for the mean based on the sample using the central limit theorem.

Suppose we take our sample from a distribution with the following parameters:

$$\mu = \text{population mean}$$

$$\sigma^2 = \text{population variance}$$

Denote the sample mean:

$$\bar{X} = \text{sample mean}$$

The central limit theorem says that all means of all possible samples of size *n* are normally distributed around the true mean of the population. "Around" means that the mean of this distribution of all sample means will be equal to the true mean of the population. Variance will be equal to the population variance divided by *n* (the sample size).

$$\bar{X} \sim \mathbf{N}\left(\mu, \frac{\sigma^{2}}{n}\right)$$

The standard deviation of this distribution is called the **standard error** (*standard error of mean*, or *SEM*):

$$\mathrm{SEM}(\bar X) = \frac{\sigma}{\sqrt{n}}$$

The larger the sample size, the smaller the standard error — i.e., the closer all sample means "squeeze up" against the true mean. The larger our sample, the more accurate the estimate.

Let's standardize this normal distribution:

$$\frac{\bar{X} - \mu}{\mathrm{SEM}(\bar X)} \sim \mathbf{N}(0, 1^{2})$$

From the standard normal distribution, take the 5% percentile *F*(0.05) and the 95% percentile *F*(0.95) to obtain the 90% confidence interval:

$$P\left(F(0.05) < \frac{\bar{X} - \mu}{\mathrm{SEM}(\bar X)} < F(0.95)\right) = 90\%$$

Reexpress:

$$P\left(\bar{X} - F(0.05) \cdot \mathrm{SEM}(\bar X) < \mu < \bar{X} + F(0.95) \cdot \mathrm{SEM}(\bar X)\right) = 90\%$$

This is it! 90% confidence interval for the true mean.

Only one problem remains: to calculate the standard error, we use the population variance, which is unknown to us just like the population mean. We estimate it from the sample.

It affects the distribution of sample means as well: if the variance is unknown, we can't use normal distribution and have to describe it with the Student distribution. By putting the 5% percentile *t*(0.05) and the 95% percentile *t*(0.95) into the formula, we obtain:

$$P\left(\bar{X} - t(0.05) \cdot \mathrm{SEM}(\bar X) < \mu < \bar{X} + t(0.95) \cdot \mathrm{SEM}(\bar X)\right) = 90\%$$

The calculation can be simplified by using the Student distribution *scipy.stats.t*. It has a function for the confidence interval, *interval().* It takes:

- *alpha* — level of significance
- *df* — number of degrees of freedom (equal to n - 1)
- loc (from *location*) — average distribution equal to the mean estimate. For the *sample*, it is calculated as follows: `sample.mean()`
- *scale* — standard error of distribution equal to the standard error estimate. It is calculated as follows: `sample.sem()`.

```python
import pandas as pd
from scipy import stats as st

confidence_interval = st.t.interval(alpha, len(sample)-1, 
																		loc=sample.mean(), scale=sample.sem())
```

## Bootstrap

Complex values can be calculated with the help of the **Bootstrap** technique.

To obtain the desired value, like the mean for example, we can obtain the subsamples (pseudo-samples) from the source set of data. Then we calculate the mean from each of them. Theoretically, we can form subsamples and calculate the desired value from them many times. This way, we can obtain several values for the parameter of interest and estimate the distribution.

![Chapter%20Summary%20Implementing%20New%20Functionality%20c3839cb748a14f2d86655a9210e5d454/raspredelenie.jpg](Chapter%20Summary%20Implementing%20New%20Functionality%20c3839cb748a14f2d86655a9210e5d454/raspredelenie.jpg)

Bootstrap is applicable to any samples. It is useful when:

- Observations are not described by normal distribution;
- There are no statistical tests for the target value.

In fact, you can't always rely on the normal distribution.

## Bootstrap for confidence interval

Let's find out how to form subsamples for *bootstrap*. You're already familiar with the *sample()* function. For this task we need to call it in a loop. But here we hit a problem:

```python
for i in range(5):
    # extract one random element from sample 1
    # specify random_state for reproducibility
    print(data.sample(1, random_state=54321))

```

Since we specify the `random_state`, the random element is always the same. To address that, create a `RandomState()` instance from the  `numpy.random` module:

```python
from numpy.random import RandomState
state = RandomState(54321)

```

This instance can be passed to the `random_state` argument of any function. It is important that with each new call, its state will change to random. So we get different subsamples:

```python
for i in range(5):
    # extract one random element from sample 1
    print(data.sample(1, random_state=state))

```

Another important detail when creating subsamples is that they should provide a selection of elements with replacement. That is, the same element can fall into a subsample several times. To do this, specify `replace=True` for the `sample()` function. Compare:

```python
example_data = pd.Series([1, 2, 3, 4, 5])
print("Without replacement")
print(example_data.sample(frac=1, replace=False, random_state=state))
print("With replacement")
print(example_data.sample(frac=1, replace=True, random_state=state))

```

## Bootstrap for A/B test analysis

Bootstrap is also used to analyze the results of *A/B* testing. 

While the test was being conducted, we accumulated data on the target parameter in the control group and in the treatment group. We calculate the *actual difference of target parameters* between the groups. Then form and test the hypotheses. The null hypothesis is that there is no difference between the target parameters of both groups. The alternative hypothesis is that in the treatment group, the target parameter value is larger. Let's find the *p-value.*

Now, let's find the probability that such a difference was obtained by accident (this will be our *p-value*). Concatenate the samples and use bootstrap to obtain the distribution of the average purchase amount.

Create many subsamples and divide each subsample in two with the index *i*:

![Chapter%20Summary%20Implementing%20New%20Functionality%20c3839cb748a14f2d86655a9210e5d454/ai.jpg](Chapter%20Summary%20Implementing%20New%20Functionality%20c3839cb748a14f2d86655a9210e5d454/ai.jpg)

![Chapter%20Summary%20Implementing%20New%20Functionality%20c3839cb748a14f2d86655a9210e5d454/bi.jpg](Chapter%20Summary%20Implementing%20New%20Functionality%20c3839cb748a14f2d86655a9210e5d454/bi.jpg)

Find the difference of average purchase amount between them:

In bootstrap, let's assess the share of average purchase amount differences that turned out to be no less that the average purchase amount differences between the original samples:

![https://pictures.s3.yandex.net/resources/p_value_1575157722.jpg](https://pictures.s3.yandex.net/resources/p_value_1575157722.jpg)

```python
import pandas as pd
import numpy as np

# actual difference between the means in the groups
AB_difference = samples_B.mean() - samples_A.mean()

alpha = 0.05
    
state = np.random.RandomState(54321)

bootstrap_samples = 1000
count = 0
for i in range(bootstrap_samples):
    # calculate how many times the difference between the means will exceed 
    # the actual value, provided that the null hypothesis is true
    united_samples = pd.concat([samples_A, samples_B])
    subsample = united_samples.sample(frac=1, replace=True, random_state=state)
    
    subsample_A = subsample[:len(samples_A)]
    subsample_B = subsample[len(samples_A):]
    bootstrap_difference = subsample_B.mean() - subsample_A.mean()
    
    if bootstrap_difference >= AB_difference:
        count += 1

pvalue = 1. * count / bootstrap_samples
print('p-value =', pvalue)

if pvalue < alpha:
    print("Reject null hypothesis: average purchase amount is likely to increase")
else:
    print("Failed to reject null hypothesis: average purchase amount is unlikely to increase")
```

## Bootstrap for models

Bootstrap can be used to assess confidence intervals in ML models.