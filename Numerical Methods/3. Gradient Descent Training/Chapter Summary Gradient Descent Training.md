# Chapter Summary: Gradient Descent Training

## Gradient descent for linear regression

Remember the linear regression training task:

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/min.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/min.jpg)

Let’s train a model using gradient descent. But first, write down the loss function in vector form to find its gradient. Express *MSE* as a scalar product of the difference of vectors:

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/MAE.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/MAE.jpg)

where *y* is the correct answer vector, and *a* is the prediction vector.

Convert the scalar product to a matrix product:

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/ay.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/ay.jpg)

After transposing the vector — that is, converting it from a column to a row — we can multiply it by another vector.

Combine the *MSE* and linear regression formulas:

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/MAEx.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/MAEx.jpg)

Find the function gradient for parameter vector *w*. Gradients of vector-valued functions are calculated similar way as derivatives. For example, when working with numbers, the partial derivative of (*xw* - *y*)² for the parameter vector *w* is equal to *2x(xw - y).* When dealing with vectors, only the factor of *w* remains from the first parenthesis ( Xᵀ):

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/MAEx1.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/MAEx1.jpg)

## Stochastic gradient descent

We can calculate the gradient using small parts of the training set. These parts are called **mini-batches** or **batches**. For the algorithm to "see" the whole training set, its batches at each iteration should be changed randomly. Here we need the **mini-batch stochastic gradient descent,** or **stochastic gradient descent, SGD.**

To obtain batches, we need to shuffle all the data of the training set and divide it into parts. One batch should contain an average of 100-200 observations (the **batch size)**. When the *SGD* algorithm has gone through all the batches one time, it means that one **epoch** has ended. The number of epochs depends on the size of the training set. It can be one or two if the set is large, or several dozen if the set is small. The number of batches is equal to the number of iterations for the completion of one epoch.

Here’s how the *SGD* algorithm works:

1. Input hyperparameters: batch size, number of epochs, and step size.
2. Define the initial values of the model weights.
3. Split the training set into batches for each epoch.
4. For each batch:

    4.1. Calculate the loss function gradient;

    4.2. Update the model weights (add the negative gradient multiplied by the step size to the current weights).

5. The algorithm returns the final model weights.

Let's find the computational complexity of *SGD* with the following definitions:

- *n* — the number of observations in the whole training set;
- *b* — the batch size;
- *p* — the number of features.

## SGD in Python

Let's learn how to pass hyperparameters to a model. We need to declare the model class and create method "**class initializer**" (`__init__`):

```python

class SGDLinearRegression:
    def __init__(self):
        ...
```

Add one hyperparameter `step_size` to the class initializer:

```python
class SGDLinearRegression:
    def __init__(self, step_size):
        ...
```

Now we can pass the step size to the model when creating a class:

```python
# you can choose step size arbitrarily
model = SGDLinearRegression(0.01)
```

Save the step size as an attribute:

```python
class SGDLinearRegression:
    def __init__(self, step_size):
        self.step_size = step_size
```

Here's the full implementation of the SGD algorithm:

```python
class SGDLinearRegression:
    def __init__(self, step_size, epochs, batch_size):
        self.step_size = step_size
        self.epochs = epochs
        self.batch_size = batch_size
    
    def fit(self, train_features, train_target):
        X = np.concatenate((np.ones((train_features.shape[0], 1)), train_features), axis=1)        
        y = train_target
        w = np.zeros(X.shape[1])
        
        for _ in range(self.epochs):
            batches_count = X.shape[0] // self.batch_size
            for i in range(batches_count):
                begin = i * self.batch_size
                end = (i + 1) * self.batch_size
                X_batch = X[begin:end, :]
                y_batch = y[begin:end]
                
                gradient = 2 * X_batch.T.dot(X_batch.dot(w) - y_batch) / X_batch.shape[0]
                
                w -= self.step_size * gradient

        self.w = w[1:]
        self.w0 = w[0]

    def predict(self, test_features):
        return test_features.dot(self.w) + self.w0
```

## Linear regression regularization

Let's modify the loss function to get rid of overfitting. To reduce the overfitting, we can use **regularization***.* It "fines" the model if the parameter values complicate the algorithm operation. For a linear regression model, regularization implies the limitation of weights. The lower the weight values, the easier it is to train the algorithm. To find out how large the weights are, we calculate the distance between the weight vector and the vector consisting of zeros. For example, the Euclidean distance *d₂*(*w*, 0) is equal to the scalar product of the weights alone: (*w, w*).

To limit the weight values, include the scalar product of the weights in the loss function formula:

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/lw.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/lw.jpg)

The derivative (*w, w*) is equal to *2w*. Calculate the loss function gradient:

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/lw1.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/lw1.jpg)

To control the magnitude of regularization, add the **regularization weight** to the loss function formula. It is denoted as *λ.*

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/lw2.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/lw2.jpg)

The regularization weight is also added to the gradient calculation formula:

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/lw3.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/lw3.jpg)

When we use Euclidean distance for weight regularization, such linear regression is called **ridge regression**.

Here's how the SGD will look if we take into account regularization:

```python
class SGDLinearRegression:
    def __init__(self, step_size, epochs, batch_size, reg_weight):
        self.step_size = step_size
        self.epochs = epochs
        self.batch_size = batch_size
        self.reg_weight = reg_weight
    
    def fit(self, train_features, train_target):
        X = np.concatenate((np.ones((train_features.shape[0], 1)), train_features), axis=1)        
        y = train_target
        w = np.zeros(X.shape[1])
        
        for _ in range(self.epochs):
            batches_count = X.shape[0] // self.batch_size
            for i in range(batches_count):
                begin = i * self.batch_size
                end = (i + 1) * self.batch_size
                X_batch = X[begin:end, :]
                y_batch = y[begin:end]
                
                gradient = 2 * X_batch.T.dot(X_batch.dot(w) - y_batch) / X_batch.shape[0]
                reg = 2 * w.copy()
                reg[0] = 0
                gradient += self.reg_weight * reg
                
                w -= self.step_size * gradient

        self.w = w[1:]
        self.w0 = w[0]

    def predict(self, test_features):
        return test_features.dot(self.w) + self.w0
```

## Basics of neural networks

A **neural network** is a model that consists of many simple models (for example, linear regression models). The name comes from biology: an artificial neural network uses the principal of a neural cell network operation where neurons build complex relationships between input and output data.

Here's an example of a neural network with three inputs *x₁, x₂, x₃* and two outputs *а₁, а₂*:

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/nejron.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/nejron.jpg)

The value at each output, or neuron, is calculated in the same way as a linear regression prediction:

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/a1.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/a1.jpg)

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/a2.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/a2.jpg)

Each output value has its own weights (*w₁* and *w₂*).

Here's another example. The network has three inputs *x₁, x₂, x₃*, two hidden variables *h₁* and *h₂,* and one output *а*.

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/nejron2.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/nejron2.jpg)

Values *h₁* and *h₂* are passed to the logistic function *σ(x):*

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6.jpg)

where e is the Euler number (approximately 2.718281828).

The logistic function in a neural network is called an **activation function**. It is included in the neuron after multiplying the input values by the weights, when the neuron outputs become inputs for other neurons. This way, we can describe more complex dependencies.

Each hidden variable *(h₁, h₂)* is equal to the input value multiplied by a weight:

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/h1.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/h1.jpg)

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/h2.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/h2.jpg)

For convenience, we denote hidden variables *h₁* and *h₂* as vector *h*. Here's the formula for calculating the neural network prediction:

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/a.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/a.jpg)

For convenience, we denote hidden variables *h₁* and *h₂* as vector *h*. Here's the formula for calculating the neural network prediction:

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/w3.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/w3.jpg)

If we put the weights of several neurons into matrices, we can get an even more complex network, for example:

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/nejron3.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/nejron3.jpg)

where:

- *x* — input vector with dimension *p* (number of features)
- *W₁* — matrix with dimension *p x m*
- *W₂* — matrix with dimension *m x k*
- *W₃* — matrix with dimension *k x 1*
- a — model prediction (single number)

When such a neural network calculates a prediction, it sequentially performs all operations:

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/a%201.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/a%201.jpg)

## Training of neural networks

To train a neural network, we need to state the training objective. Any neural network can be written as a function from its input vector and parameters. Let’s define the following:

- *X* — training set features
- *P* — set of all neural network parameters
- *N(X, P) —* neural network function

Let's take this neural network:

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/nejron3.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/nejron3.jpg)

Neural network parameters are weights in neurons:

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/pw.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/pw.jpg)

Here's the neural network function:

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/nxp.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/nxp.jpg)

Let’s also define:

- *y* — training set answers
- *L(a, y)* — loss function (for example, *MSE)*

Then we can state the objective of neural network training as follows:

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/minp.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/minp.jpg)

The minimum of this function can be also found using the *SGD* algorithm.

The neural network learning algorithm is the same as the SGD algorithm for linear regression. Only instead of gradient for linear regression, we calculate the neural network gradient.

![Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/ll.jpg](Chapter%20Summary%20Gradient%20Descent%20Training%207c2bc919475c42ff8201117bdd270ea6/ll.jpg)