# Chapter Summary: Vectors and Vector Operations

## Creating vectors

In Python, datasets are often represented as lists. In mathematics, an ordered set of numerical data is a **vector**, or an **arithmetic vector**. The operations that can be performed with numbers can be performed with vectors as well: addition, subtraction, and multiplication. In Python, operations with vectors are hundreds of times faster than operations with lists.

To work with vectors, let's turn to the **NumPy** library. Convert a two number list and convert it into a vector:

```python
import numpy as np

numbers1 = [2, 3] # Python list
vector1 = np.array(numbers1) # NumPy array
print(vector1)
```

Vectors can be created without a temporary variable:

```python
import numpy as np
vector2 = np.array([6, 2])
print(vector2)
```

Vectors can be converted into lists:

```python
numbers2 = list(vector2) # List from vector
print(numbers2)
```

The column of the DataFrame structure in pandas is converted into a NumPy vector using the `**values**` attribute:

```python
import pandas as pd

data = pd.DataFrame([1, 7, 3])
print(data[0].values)
```

Use the `len()` function to determine the vector size (number of its elements):

```python
print(len(vector2))
```

## Vector presentation

Let's plot a two-dimensional vector. It consists of two numbers: the first is the coordinate along the horizontal *x* axis, and the second one is the coordinate for the vertical *y* axis. The vector is represented by a **point** or an **arrow** that connects the origin and the point with coordinates (*x, y*). We use arrows when we want to indicate the movements. If we work with several vectors that may lie along the same line, it is better to use a point to represent a vector.

Vector elements are also called coordinates.

```python
import numpy as np
import matplotlib.pyplot as plt

vector1 = np.array([2, 3])
vector2 = np.array([6, 2])

plt.figure(figsize=(7, 7))
plt.axis([0, 7, 0, 7])
# 'ro' argument sets graph style
# 'r' - red
# 'o' - circle
plt.plot([vector1[0], vector2[0]], [vector1[1], vector2[1]], 'ro') 
plt.grid(True)
plt.show()
```

![Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/lesson3_1.png](Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/lesson3_1.png)

Let's use arrows to draw the same vectors. Instead of `plt.plot()`, call **`plt.arrow()`.**

```python
import numpy as np
import matplotlib.pyplot as plt

vector1 = np.array([2, 3])
vector2 = np.array([6, 2])

plt.figure(figsize=(7, 7))
plt.axis([0, 7, 0, 7])
plt.arrow(0, 0, vector1[0], vector1[1], head_width=0.3,
          length_includes_head="True", color='b')
plt.arrow(0, 0, vector2[0], vector2[1], head_width=0.3,
          length_includes_head="True", color='g')
plt.plot(0, 0, 'ro')
plt.grid(True)
plt.show()
```

![Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/lesson3_2.png](Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/lesson3_2.png)

## Addition and subtraction of vectors

Vectors of the same size have an equal length. The result of their addition is the vector with each coordinate being equal to the sum of the coordinates of the summand vectors. The first coordinate of the resulting vector is equal to the sum of the first coordinates, and the second one is the sum of the second coordinates. When subtracting, each coordinate of the obtained vector is equal to the difference of coordinates of the given vectors.

When adding or subtracting vectors, the operation is performed for each element of the vectors:

![Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/Vector.jpg](Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/Vector.jpg)

```python
import numpy as np

vector1 = np.array([2, 3])
vector2 = np.array([6, 2])
sum_of_vectors = vector1 + vector2
subtraction_of_vectors = vector2 - vector1
```

If we plot a vector that is equal to the green `vector1` in terms of length and direction from the end of the blue `vector2`, we will get the red vector (`sum_of_vectors`).

![Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/lesso4_2.png](Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/lesso4_2.png)

The triangle formed in the graph above gives a geometric sense to the addition of vectors. If each vector is a movement in a certain direction, then the sum of two added vectors is the movement along the first vector followed with the movement along the second one.

The difference of two vectors is a step — for example along `vector2` — followed by a step along the direction opposite to `vector1`.

![Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/Untitled.png](Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/Untitled.png)

## Multiplication of a vector by a scalar

Besides addition and subtraction, vectors can be also multiplied by scalars. Each coordinate of the vector is multiplied by the same number:

![Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/Vector_kx.jpg](Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/Vector_kx.jpg)

If the number is negative, all coordinates also change their signs.

```python
import numpy as np

vector1 = np.array([2, 3])
vector3 = 2 * vector1
vector4 = -1 * vector1
```

When multiplied by a positive number, vectors on the plane maintain direction, but the arrows change length. When multiplied by a negative number, vectors flip to the opposite direction.

![Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/lesson5_1.png](Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/lesson5_1.png)

## Mean value of vectors

If individual vectors in a set describe, customers by features for example, then the mean value of the vectors often describes a typical or *statistically average* customer. For the set of vectors 𝑎1, 𝑎2… 𝑎𝑛 (where *n* is total number of vectors), the **mean value** of vectors is the sum of all vectors multiplied by  1/𝑛. This results in a new vector *a:*

![Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/a.jpg](Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/a.jpg)

If the set consists of only one vector (𝑛=1), it will be equal to the mean: 𝑎=𝑎1. The mean value of two vectors is 𝑎=0.5(𝑎1+𝑎2). The mean value for a pair of two-dimensional vectors is the middle of the segment connecting 𝑎1 and 𝑎2.

```python
import numpy as np

vector1 = np.array([2, 3])
vector2 = np.array([6, 2])
vector_mean = .5*(vector1+vector2)
print(vector_mean)
```

The first coordinate of the new vector is the mean value of the first coordinates of `vector1` and `vector2`, and the second coordinate is the mean value of the second coordinates of `vector1` and `vector2`.

That's how we draw these vectors on the plane: plot the `vector1+vector2` vector and then multiply it by 0.5.

![Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/lesson6_1.png](Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/lesson6_1.png)

## Vectorized Functions

NumPy tools allow for performing various operations with vectors. If we use the `np.array()` function after multiplying and dividing two arrays of the same size, we will obtain a new vector that will also have the same size:

```python
import numpy as np

array1 = np.array([2, -4, 6, -8])
array2 = np.array([1, 2, 3, 4])
array_mult = array1 * array2
array_div = array1 / array2
print("Product of two arrays: ", array_mult)
print("Quotient of two arrays: ", array_div)
```

If arithmetic operations are performed on an array and a single number, then the action is applied to each element of the array. And again, an array of the same size is formed.

To prove the point, let's perform addition, subtraction, and division on an array with a scalar:

```python
import numpy as np

array2 = np.array([1, 2, 3, 4])
array2_plus_10 = array2 + 10
array2_minus_10 = array2 - 10
array2_div_10 = array2 / 10
print("Sum: ", array2_plus_10) 
print("Difference: ", array2_minus_10)
print("Quotient: ", array2_div_10)
```

The same element-by-element principle works on arrays when we deal with standard mathematical functions like exponentiation or logarithms.

Let's raise an array to the second power:

```python
import numpy as np

numbers_from_0 =  np.array([0, 1, 2, 3, 4])
squares = numbers_from_0**2
print(squares)
```

All of that can be done with lists using loops as well, but operations with vectors in NumPy are much faster.

Here's an example: Among the elements of the `values` array, the maximum value and the minimum values are a pair of numbers, *MIN* and *MAX,* provided that *MAX*>*MIN*. For analysis, the data should be converted. Each element 𝑥 of the array should be converted to a number in the range from 0(*MIN*) to 1(*MAX*). Here's the formula of the `min_max_scale()` function:

![Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/f(x).jpg](Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/f(x).jpg)

To apply this function to all elements of the `values` array, call the `max()` and `min()` methods. They will find its maximum and minimum values. As a result, we get an array of the same length, but with converted elements:

```python
import numpy as np
def min_max_scale(values):
    return (values - min(values)) / (max(values) - min(values))

print(min_max_scale(our_values))
```

To apply this function to all elements of the `values` array, call the `max()` and `min()` methods. They will find its maximum and minimum values. As a result, we get an array of the same length, but with converted elements:

![Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/f(x)_1.jpg](Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/f(x)_1.jpg)

where **exp()** is the exponent function (from lat. *exponere*, "to expose"). It raises *e,* Euler‘s number, to the power of the argument. The number is named after the great Swiss mathematician Leonhard Euler and approximately equals 2.718281828.

![Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/plot_plot.jpeg](Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/plot_plot.jpeg)

Perform logistic transformation:

```python
import numpy as np

def logistic_transform(values):
    return 1 / (1 + np.exp(- values))

print(logistic_transform(our_values))
```

## Vectorization of metrics

Store a set of actual values to the `target` variable, and predicted values to the `predictions` variable. Both sets are `np.array` type.

Use standard NumPy functions to calculate the evaluation metrics:

- `sum()` (to find the sum of the elements in an array);
- `mean()` (to calculate the mean value).

Call them as follows: `<array name>.sum()` and `<array name>.mean()`.

For example, here's the formula to calculate the **mean square error** (*MSE*):

![Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/mse.jpg](Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/mse.jpg)

where 𝑛 is the length of each array and ∑ is the summation over all observations of the sample (𝑖 varies from 1 to 𝑛). The ordinal elements of the vectors *target* and *predictions* are denoted by *target*_𝑖 and *predictions*_𝑖. 

Write the formula using `sum()`:

```python
def mse1(target, predictions):
    n = target.size
    return((target - predictions)**2).sum()/n
```

The sum of several numbers divided by their quantity is the mean of such numbers. Let's write the *MSE* formula using `mean()`:

```python
def mse2(target, predictions):
    return((target - predictions)**2).mean()
```

Write the function to calculate *MAE* using `mean()`:

![Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/MAE.jpg](Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/MAE.jpg)

```python
import numpy as np

def mae(target, predictions):
    return np.abs((target - predictions)).mean()

print(mae(target, predictions))
```

Vectorized functions can be used to calculate *RMSE*. Here's the formula:

![Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/RMSE.jpg](Chapter%20Summary%20Vectors%20and%20Vector%20Operations%2079edb41f84d64201983aa14b880663e6/RMSE.jpg)

```python
import numpy as np

def rmse(target, predictions):
    return (((target-predictions)**2).mean())**0.5 

print(rmse(target, predictions))
```