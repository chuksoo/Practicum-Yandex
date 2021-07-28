# Takeaway sheet: Matrices and Matrix Operations

## Practice

```python
# A matrix from a list of lists

import numpy as np

matrix = np.array([
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]])
print(matrix)
```

```python
# A matrix from a list of vectors

import numpy as np

string0 = np.array([1,2,3])
string1 = np.array([-1,-2,-3])
list_of_vectors = [string0, string1]
matrix_from_vectors = np.array(list_of_vectors)

print(matrix_from_vectors)
```

```python
# A matrix from data frames

import pandas as pd
import numpy as np

matrix = df.values
print(matrix)

print('Size:', matrix.shape) # matrix dimensions
print('Row 2:', matrix[2, :]) # vector is the second row of the matrix 
print('Column 1:', matrix[:, 1]) # vector is the first row of the matrix 
```

```python
# Matrix by vector multiplication 

import numpy as np
    
A = np.array([
    [1, 2, 3], 
    [4, 5, 6]])

b = np.array([7, 8, 9])

print(np.dot(A, b))
print(A.dot(b))
```

```python
# Matrix by matrix multiplication 

import numpy as np

print(A.dot(B))
print(np.dot(A,B)) 
print(A @ B)
```

```python
# Transpose of matrix

print(matrix.T)
```

```python
# Creating a class

class ClassName:
    def fit(self, arg1, arg2, ...): # class method
        # method content 
```

## Theory

**A matrix** is a rectangular numeric table or two-dimensional array consisting of m rows and n columns;

**A transpose of the matrix** is a matrix operation when its rows become columns with the same numbers;