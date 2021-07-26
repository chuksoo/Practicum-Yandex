# Takeaway sheet: Vectors and Vector Operations

## Practice

```python
# Creating NumPy array 

import numpy as np

numbers1 = [2, 3] # Python list
vector1 = np.array(numbers1) # NumPy array
vector2 = np.array([6, 2])
```

```python
# Converting NumPy array into list

numbers2 = list(vector2) # List from vector
```

```python
# Obtaining NumPy array - dataframe column

data[0].values
```

```python
# Arithmetic operations on vectors

import numpy as np

sum_of_vectors = vector1 + vector2 # sum of two vectors
subtraction_of_vectors = vector2 - vector1 # difference of two vectors
vector4 = -5 * vector1 # multiplying vector by scalar
array_mult = array1 * array2 # element-by-element product of vectors
array_div = array1 / array2 # element-by-element quotient of vectors

array2_plus_10 = array2 + 10 # adding a number to each element of vector
array2_minus_10 = array2 - 10 # subtracting a number from each element of vector
array2_div_10 = array2 / 10 # dividing each element of vector by a number

vector_1_squared = vector_1**2 # element by element exponentation
```

```python
# Vector minimum and maximum

min(vector)
max(vector)
```

```python
# Vector exponent

np.exp(vector)
```

```python
# Sum and mean of vector elements

vector.sum()
vector.mean()
```

## Theory

**Vector** is an ordered set of numerical data.