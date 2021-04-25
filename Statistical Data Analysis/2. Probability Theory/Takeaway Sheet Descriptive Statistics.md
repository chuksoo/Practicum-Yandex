# Takeaway Sheet: Descriptive Statistics

## Practice

```
# declaring a table in a numpy array

table = np.array([[2,3,4,5,6,7], 
[3,4,5,6,7,8], 
...
[7,8,9,10,11,12]])

# acquiring a list of dictionary keys and values

dictionary.keys() # list of keys
dictionary.values() # list of values

# calculating factorial numbers

from math import factorial
x = factorial(5)

# finding normal distribution from expected value and standard deviation

from scipy import stats as st

distr = st.norm(1000, 100) 

result = distr.cdf(x) # probability of getting the value x 

result = distr.cdf(x2) - distr.cdf(x1) # probability of getting a value between x1 and x2

result = distr.ppf(p1) # value by probability
```

## Theory

An **experiment** is a repeatable test that can have various outcomes.

**Elementary outcomes** are experiment outcomes that cannot be broken down into smaller outcomes.

**Equally probable outcomes** are outcomes whose probability of occurring is equal.

The **sample space** is the set of all elementary outcomes from the experiment.

An **event** is a subset of the sample space containing a number of elementary outcomes.

An **impossible event** is an event that can never happen, so the probability of it occurring is 0.

A **certain event** is an event that will definitely happen, so its probability is equal to 1.

The **law of large numbers** says that the more times you repeat an experiment, the closer the frequency of a given event will be to its probability.

**Mutually exclusive events** are events that cannot occur simultaneously in the same experiment.

**Independent events** are events where the occurrence of one does not affect the probability of the other. If events are independent, the probability of their intersection is the same as the product of their probabilities of occurring.

**Random variables** are variables that take a **random value** that cannot be predicted before the experiment is carried out.

The **probability distribution** of **random variables** is a table that contains all of the random variable's possible values and the probability of their occurrence.

The **expected value** of a **random variable** is a numerical value which the random variable will tend toward over multiple repetitions of the experiment, calculated as the sum of all values of the random variable multiplied by their probability:

*E*(*X*) = ∑*p*(*xi*)*xi*

**Variance of random variables** is a measure of the dispersion of random variable values, which can be found using the formula:

*Var*(*X*) = *E*(*X^*2) − (*E*(*X*))^2

**Binomial experiments** are experiments with two possible outcomes, which are usually called **success** and **failure**.

A **factorial (n!)** is the product of all natural numbers from 1 to *n* inclusive.

**Central limit theorem (CLT):** Many independent random variables, added together, give a normal distribution.