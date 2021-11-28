# Chapter Summary: Fully Connected Networks

## Tasks with Neural Networks

Suppose the observation is a photo, and each pixel is a feature of that observation. 

Here's an example: the picture on the left is a low-resolution black and white image. The middle one is the same image but with shades of gray from 0 (black) to 255 (white). 0-255 is the range of pixel brightness values. That is, the possible feature value. The picture on the right contains only those numbers from the range without the image.

![https://pictures.s3.yandex.net/resources/Screenshot_2020-04-06_at_12.22.32_1586164961.png](https://pictures.s3.yandex.net/resources/Screenshot_2020-04-06_at_12.22.32_1586164961.png)

Let's convert the pixel values into a vector to get our features:

```python
[255, 255, 255, 255, 237, 217, 239, 255, 255, 255, 255, 255, 255, 255, 255, 190, 75, 29, 29, 30, 81, 198, 255, 255, 255, 255, 255, 147, 30, 29, 29, 29, 29, 29, 31, 160, 255, 255, 255, 185, 29, 29, 29, 29, 29, 29, 29, 29, 31, 198, 255, 255, 61, 29, 29, 29, 29, 29, 29, 29, 29, 29, 74, 255, 255, 108, 121, 121, 121, 121, 121, 121, 121, 121, 121, 102, 219, 255, 250, 255, 255, 255, 255, 255, 255, 255, 255, 255, 238, 107, 168, 255, 238, 153, 150, 152, 244, 201, 152, 150, 178, 253, 103, 144, 248, 243, 121, 108, 114, 225, 184, 130, 112, 154, 235, 103, 62, 197, 255, 227, 168, 231, 149, 230, 196, 179, 251, 183, 29, 29, 105, 255, 255, 219, 195, 191, 184, 195, 235, 255, 91, 29, 29, 30, 187, 255, 234, 218, 218, 218, 218, 243, 174, 29, 29, 29, 29, 38, 180, 255, 255, 255, 255, 255, 169, 35, 29, 29, 29, 29, 29, 29, 82, 153, 174, 150, 76, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29]
```

If the size of each image of the dataset is 1920x1080 pixels, then each image is described by 2,073,600 features (1920 multiplied by 1080). Classic algorithms like gradient boosting can't manage the training with so many features.

Let's see what images and texts have in common: 

1. Both have redundant information. 
2. Neighbor features are related to each other. 

## Keras Library

Let's talk about **Keras**, an open source neural network library. In fact, Keras is really more of an interface for working with another more complex library, **TensorFlow.** Another popular neural network library is **PyTorch**, and you're ****you're ****already familiar with it. You might've found it easy to work with, since you used a pretrained model. Regardless, both TensorFlow and PyTorch are difficult for junior coders.

Let's write a linear regression in Keras. A linear regression is a neural network but with only one neuron:

```python
# import Keras
from tensorflow import keras

# create the model
model = keras.models.Sequential()
# indicate how the neural network is arranged
model.add(keras.layers.Dense(units=1, input_dim=features.shape[1]))
# indicate how the neural network is trained
model.compile(loss='mean_squared_error', optimizer='sgd')

# train the model
model.fit(features, target)
```

Let's dissect the code line by line. The first line imports *Keras* from the *tensorflow* library. On the platform, we're using *TensorFlow* v2.1.0.

```python
from tensorflow import keras
```

The next line initializes the model (i.e. the neural network that we will build). Let's set the model class to `**Sequential**`. This class is used for models with sequential layers. **Layer** is a set of neurons that share the same input and output.

```python
model = keras.models.Sequential()
```

Our network will consist of only one neuron (or the value at one output). It has *n* inputs, each multiplied by its own weight. For example, *x₁* is multiplied by *w₁*. There's one more input and it is always equal to unity. Its weight is designated as **b** (bias). It is the selection of weights *w* and *b* that comprises the process of the neural network training. After all the products of the values of the inputs and the weights are summed up, the answer of the neural network (*a*) is sent to the output.

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/x1.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/x1.jpg)

The **`keras.layers.Dense()`** command creates one layer of neurons. "Dense" means that every input will be connected to every neuron, or output. The `**units**` parameter sets the number of neurons in the layer, and `**input_dim**` sets the number of inputs in the layer. Note that this parameter doesn't take the bias into the account.

To create a layer for our network, write:

```python
# take the number of inputs from the training set
keras.layers.Dense(units=1, input_dim=features.shape[1])
```

Layers where all inputs are connected to all neurons are called **fully connected layers**. The fully connected layer set by the `keras.layers.Dense(units=2, input_dim=3)` command looks like this:

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/x1%201.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/x1%201.jpg)

To add the fully connected layer to the model, call the `model.add()` method:

```python
model.add(keras.layers.Dense(units=1, input_dim=features.shape[1]))
```

Take a look at this line:

```python
 model.compile(loss='mean_squared_error', optimizer='sgd') 
```

It prepares the model for training. After this command, the network structure can no longer be changed. Specify MSE as the regression task loss function for the `loss` parameter. Set the gradient descent method for the `optimizer='sgd'` parameter. Remember, neural networks are trained using SGD.

Now let's run the training:

```python
model.fit(features, target)
```

## Logistic Regression

Linear regression is a neural network with only one neuron. The same can be said about logistic regression. If observations have only two classes, the difference between linear regression and logistic regression is almost imperceptible. We need to add one extra element.

Here's what linear regression looks like:

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/x1.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/x1.jpg)

And here's what logistic regression looks like:

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/x1-1.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/x1-1.jpg)

The latter diagram has the **sigmoid function** or activation function. It takes any real number as the input and returns a number in the range from 0 (no activation) to 1 (activation).

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97.jpg)

In the formula, *e* is Euler's number, which is approximately equal to 2.718281828.

This number in the range from 0 to 1 can be interpreted as a prediction of a neural network on whether the observation belongs to the positive class or the negative class.

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97%201.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97%201.jpg)

If the sum of the products of the inputs' values and the weights (z) is very large, then at the sigmoid output, we'll get a number close to unity:

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97%202.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97%202.jpg)

But if, on the contrary, the sum is a large negative number, then the function returns a number close to zero:

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97%203.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97%203.jpg)

The loss function varies depending on the neural network type. The MSE is used in regression tasks, while **Binary Cross-Entropy (BCE)** is suitable for a binary classification. We can't use the *accuracy* metric because it doesn't have a product, making it impossible for SGD to work.

BCE is calculated as follows:

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97%204.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97%204.jpg)

In the formula, p is the correct answer probability. The base of the logarithm doesn't matter because the change of the base is the multiplication of the loss function by the constant, which doesn't change the minimum.

If the target = 1, then the correct answer probability is:

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/p.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/p.jpg)

If the target = 0, then p is:

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/pp.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/pp.jpg)

To better understand the BCE function, take a look at its graph:

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/log.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/log.jpg)

If the correct answer probability *p* is approximately equal to unity, then *-log(p)* is a positive number close to zero. Therefore, the error is small. If the correct answer probability *p≈0,* then *-log(p)* is a large positive number. Therefore, the error is large as well.

## Logistic Regression in Keras

To get a logistic regression, we only need to change the linear regression code in two places:

1. Apply the activation function to the fully connected layer:

```python
keras.layers.Dense(units=1, input_dim=features_train.shape[1], 
                   **activation='sigmoid'**)
```

2. Change the loss function from MSE to `binary_crossentropy`:

```python
model.compile(**loss='binary_crossentropy'**, optimizer='sgd')
```

## Fully Connected Neural Networks

Time to get a closer look at **the fully connected neural networks**. In these networks, every neuron in each layer is connected with each neuron of the previous layer. 

Below is an example of a fully connected network. You should note that all the layers except for the input and output layers are called **hidden layers**:

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/neuron3.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/neuron3.jpg)

Let's analyze the structure of this fully connected network. Every neuron except for the last one is followed by an activation function. Wonder why? Take a look at the example of such a network without the b weight:

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/x1%202.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/x1%202.jpg)

To get z, sum up all the products of the input values and the weights:

```
z1 = x1 * w11 + x2 * w12
z2 = x1 * w21 + x2 * w22
z3 = z1 * w31 + z2 * w32
```

We get:

```
z3 = (x1 * w11 + x2 * w12) * w31 + (w21 * x1 + w22 * x2) * w32
```

Take *x₁* and *x₂* out of the brackets:

```
z3 = x1 * (w11 * w31 + w21 * w32) + x2 * (w12 * w31 + w22 * w32)
```

For convenience, we'll introduce new notation, w₁ and w₂:

```
w1' = w11 * w31 + w21 * w32 
w2' = w12 * w31 + w22 * w32
```

We get:

```
z3 = x1 * w1' + x2 * w2' 
```

Here's the diagram of this formula:

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/x1%203.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/x1%203.jpg)

Does it look familiar? A multilayer network is a single neuron network!

To fix this, let's reintroduce the sigmoid and see how the network changes:

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/x1%204.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/x1%204.jpg)

Write down the formula for this:

```
z1 = σ(x1 * w11 + x2 * w12)
z2 = σ(x1 * w21 + x2 * w22)
z3 = z1 * w31 + z2 * w32
```

We get:

```
z3 =  σ(x1 * w11 + x2 * w12) * w31 + σ(w21 * x1 + w22 * x2) * w32
```

Because of the sigmoids, we can't take *x₁* and *x₂* out of the brackets. This means we aren't dealing with a single neuron now. The sigmoids allow for making the network more complex.

## How Neural Networks are Trained

Similar to linear regression, the multilayer networks are trained with a gradient descent. There are parameters that are the weights of the neurons in each fully connected layer. And the training objective is to find such parameters that result in the minimal loss function.

How does a neural network change when we add neurons and layers? To find out, solve a few tasks on the [**TensorFlow Playground](http://playground.tensorflow.org)** website. This platform allows you to train small neural networks on model data with two features for classification tasks.

You can choose the dataset in the left part of the *TensorFlow Playground* interface. In the middle, you have your network structure, and on the right side, you have the training result output. You can control the model training process from the top panel and change the epoch value, learning rate, or activation function.

Look at [this network](http://playground.tensorflow.org/#activation=sigmoid&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.1&regularizationRate=0&noise=0&networkShape=4,4,4,4&seed=0.29689&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false). It has many layers and a sigmoid activation function. Try to train the network. It won't learn no matter what step value you set.

Let's figure out why. As the number of layers increase, the training gets less efficient. The more layers in the network, the less of a signal there's going to be from the input to the network's output. This is called a **vanishing signal** and is caused by the sigmoid, which converts large values into smaller ones over and over again.

To get rid of the problem, you can try another activation function, for example, **ReLU** (*Rectified Linear Unit*). Here's what it looks like:

[https://pictures.s3.yandex.net/resources/jpg_1586168291](https://pictures.s3.yandex.net/resources/jpg_1586168291)

And here's the ReLU formula:

[https://pictures.s3.yandex.net/resources/jpgagg_1586168313](https://pictures.s3.yandex.net/resources/jpgagg_1586168313)

ReLU brings all negative values to 0 and leaves positive values without changes.

Change the activation function from sigmoid to *ReLU* in [this network](http://playground.tensorflow.org/#activation=sigmoid&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.1&regularizationRate=0&noise=0&networkShape=4,4,4,4&seed=0.29689&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false). Make sure the neural network is now learning correctly. Because the activation function was changed, the surface area separating the points is polygonal. The shape depends on how the network weights were initialized.

## Fully Connected Neural Networks in Keras

Fully connected layers in *Keras* can be created by calling *Dense()*. To build a multilayer fully connected network, you need to add a fully connected layer several times. Let the first hidden layer have ten neurons, and second output layer will then have one neuron.

```xml
model = keras.models.Sequential()
model.add(keras.layers.Dense(units=10, input_dim=features_train.shape[1], 
                             activation='sigmoid'))
model.add(keras.layers.Dense(units=1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['acc'])

model.fit(features_train, target_train, epochs=10, verbose=2,
          validation_data=(features_valid, target_valid))
```

## Working with Images in Python

You already know that images are sets of numbers. If the image is black and white, then each pixel stores a number from 0 (black) to 255 (white).

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/log%201.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/log%201.jpg)

Let's open this image with the **PIL** (Python Imaging Library) library tools. We'll be able to work with it like with a *NumPy* array:

```python
import numpy as np
from PIL import Image

image = Image.open('image.png')
image_array = np.array(image)
print(image_array)
```

```python
[[255 255 255 255 237 217 239 255 255 255 255 255 255]
 [255 255 190  75  29  29  30  81 198 255 255 255 255]
 [255 147  30  29  29  29  29  29  31 160 255 255 255]
 [185  29  29  29  29  29  29  29  29  31 198 255 255]
 [ 61  29  29  29  29  29  29  29  29  29  74 255 255]
 [108 121 121 121 121 121 121 121 121 121 102 219 255]
 [250 255 255 255 255 255 255 255 255 255 238 107 168]
 [255 238 153 150 152 244 201 152 150 178 253 103 144]
 [248 243 121 108 114 225 184 130 112 154 235 103  62]
 [197 255 227 168 231 149 230 196 179 251 183  29  29]
 [105 255 255 219 195 191 184 195 235 255  91  29  29]
 [ 30 187 255 234 218 218 218 218 243 174  29  29  29]
 [ 29  38 180 255 255 255 255 255 169  35  29  29  29]
 [ 29  29  29  82 153 174 150  76  29  29  29  29  29]
 [ 29  29  29  29  29  29  29  29  29  29  29  29  29]]
```

We get a two-dimensional array.

Call the **`plt.imshow()`** (image show) to plot the image.

```xml
plt.imshow(image_array)
```

You can plot the image in black and white by adding `cmap='gray'` argument. To add a color bar to the image, you need to call `plt.colorbar()`.

```xml
plt.imshow(image_array, cmap='gray')
plt.colorbar()
```

Usually, neural networks learn better when they receive images in the range from 0 to 1 as input. To bring the scale [0, 255] to [0, 1], divide all the values of the two-dimensional array by 255.

```xml
image_array = image_array / 255.
```

## Color Images

Color images or **RGB images** consist of three channels: **red**, **green**, and **blue**. In fact, such images are three-dimensional arrays with cells containing integers in the range from 0 to 255.

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/grids.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/grids.jpg)

Three-dimensional arrays in *NumPy* work just like two-dimentional ones.

Compare how they are created:

```python
np.array([[0, 255],
          [255, 0]])
```

```python
np.array([[[0, 255, 0], [128, 0, 255]], 
          [[12, 89, 0], [5,  89, 245]]])
```

In a three-dimensional array obtained from an image, everything is almost the same. The first coordinate is the row ID, and the second one is the column ID. But here we also have a new third coordinate, it indicates the channel.

So, a three-dimensional array is just like a two-dimensional array from a black and white image. The only difference is that each pixel of such an array stores three numbers that represent the brightness of each of the three channels: red, green, and blue.

## Multiclass Classification

Let's explore **the multiclass classification** and see how it works. Such a classification implies that the observations belong to one of several classes as opposed to one of two classes.

Suppose we have three classes. Here's the logistic regression represented as a neural network:

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/x1%205.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/x1%205.jpg)

We get a fully connected network with the output layer containing not one, but three neurons. Each neuron is responsible for its own class. If the value at the *z1* output is a large positive number, then the network will set the observation to class "1."

How do we calculate the loss function? Remember the binary cross-entropy:

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97%204.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97%204.jpg)

If the target value is 1, then the correct answer probability is:

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/p.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/p.jpg)

If the target value is 0, the p value is:

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/pp.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/pp.jpg)

We have three classes, but it won't affect the loss function calculation. And it will be called **CE** (cross-entropy):

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97%205.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97%205.jpg)

In the formula, p is the correct answer probability returned by the network.

Where do we get the probability from? Sigmoids used to get it. What if we put a sigmoid after each neuron in the output layer?

```python
p_1 (first class probability) = σ(z_1)
p_2 (second class probability) = σ(z_2)
p_3 (third class probability) = σ(z_3)
```

All the probabilities are in the range from 0 to 1, but the sum of all three won't necessarily equal unity. If we assume that the observation belongs to only one class, we hope to get this:

```python
p_1 + p_2 + p_3 = 1
```

The activation function that suits this case is called **SoftMax**. It takes several outputs of the networks and returns probabilities that are all equal to one.

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/zz.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/zz.jpg)

Here's how we calculate the probabilities:

```python
p1 = SoftMax(z1) = e^z1 / (e^z1 + e^z2 + e^z3)
p2 = SoftMax(z2) = e^z2 / (e^z1 + e^z2 + e^z3)
p3 = SoftMax(z3) = e^z3 / (e^z1 + e^z2 + e^z3)
```

Now *p₁* varies in the range from 0 to 1.

Note that if z₁ is significantly greater than z₂ and *z₃*, then in formula `e^z1 / (e^z1 + e^z2 + e^z3)` the numerator is approximately equal to the denominator, that is *p₁*≈1.

If *z₁* is significantly less than *z₂* or *z₃*, then in formula `e^z1 / (e^z1 + e^z2 + e^z3)` the numerator is much less than the denominator, that is *p₁*≈0.

Now the probabilities are equal to one:

```python
p1 + p2 + p3 = SoftMax(z1) + SoftMax(z2) + SoftMax(z3) =

= e^z1 / (e^z1 + e^z2 + e^z3) + e^z2 / (e^z1 + e^z2 + e^z3) + e^z3 / (e^z1 + e^z2 + e^z3) =

= (e^z1 + e^z2 + e^z3) / (e^z1 + e^z2 + e^z3) = 1
```

Here's the diagram of our neural network with the *SoftMax* activation function:

![Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/x1%206.jpg](Chapter%20Summary%20Fully%20Connected%20Networks%203060dc67a37143c38c242187b2c6ff97/x1%206.jpg)

Why does the *SoftMax* block in the diagram depend on all the outputs from the network? Because we really need all the outputs to find all the probabilities.

If there are more than three classes, the number of the neurons in the output layer should be equal to the number of classes, and all outputs should be connected to *SoftMax*.

Probabilities from *SoftMax* at the training stage will go to cross-entropy, which will calculate the error. The loss function will be minimized using the gradient descent method. The only condition for the gradient descent to work is that the function has a derivative for all the parameters: weights and the bias of the neural network.

Let's see how the code changes. Here's the last layer initialization for binary classification:

```python
Dense(units=1, activation='sigmoid'))
```

And here's the initialization for multiclass classification:

```python
Dense(units=3, activation='softmax'))
```