# Chapter Summary: Linear Regression From the Inside

## Linear regression model

In linear regression, features are a vector of numbers in n-dimensional space (let's say *x*). The prediction of the model (a) is calculated as follows: the feature vector is scalar multiplied by the **weight** vector (w), then the value of the prediction **bias** is added to this product:

![Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/a.jpg](Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/a.jpg)

The w vector and a w0 scalar are parameters of the model. There are n parameters in the w vector, and one in w0. In other words, the number of parameters is greater than the length of the features vector by one.

If the length of the features vector is equal to one, then there is only one feature in the sample. Let's draw this feature with the answers on the graph:

![Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/priznak.jpg](Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/priznak.jpg)

Prediction plots for linear regression are set by the equation:

![Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/y_1.jpg](Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/y_1.jpg)

If you change the parameters *w* and *w0*, you will get any straight line (hence the model takes its name):

![Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/priznak3.jpg](Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/priznak3.jpg)

## Training objective

We need to analyze the learning algorithm. Our quality metric will be MSE: the model should achieve its lowest value on the test data. The goal of the training task is formulated as follows: find the model parameters for which the value of the **loss function** on the training set is minimal. As a quality metric, it takes correct responses and predictions as input. It returns a values which represents "losses" (they need to be minimized). In our task, this function is equated to *MSE*. But usually, the loss function is used for training, and the quality metric is used for testing.

Let's write the goal of the training task in vector format. The training set is represented as matrix *X*, in which the rows correspond to objects, and the columns correspond to features. Let's denote the linear regression parameters as *w* and *w0*. To get the prediction vector a, multiply the *X* matrix by the *w* vector and add the *w0* prediction bias value.

The formula is: 

![Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/A_xw.jpg](Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/A_xw.jpg)

To shorten it, let's change the notation. In the *X* matrix, add a column consisting only of ones (it will be the 0 column); and the parameter *w0* add to the *w* vector:

![Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/x_w.jpg](Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/x_w.jpg)

Then multiply the *X* matrix by the *w* vector. The prediction bias is multiplied by a vector of ones (column zero). We get the resulting prediction vector *a*:

![Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/A_xw_1.jpg](Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/A_xw_1.jpg)

Now we can introduce a new notation y - the vector of target feature values for the training set.

Write the formula for training the linear regression of the *MSE* loss function:

![Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/min.jpg](Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/min.jpg)

The `argmin()` function finds the minimum and returns the indices at which it was reached.

## Inverse matrix

**An identity matrix** (also known as a unit matrix) is a square matrix with ones on the main diagonal and zeros elsewhere. If any matrix A is multiplied by an identity matrix (or vice versa), we will get the same matrix A:

![Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/AE.jpg](Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/AE.jpg)

The **inverse matrix** for a square matrix A is a matrix A with a superscript -1 whose product with A is equal to the identity matrix. Multiplication can be performed in any order:

![Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/AA.jpg](Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/AA.jpg)

Matrices for which you can find inverses are called **invertible** matrix. But not every matrix has an inverse. This matrix is called a **non-invertible** matrix.

Non-invertible matrices are rare. If you generate a random matrix with the `numpy.random.normal()` function, the probability of getting a non-invertible matrix is close to zero.

To find the inverse matrix, call the `numpy.linalg.inv()` function. It will also help you check the matrix for invertibility: if the matrix is non-invertible, an error will be detected.

## Training linear regression

The task of training linear regression is:

![Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/min.jpg](Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/min.jpg)

The minimum *MSE* value is obtained when the weights are equal to this value:

![Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/W.jpg](Chapter%20Summary%20Linear%20Regression%20From%20the%20Inside%2008137c202e7b4d3c8aecd8fc6b2499dc/W.jpg)

How did we get this formula:

- The transposed feature matrix is multiplied by itself;
- The matrix inverse to the result is calculated;
- The inverse matrix is multiplied by the transposed feature matrix;
- The result is multiplied by the vector of the target feature values.