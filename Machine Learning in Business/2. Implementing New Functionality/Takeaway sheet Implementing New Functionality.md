# Takeaway sheet: Implementing New Functionality

## Practice

```python
# Finding confidence interval for the mean
# alpha — level of significance;
# df — number of degrees of freedom, = n - 1;
# loc — mean distribution, equals to mean estimate. 
# sample = sample.mean();
# scale — distribution standard error, equals to standard error estimate. 
# Calculation: sample.sem()

from scipy import stats as st

confidence_interval = st.t.interval(alpha = alpha, df=df, 
																		loc=sample.mean(), scale=sample.sem())
```

```python
# Extracting subsample for bootstrap

from numpy.random import RandomState
state = RandomState(12345)

# without replacement
print(example_data.sample(frac=1, replace=False, random_state=state))
# with replacement
print(example_data.sample(frac=1, replace=True, random_state=state))
```

```python
# A/B test analysis using bootstrap

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

## Theory

**A/B testing** or **Split testing** is a technique for hypothesis testing that helps to monitor the impact of service or product changes on the users. The technique implies the following: the population is split into control group that uses the regular service with no changes and treatment group that uses the new version, the one we need to test.

**Peeking problem**: the overall result is distorted when new data is added at the beginning of the experiment.

**Type I error** — when the null hypothesis is correct but it is rejected (*false positive* result; new functionality is approved hence *positive*)

**Type II error** — when the null hypothesis is wrong but it is accepted (*false negative* result)

A **confidence interval** is a segment of the number axis, which the population parameter of interest falls into with a predetermined probability.