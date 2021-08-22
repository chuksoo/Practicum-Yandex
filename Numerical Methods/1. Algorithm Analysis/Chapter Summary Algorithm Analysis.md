# Chapter Summary: Algorithm Analysis

## Computational complexity

The **algorithm running time** isn't measured in seconds. It is determined by the number of elementary operations performed by the algorithm: additions, multiplications and comparisons. The running time on any given computer is usually called **real running time**. ****An algorithm's running time is also influenced by its arguments.

The running time of complex algorithms is impossible to calculate. That's why we determine their **computational complexity**, or **asymptotic running time.** The term is based on the word **asymptote,** which defines a straight line that a curve approaches but does not cross.

Let's denote the length of the list as *n*. The working time is a function of *n,* written as *T(n)*. The asymptotic running time of an algorithm shows how *T(n)* grows when *n* increases.

When *T(n)* is a polynomial, the asymptotic running time is equal to the term of the highest power without a coefficient (for example, *n²* instead of *5n²*). As *n* reaches greater values, the other terms become unimportant.

- If *T(n)* = *4n* + 3, the asymptotic running time *T(n) ~ n.* The algorithm has **linear complexity**. The tilde symbol (~) means that the asymptotic runtime is *n*.
- If *T(n) = 5n²* + *3n* - 1, the asymptotic running time *T(n) ~ n².* The algorithm has **quadratic complexity**.
- If *T(n)* = *10n³* - 2*n²* + 5, then *T(n) ~ n³*. The algorithm has **cubic complexity**.
- If *T(n)* = 10, then *T(n)* ~ 1. The algorithm has **constant complexity**, that is, it doesn't depend on *n*.

## Linear regression model training time

The linear regression training objective is represented as follows:

![Chapter%20Summary%20Algorithm%20Analysis%20735817205fa34faea6aa4b2a65a06705/min.jpg](Chapter%20Summary%20Algorithm%20Analysis%20735817205fa34faea6aa4b2a65a06705/min.jpg)

Weights are calculated by this formula:

![Chapter%20Summary%20Algorithm%20Analysis%20735817205fa34faea6aa4b2a65a06705/W.jpg](Chapter%20Summary%20Algorithm%20Analysis%20735817205fa34faea6aa4b2a65a06705/W.jpg)

We'll find the computational complexity of the weights calculation, but first let's go over a few points: 

- Let's define the number of observations in the training set as *n*, and the number of features as *p;*
- The size of matrix *X* will be *n x p*, and the size of vector *y* will be *n;*
- The computational complexity will be defined as *T(n, p)* because it depends on two parameters: *n* and *p.*

To calculate the complexity of algorithm training, add up the answers:

*T(n, p) ~ np² + p³ + np² + np*

There are usually fewer features than observations, meaning *p* < *n*. Multiplying both parts by *p²* results in *p³* < *np²*. Taking only the term with the highest power, we get: *T(n, p) ~ np²*. If there are many features, the training will take more time.

## Iterative methods

The following formula is employed as a **direct method** in linear regression model training:

![Chapter%20Summary%20Algorithm%20Analysis%20735817205fa34faea6aa4b2a65a06705/W.jpg](Chapter%20Summary%20Algorithm%20Analysis%20735817205fa34faea6aa4b2a65a06705/W.jpg)

Direct methods help to find a precise solution using a given formula or algorithm. Their computational complexity is independent of the data.

Another approach to training linear regression models is the use of **iterative methods**, or **iterative algorithms**. They won't give you a precise solution though, only an approximate one. The algorithm performs similar iterations repeatedly, the solution becoming more accurate with each step. If there's no need for high accuracy, just a few iterations will do.

The computational complexity of iterative methods depends on the number of steps they take, which may be affected by the amount of data.

### Bisection method

We will find the solution to the equation *f(x) = 0* using an iterative method. Let *f(x)* be defined as a **continuous function**. That is, you can plot its graph without lifting your pencil off the paper. 

The **bisection method** will help solve our equation. It takes a continuous function and segment [*a, b*] as input. The values *f(a)* and *f(b)* have different signs.

When these two conditions are fulfilled:

1. the function is continuous;
2. the values at the ends of the segment have different signs,

then the root of the equation is located somewhere on the given segment.

At each iteration, the bisection method:

- Checks if any value *f(a)* or *f(b)* equals zero. If it does, the solution has been found;
- Finds the middle of the segment *c = (a + b) / 2;*
- Compares the sign of *f(c)* with the signs of *f(a)* and *f(b)*:
    - If *f(c)* and *f(a)* have different signs, the root is located on the segment *[a, c]*. The algorithm analyzes this segment on its next iteration;
    - If f*(c)* and *f(b)* have different signs, the root is located on the segment *[b, c].* The algorithm analyzes this segment on its next iteration;
    - The signs of *f(a)* and *f(b)* are different, so there are no other options.

The solution's accuracy is usually chosen beforehand, for example, *e* (margin of error) *= 0.000001*. At each iteration, the segment with the root is divided by 2. Once it reaches a length of the segment that is less than *e*, the algorithm can be stopped. This condition is called the **stopping criterion**.

## Comparing methods

A large part of this course focuses on the key iterative method for machine learning—**gradient descent**. Many training algorithms are based on it because it has many advantages over direct methods, such as:

- It works faster with large datasets in linear regressions with the *MSE* loss function.
- It is also suitable for linear regressions with other loss functions (not all of them have formulas).
- It can be used for training neural networks which also lack direct formulas.