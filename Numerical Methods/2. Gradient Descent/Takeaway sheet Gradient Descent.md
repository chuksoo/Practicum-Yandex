# Takeaway sheet: Gradient Descent

**Practice**

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

**Theory**

The **gradient of a vector-valued function** is a vector consisting of derivatives of the answer for each argument that indicates the direction in which the function grows the fastest.

**Gradient descent** is an iterative algorithm for finding the loss function minimum. It moves in the direction of the negative gradient and gradually approximates the minimum.