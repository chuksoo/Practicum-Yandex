# Chapter Summary: Gradient Descent

## Loss function minimization

To state the task for gradient descent, let's look at the training problem from a new angle. You are already familiar with the loss function. It returns the number of losses from incorrect model answers and is usually used for training.

In the previous course, we equated the loss function with MSE. In this new task, let's denote the loss function as *L( y, a ),* where vector *y* represents the correct answers, and vector *a* represents predictions.

Write the model training task via loss function as follows:

![Chapter%20Summary%20Gradient%20Descent%20d759d07dbce942a1abe88aba7708fd56/argmin.jpg](Chapter%20Summary%20Gradient%20Descent%20d759d07dbce942a1abe88aba7708fd56/argmin.jpg)

To calculate MSE, or the **quadratic loss function**, square the difference between correct answers and predictions:

![Chapter%20Summary%20Gradient%20Descent%20d759d07dbce942a1abe88aba7708fd56/lay.jpg](Chapter%20Summary%20Gradient%20Descent%20d759d07dbce942a1abe88aba7708fd56/lay.jpg)

What other loss functions exist for a regression task? If we want the function in the task to be less sensitive to outliers, then instead of MSE, we use the **absolute loss function (***MAE)* which you are already familiar with. Just like in the case with *MSE,* we use it as a loss function, not an evaluation metric.

![Chapter%20Summary%20Gradient%20Descent%20d759d07dbce942a1abe88aba7708fd56/lay_2.jpg](Chapter%20Summary%20Gradient%20Descent%20d759d07dbce942a1abe88aba7708fd56/lay_2.jpg)

For classification problems, the *accuracy* metric is often used. But it is rarely suitable as a loss function. This is because the accuracy calculation function does not have a **derivative** that shows the change in the function at small changes in the argument.

Let's replace the *accuracy* with the **negative logarithmic likelihood**, or the **logistic loss function**. The loss function adds up the logarithms of probabilities depending on the observation. If the correct answer is 0, *log₁₀ aᵢ* is added. If it is zero, *log₁₀* (1 - *aᵢ*) is added. **Logarithm** is the power to which the base (in our case, 10) is raised to extract the argument.

Here's the formula:

![Chapter%20Summary%20Gradient%20Descent%20d759d07dbce942a1abe88aba7708fd56/lay_3.jpg](Chapter%20Summary%20Gradient%20Descent%20d759d07dbce942a1abe88aba7708fd56/lay_3.jpg)

where *aᵢ* is probability of class 1 for observation with index *i*. That is, the value of *aᵢ* should be as high as possible for a positive class observation, and as low as possible for a negative class observation.

The name of the negative logarithmic likelihood comes from the **likelihood function**. It calculates the probability of the model giving correct answers for all observations if it takes the values of *aᵢ* for the answer:

![Chapter%20Summary%20Gradient%20Descent%20d759d07dbce942a1abe88aba7708fd56/lay_4.jpg](Chapter%20Summary%20Gradient%20Descent%20d759d07dbce942a1abe88aba7708fd56/lay_4.jpg)

Taking the logarithm "stretches" the values over a wider range. For example, the range from 0 to 1 turns into the range from -∞ to 0. For this range, the calculation errors are not that important. We multiply by -1 because the final loss function should be minimized.

Unlike *accuracy*, logarithmic loss function has a derivative.

## Function gradient

The loss function minimum cannot always be found manually. The **function gradient** can help to find the direction.

The loss function depends on the parameters of the algorithm. This function is a **vector-valued function**, that is, it takes a vector and returns a scalar.

The gradient of a vector-valued function is a vector consisting of derivatives of the answer for each argument. It is denoted ∇ (nabla — a Hebrew harp of the same shape). Gradient of the *f* function from a n-dimensional vector x is calculated as follows:

![Chapter%20Summary%20Gradient%20Descent%20d759d07dbce942a1abe88aba7708fd56/fx.jpg](Chapter%20Summary%20Gradient%20Descent%20d759d07dbce942a1abe88aba7708fd56/fx.jpg)

where *∂f/∂xi* is the partial derivative of the function *f* for the argument *xᵢ.* The function gradient for one argument is the derivative.

The gradient indicates the direction in which the function grows the fastest. It doesn't fit the minimization problem though. We need the opposite vector, the one that shows the fastest decrease — the **negative** **gradient**. It can be found as follows:

![Chapter%20Summary%20Gradient%20Descent%20d759d07dbce942a1abe88aba7708fd56/-fx.jpg](Chapter%20Summary%20Gradient%20Descent%20d759d07dbce942a1abe88aba7708fd56/-fx.jpg)

## Gradient descent

**Gradient descent** is an iterative algorithm for finding the loss function minimum. It moves in the direction of the negative gradient and gradually approximates the minimum.

It is difficult to get to the minimum in one iteration, because the negative gradient vector shows the direction of decrease, and not the specific minimum point of the loss function.

To begin the descent, let's pick the **initial value** of the argument (vector *x*). It is denoted as x⁰. From there, the first **gradient descent step** will be made. The next point, x¹ is calculated as follows: add the negative gradient multiplied by the size of the gradient descent step (*μ*) to point x⁰.

![Chapter%20Summary%20Gradient%20Descent%20d759d07dbce942a1abe88aba7708fd56/-fx_1.jpg](Chapter%20Summary%20Gradient%20Descent%20d759d07dbce942a1abe88aba7708fd56/-fx_1.jpg)

The value *μ* controls the size of the gradient descent step. If the step is small, the descent will take many iterations, but each one will bring us closer to the loss function minimum. When the step is too big, we can miss the minimum (just like the diver hitting the rock).

Repeat to obtain the values of arguments at subsequent iterations. The number of iterations is denoted as *t*. To get the new values of *xᵗ*, multiply the negative gradient by the step size and add this product to the previous point:

![Chapter%20Summary%20Gradient%20Descent%20d759d07dbce942a1abe88aba7708fd56/-fx_t.jpg](Chapter%20Summary%20Gradient%20Descent%20d759d07dbce942a1abe88aba7708fd56/-fx_t.jpg)

Gradient descent is completed when:

- the algorithm completes the required number of iterations

or

- the *x* value is no longer changing.

## Gradient descent in Python

First, let’s sum up the steps necessary to run a gradient descent algorithm:

1. In the arguments of the algorithm, set the initial value, x⁰.
2. Calculate the gradient of the loss function (this is the vector of partial derivatives with respect to each argument that takes vector *x* as input).
3. Find the new value using the formula:

    ![Chapter%20Summary%20Gradient%20Descent%20d759d07dbce942a1abe88aba7708fd56/-fx_t.jpg](Chapter%20Summary%20Gradient%20Descent%20d759d07dbce942a1abe88aba7708fd56/-fx_t.jpg)

    where *μ* is the step size; set in the argument of the algorithm.

4. Perform the number of iterations specified in the arguments.

```python
import numpy as np

def func(x):
    # function to be minimized

def gradient(x):
    # func function gradient

def gradient_descent(initialization, step_size, iterations):
    x = initialization
    for i in range(iterations):
        x = x - step_size * gradient(x)
    return x
```