# Chapter Summary: Matrices and Matrix Operations

## Creating matrices

A **matrix** (from latin "mother") is a rectangular numeric table or two-dimensional array. It consists of *m* rows and *n* columns (the size is written as 𝑚×𝑛). Matrices are usually denoted by uppercase Latin letters, for example, *A*. Their elements are lowercase with a double index: *aij*, where *i* is the row number and *j* is the column number.

![Chapter%20Summary%20Matrices%20and%20Matrix%20Operations%200c2707ca91cb40878f4f564cb38920ad/a.jpg](Chapter%20Summary%20Matrices%20and%20Matrix%20Operations%200c2707ca91cb40878f4f564cb38920ad/a.jpg)

Call `np.array()`*,* to create a NumPy matrix from a list of lists. All nested lists are the same length.

```python
import numpy as np

matrix = np.array([
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]])
print(matrix)
```

Let's take a list of vectors instead of a list of lists:

```python
import numpy as np

string0 = np.array([1,2,3])
string1 = np.array([-1,-2,-3])
list_of_vectors = [string0, string1]
matrix_from_vectors = np.array(list_of_vectors)

print(matrix_from_vectors)
```

Create a matrix from the pandas table: its `values` attribute is a matrix.

```python
import pandas as pd
import numpy as np

matrix = df.values
print(matrix)
```

The `shape` attribute defines the size of the matrix 𝐴. Its 𝑎𝑖𝑗 element is set in NumPy as A[I,j]: rows and columns are numbered from zero, just like array indices.

```python
import numpy as np

A = np.array([
    [1, 2, 3], 
    [2, 3, 4]])

print('Size:', A.shape)
print('A[1, 2]:', A[1, 2])
```

Select individual rows and columns from the matrix:

```python
import numpy as np

matrix = np.array([
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9],
    [10,11,12]])

print('Row 0:', matrix[0, :])
print('Column 2:', matrix[:, 2])
```

## Operations with matrix elements

You can do the same operations with matrix elements as you do with vector elements. Two matrices can be added, subtracted, multiplied, or divided. The most important part is that the operations are performed element-by-element, and the matrices are the same size. The result of an operation is a matrix of the same size.

```python
import numpy as np

matrix1 = np.array([
    [1, 2], 
    [3, 4]])

matrix2 = np.array([
    [5, 6], 
    [7, 8]])

print(matrix1 + matrix2)
```

You can multiply a matrix by a number, add a number, or subtract it: the operation is applied to each element.

```python
import numpy as np

matrix = np.array([
    [1, 2], 
    [3, 4]])

print(matrix * 2)
print(matrix - 2)
```

## Multiplying a matrix by a vector

To understand how a matrix is multiplied by a vector, let's take a list of rows. Each row of this list (matrix) is a vector multiplied by a scalar, and the resulting numbers form a new vector.

For example, a matrix 𝐴 with the 𝑚×𝑛 size is multiplied by a vector *b* (n-dimensional). The product will be a new vector c=*𝐴b*. This is a 𝑚 - dimensional vector whose 𝑖 coordinate is equal to the scalar product of row 𝑖 of the matrix and b.

![Chapter%20Summary%20Matrices%20and%20Matrix%20Operations%200c2707ca91cb40878f4f564cb38920ad/b.jpg](Chapter%20Summary%20Matrices%20and%20Matrix%20Operations%200c2707ca91cb40878f4f564cb38920ad/b.jpg)

Let's perform this operation in NumPy and call the familiar to us the `np.dot()` function.

```python
import numpy as np
    
A = np.array([
    [1, 2, 3], 
    [4, 5, 6]])

b = np.array([7, 8, 9])

print(np.dot(A, b))
print(A.dot(b))
```

For multiplication to be correct, the size of the vector must be equal to the width of the matrix.

## Transpose of matrix

**The transpose of a matrix** is its "flip" over the main diagonal of the matrix, which goes from the upper-left to the lower-right corner. With this reversal, the matrix A of the 𝑚×𝑛 size is transformed into a matrix of the 𝑛×𝑚 size. In other words, the rows of the matrix become its columns, and the columns become its rows. The transposed matrix is indicated by the upper index **T**:

![Chapter%20Summary%20Matrices%20and%20Matrix%20Operations%200c2707ca91cb40878f4f564cb38920ad/t.jpg](Chapter%20Summary%20Matrices%20and%20Matrix%20Operations%200c2707ca91cb40878f4f564cb38920ad/t.jpg)

In NumPy, this operation is set by the `T` attribute. If you need to build a matrix, start from the list of columns to create a matrix and apply transpose:

```python
import numpy as np

matrix = np.array([
    [1, 2], 
    [4, -4], 
    [0, 17]])

print("Transposed matrix")
print(matrix.T)
```

Multiply the original matrix by a vector with the length equal to 3:

```python
vector = [2, 1, -1]
print(np.dot(matrix, vector))
```

We got an error: the dimensions of the matrix (3, 2) and the vector (3,) are not aligned. The second dimension of the matrix is not equal to the length of the vector. To make the multiplication correct, we transpose the matrix:

```python
print(np.dot(matrix.T, vector))
```

## Matrix multiplication

During **Matrix multiplication,** a third matrix is constructed using two matrices. It consists of scalar products of the rows of the first matrix by the columns of the second. The product of the i row of the matrix A (*Ai*) and the j column of the matrix B (*Bj*) is equal to the matrix *Cij*: 

![Chapter%20Summary%20Matrices%20and%20Matrix%20Operations%200c2707ca91cb40878f4f564cb38920ad/cij.jpg](Chapter%20Summary%20Matrices%20and%20Matrix%20Operations%200c2707ca91cb40878f4f564cb38920ad/cij.jpg)

Matrix multiplication is possible if the width of the first matrix A (𝑚×𝑛) is equal to the height of the second matrix B (𝑛×r). Then the dimensions of their product will be m×r. We say that the dimension n "collapses".

![Chapter%20Summary%20Matrices%20and%20Matrix%20Operations%200c2707ca91cb40878f4f564cb38920ad/ijr.jpg](Chapter%20Summary%20Matrices%20and%20Matrix%20Operations%200c2707ca91cb40878f4f564cb38920ad/ijr.jpg)

In NumPy, matrices A and B are multiplied by calling the functions `np.dot(A, B)`, or `A.dot(B)`. You can also replace this call with a matrix multiplication sign @:

```python
import numpy as np

print(A.dot(B))
print(np.dot(A,B)) 
print(A @ B)
```

The result of matrix multiplication depends on the order of multipliers. The result of matrix multiplication depends on the order of multipliers. 

```python
matrix = np.array([
    [1, 2, 3], 
    [-1, -2, -3]])

print(matrix @ matrix)
```

An error occurred: the dimensions of the matrices are mismatched*.* 

Multiplying the matrix by itself is only possible if it is square:

```python
square_matrix = np.array([
    [1, 2, 3], 
    [-1, -2, -3],
    [0, 0, 0]])

print(square_matrix @ square_matrix)
```