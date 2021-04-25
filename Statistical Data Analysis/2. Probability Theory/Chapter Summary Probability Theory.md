# Chapter Summary: Probability Theory

## Experiments, Elementary Outcomes, and Events

An **experiment** is a repeatable test in which one of multiple **outcomes** occurs. An outcome can be composed of several **elementary outcomes**, which by definition cannot be broken down further.

In the simplest situations, all elementary outcomes are equally probable. We can call such an experiment a "fair experiment." In a fair experiment with *n* elementary outcomes, the probability of each outcome is 1/*n*.

The set of all of an experiment's potential elementary outcomes is called the **sample space**. You can select a subset containing a number of elementary outcomes. This is called an **event**.

An **impossible event** is an event which can never happen, so the probability of it occurring is 0. A **certain event** is an event which will definitely happen, so its probability equals 1. The probability of other events is between 0 and 1.

As long as you maintain the condition that all elementary outcomes have equal probability, the **event probability** is the number of elementary outcomes in the event divided by the total number of outcomes (i.e., the size of the sample space). More generally (even when elementary outcomes are not equally probable), an event's probability will be the sum of the probabilities of its constituent elementary outcomes.

## The Law of Large Numbers

The **law of large numbers** says that the more times you repeat an experiment, the closer the frequency of a given event will be to its probability.

We can use this rule in reverse. If we don’t know the probability of an event, but we can repeat the experiment many times, we can estimate its probability from the frequency of the outcomes.

## Mutually Exclusive and Independent Events; Multiplying Probabilities

To illustrate the intersection between events, you can use a **Venn diagram**:

![Chapter%20Summary%20Probability%20Theory%2018ad4e7fcf56440fb4e9e2a8f93ee4ce/Untitled.png](Chapter%20Summary%20Probability%20Theory%2018ad4e7fcf56440fb4e9e2a8f93ee4ce/Untitled.png)

If events A and B intersect, this means that there are elementary outcomes that occur in both A and B.

Events that cannot occur simultaneously in the same experiment are called **mutually exclusive** — their Venn diagram shows no intersection:

![Chapter%20Summary%20Probability%20Theory%2018ad4e7fcf56440fb4e9e2a8f93ee4ce/Untitled%201.png](Chapter%20Summary%20Probability%20Theory%2018ad4e7fcf56440fb4e9e2a8f93ee4ce/Untitled%201.png)

The probability of mutually exclusive events both occurring is zero.

Events are called **independent** if the occurrence of one does not affect the probability of the other. If events are independent, then the probability of their intersection is the same as the product of their probabilities of occurrence. This rule works in reverse.

If mutually exclusive events occupy the whole sample space, the sum of their probabilities will equal 1.

You can tell if events are mutually exclusive from a Venn diagram. It's not as easy to illustrate independence; you need to check whether the product of events' probabilities equals the probability of their intersection.

## Random Numbers, Probability Distributions, and Value Intervals

A **random variable** is a variable that takes a **random value** that cannot be predicted before the experiment is carried out. Experiments have outcomes that can be described quantitatively as well as qualitatively. Did the python ever make it out of the maze, did it rain, what color did the roulette ball land on? A random number is defined numerically based on these outcomes. This is a way of projecting the experiment's outcomes, no matter how they were defined, onto the number line.

Like all quantitative variables, random variables can be either **discrete** or **continuous**.

The **probability distribution** of a random variable can be shown in a table that contains all of the variable's possible values and the probability of their occurrence.

You use the **array** data type from the NumPy library to store numerical tables:

```python
table = np.array([[2,3,4,5,6,7], 
[3,4,5,6,7,8], 
...
[7,8,9,10,11,12]])
```

If you need to get a list of all dictionary keys when working with a dictionary, use the `keys()` method. Get a list of all values using the `values()` method:

```python
dictionary = {...}
print(dictionary.keys())
print(dictionary.values())
```

## Expected Value and Variance

You can define a random variable for an experiment and find a numerical value which it will tend toward over multiple repetitions of the experiment. This value is known as the **expected value** of the random variable.

If the experiment consists of equally probable elementary outcomes that are defined numerically, the expected value will be equal to the average of the possible values.

The **expected value** of a random variable (*X*) is the sum of all values of the random variable (represented using a lowercase *x*) multiplied by their probabilities:

$$E(X) = ∑p(x_i)x_i$$

The expected value is like a measure of location, but for random variables rather than datasets. It tells you which value the random variable is distributed around, and, in accordance with the rule of large numbers, which value it will tend toward when the experiment is repeated.

Since the random variable is distributed around this "measure of location," you can determine what its variance is. To do so, you need to find the expected value of the square of the random variable. This isn't difficult given that values change, but their probability doesn’t.

Since we know the expected value of the random variable itself and its square, the **variance** can be found using the formula:

$$Var(X) = E(X²) − (E(X))²$$

## Probability of Success in Binomial Experiments

Experiments with two possible outcomes are known as **binomial experiments**. Typically, though not always, one of the outcomes is called "success" and the other "failure." If the probability of success is *p*, then the probability of failure is 1 - *p*, as the sum of the probabilities of the outcomes must equal 1.

## The Binomial Distribution

The number of ways to get *k* successes from *n* repetitions of an experiment can be found using the formula:

$$C_{n}^{k} = \frac{n!}{k!(n-k)!}$$

where ! (read as "factorial") equals the product of natural numbers from 1 to the given number: n! = 1 ⋅ 2 ⋅ 3 ⋅ 4 ⋅ … ⋅ (n-1) ⋅ n.

You can calculate the factorial using the math library and its `factorial` method:

```python
from math import factorial
x = factorial(5)
```

Let’s revisit the binomial experiment (where an experiment with two outcomes is repeated *n* times). If the probability of success is *p* and that of failure is 1 - *p*, and the experiment is repeated *n* times, then the probability of getting *k* successes given *n* attempts is:

$$C_{n}^{k} p^k(1 − p)^{n-k}$$

Here are the conditions that allow us to confirm that the random variable is binomially distributed:

- A finite, fixed number of attempts (*n*) are conducted
- Every attempt is a simple binomial experiment with exactly two outcomes
- The attempts are independent of each other
- The probability of success (*p*) is the same for all *n* attempts

## The Normal Distribution

The **central limit theorem** is a key theorem in statistics. Somewhat simplified, it states that “Many independent random variables, added together, give a normal distribution.”

The normal distribution describes real continuous values. It has two parameters, mean and variance:

*X* ∼ ℕ(*μ*, *σ*2)

This notation can be read as: The variable *X* has a normal distribution with a mean of *mu* (μ) and a variance of *sigma squared* (σ²) (corresponding to a standard deviation of *sigma*).

To find the probability of any given interval occurring from known distribution parameters, we call two methods from the scipy.stats package: **norm.ppf** and **norm.cdf.**

- `ppf`: percent point function.
- `cdf`: cumulative distribution function.

Both work with the normal distribution, given a particular mean (expected value) and standard deviation.

- `norm.ppf` gives the *value* of a variable when the probability of the interval to the left of that value is known.
- `norm.cdf`, on the other hand, gives the *probability* of the interval to the left of the value when the value is known.

Calculate the normal distribution using the `norm()` method from the scipy.stats package with two arguments: expected value and standard deviation. Let’s find the probability of getting a particular value, *x*:

```
from scipy import stats as st

# set normal distribution 
distr = st.norm(1000, 100) 

x = 1000

result = distr.cdf(x) # calculate probability of getting the value x
```

Using the `norm.cdf` function, we can calculate the probability of getting a value in the interval between *x1* and *x2***:**

```
from scipy import stats as st

# set normal distribution 
distr = st.norm(1000, 100) 

x1 = 900
x2 = 1100

result = distr.cdf(x2) - distr.cdf(x1) 
# calculate the probability of getting a value between x1 and x2
```

To find a value given a certain probability, we use the `norm.ppf` method:

```
from scipy import stats as st

# set normal distribution 
distr = st.norm(1000, 100) 

p1 = 0.841344746

result = distr.ppf(p1)
```

## Normal Approximation to the Binomial Distribution

With a large number of repetitions of a binomial experiment, the binomial distribution approaches the normal distribution.

For a discrete binomial distribution, given a number of attempts *n* and a probability of success *p*, the expected value equals *n⋅p*, and the variance is *n⋅p⋅*(1-*p*).

If *n* is greater than 50, these binomial distribution parameters can be taken as the mean and variance of a normal distribution fairly close to the binomial. The normal distribution will be closest to the binomial when the expected value has *n⋅p* for the mean value and *n⋅p⋅*(1-*p*) for the variance.