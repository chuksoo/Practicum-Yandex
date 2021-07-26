# Chapter Summary: Distance Between Vectors

## Scalar product

If we multiply all the components, and then add up the obtained values, we obtain the **scalar product** or **dot product**. As a result of this operation with two vectors of the same size we obtain a new number. That number is called the **scalar**.

Here's the formula for a scalar product of two vectors 𝑎=[𝑥1, 𝑥2… 𝑥𝑛] and 𝑏=[𝑦1, 𝑦2… 𝑦𝑛]:

![https://github.com/chuksoo/Practicum-Yandex/blob/main/Linear%20Algebra/2.%20Distance%20between%20Vector/Images/ab.jpg](Chapter%20Summary%20Distance%20Between%20Vectors%2031e7aa9e3cda45a9b3f3811e538feab3/ab.jpg)

The scalar product of vectors *a* and *b* is usually denoted by parentheses (𝑎, 𝑏) or a dot 𝑎⋅𝑏.

In NumPy, we can find the scalar product using the `numpy.dot()` ****function:

```python
import numpy as np

dot_value = np.dot(vector1, vector2)
```

The **matrix multiplication operator** allows us to calculate the scalar product even more easily. The operator is denoted by `@`:

```python
import numpy as np

volume = np.array([0.1, 0.3, 0.1])
content = np.array([0.4, 0.0, 0.1])

dot_value = vector1 @ vector2
```

There's also element-by-element multiplication. Unlike the scalar product, the result will be a vector:

```python
import numpy as np

vector3 = vector1 * vector2
```

## Planar distance

The vector length or module equals the square root of the scalar product of the vector and itself. For example, for vector 𝑎=(𝑥, 𝑦), it is calculated like this:

![Chapter%20Summary%20Distance%20Between%20Vectors%2031e7aa9e3cda45a9b3f3811e538feab3/a.jpg](Chapter%20Summary%20Distance%20Between%20Vectors%2031e7aa9e3cda45a9b3f3811e538feab3/a.jpg)

To measure the distance between two points, that is, to obtain the square root of the differences of the vectors, let's find the **Euclidian distance***.* It calculates the shortest distance using the the Pythagorean theorem — the square of the hypotenuse is equal to the sum of the squares of the other sides.

The Euclidean distance can be written as: *d₂*(*a, b*). The *d* carries subscript 2 to indicate that the vector coordinates are raised to the second power.

Distance between points *a*(𝑥1, 𝑦1) and *b*(𝑥2, 𝑦2) is calculated by the formula:

![Chapter%20Summary%20Distance%20Between%20Vectors%2031e7aa9e3cda45a9b3f3811e538feab3/dab.jpg](Chapter%20Summary%20Distance%20Between%20Vectors%2031e7aa9e3cda45a9b3f3811e538feab3/dab.jpg)

Let's find the Euclidean distance between points *a*=(5, 6) and *b*=(1, 3):

```python
import numpy as np

a = np.array([5, 6])
b = np.array([1, 3])
d = np.dot(a-b, a-b)**0.5
print('Distance between a and b is equal to', d)
```

SciPy has a dedicated **distance** library for distance calculations. Call the function to find the Euclidean distance `distance.euclidean()`:

```python
import numpy as np
from scipy.spatial import distance

a = np.array([5, 6])
b = np.array([1, 3])
d = distance.euclidean(a, b)
print('Distance between a and b is equal to', d)
```

The calculation results are the same.

## Manhattan distance

**Manhattan distance** or **city block distance** is the sum of modules of coordinate differences. The name is due to the fact that the street layout of Manhattan makes it impossible to use the Euclidean distance (calculated using the straight line).

Let's calculate the Manhattan distance between points *a=(𝑥1, 𝑦1)* and *b=(𝑥2, 𝑦2)* using the formula:

![Chapter%20Summary%20Distance%20Between%20Vectors%2031e7aa9e3cda45a9b3f3811e538feab3/d1ab.jpg](Chapter%20Summary%20Distance%20Between%20Vectors%2031e7aa9e3cda45a9b3f3811e538feab3/d1ab.jpg)

Manhattan distance is formulated *d₁(a, b)*. The *d* carries subscript 1 to indicate that the vector coordinates are raised to the first power (the number doesn't change).

In SciPy the function for Manhattan distance calculation is called `distance.cityblock()`:

```python
import numpy as np
from scipy.spatial import distance

a = np.array([5, 6])
b = np.array([1, 3])
d = distance.cityblock(a, b)
print('Distance between a and b is equal to', d)
```

To find the minimum index in the NumPy array, call the `argmin()` ****function.

```python
index = np.array(distances).argmin() # minimum element index
```

## Distances in multidimensional space

In machine learning, vectors are features of observations. Usually the vectors are multidimensional rather than two dimensional.

The Euclidean distance between vectors 𝑎=(𝑥1, 𝑥2… 𝑥𝑛) and 𝑏=(𝑦1, 𝑦2… 𝑦𝑛) is the sum of squares of coordinate differences:

![Chapter%20Summary%20Distance%20Between%20Vectors%2031e7aa9e3cda45a9b3f3811e538feab3/d2ab.jpg](Chapter%20Summary%20Distance%20Between%20Vectors%2031e7aa9e3cda45a9b3f3811e538feab3/d2ab.jpg)

The Manhattan distance is the sum of modules of coordinate differences:

![Chapter%20Summary%20Distance%20Between%20Vectors%2031e7aa9e3cda45a9b3f3811e538feab3/dab)).jpg](Chapter%20Summary%20Distance%20Between%20Vectors%2031e7aa9e3cda45a9b3f3811e538feab3/dab)).jpg)

When the number of coordinates is more than two, we still use the familiar functions `distance.euclidean()` and `distance.cityblock()` to calculate distances in multidimensional space.

## Nearest neighbors algorithm

Take a look at the picture below. How can we predict the observation class? We can find the nearest object in the sample and get the answer from it. That's how the **nearest neighbors algorithm** works. Usually we look for the nearest observation in the training set.

![Chapter%20Summary%20Distance%20Between%20Vectors%2031e7aa9e3cda45a9b3f3811e538feab3/metod_soseda.jpg](Chapter%20Summary%20Distance%20Between%20Vectors%2031e7aa9e3cda45a9b3f3811e538feab3/metod_soseda.jpg)

The algorithm works both on the plane and in multidimensional space, in which case the distances are calculated using multidimensional formulas.

## Creating model class

**Class** is a new data type with its own methods and attributes. Let's take a look at the constant model for a regression task. It predicts answers based on the mean value of the target in the training set.

To create a new class, specify key word `class` followed by the name of the class:

```python

class ConstantRegression:
    # class content with four-space offset
    # ...
```

To train the model, let's use the `fit()` method. It's a function inside the class and the first parameter for it is always `**self**`. `self` is a variable that stores the model. It is needed for working with the attributes. Two other parameters are features and target of the training set, just like in sklearn.

```python
class ConstantRegression:
    def fit(self, features_train, target_train):
        # function content with 4+4-offset
        # ...
```

In the process of training, we need to save the mean value of the target. To create the new attribute `value`, add `self` with a dot to the beginning of the variable name. This way, we indicate that the variable is inside the class:

```python
class ConstantRegression:
    def fit(self, features_train, target_train):
        self.value = target_train.mean()
```

Let's use the `predict()` method to predict the answer, which is the saved mean:

```python
class ConstantRegression:
    def fit(self, features_train, target_train):
        self.value = target_train.mean()

    def predict(self, new_features):
        answer = pd.Series(self.value, index=new_features.index)
        return answer
```
