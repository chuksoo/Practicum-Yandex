# Takeaway sheet: Distance Between Vectors

## Practice

```python
# Scalar product of vectors

import numpy as np

dot_value1 = np.dot(vector1, vector2)
dot_value2 = vector1 @ vector2
```

```python
# Euclidean distance between vectors

import numpy as np
from scipy.spatial import distance

d = distance.euclidean(a, b)
```

```python
# Manhattan distance between vectors

import numpy as np
from scipy.spatial import distance

d = distance.cityblock(a, b)
```

```python
# Indices of mimimum and maximum elements in array

index = np.array(distances).argmin() # minimum element index
index = np.array(distances).argmax() # maximum element index
```

```python
# Creating class

class ClassName:
    def fit(self, arg1, arg2, ...): # class method
        # method content
```

## Theory

**Scalar product** is an operation resulting in a number (**scalar**) that is equal to the sum of element-by-element products of two vectors' elements

**Euclidian distance**  between vectors 𝑎=(𝑥1, 𝑥2, ..., 𝑥𝑛) and 𝑏=(𝑦1, 𝑦2,..., 𝑦𝑛) is the sum of squared differences of coordinates:

![Takeaway%20sheet%20Distance%20Between%20Vectors%20b9cf39e44c214944b8a789807d87d0f0/d2ab.jpg](Takeaway%20sheet%20Distance%20Between%20Vectors%20b9cf39e44c214944b8a789807d87d0f0/d2ab.jpg)

**Manhattan distance** or **city block distance** is the sum of modules of coordinate differences of vectors 𝑎=(𝑥1, 𝑥2, ..., 𝑥𝑛) и 𝑏=(𝑦1, 𝑦2,..., 𝑦𝑛):

![Takeaway%20sheet%20Distance%20Between%20Vectors%20b9cf39e44c214944b8a789807d87d0f0/dab)).jpg](Takeaway%20sheet%20Distance%20Between%20Vectors%20b9cf39e44c214944b8a789807d87d0f0/dab)).jpg)

**Class** is a new data type with its own methods and attributes.