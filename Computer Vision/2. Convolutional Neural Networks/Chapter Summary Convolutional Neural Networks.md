# Chapter Summary: Convolutional Neural Networks

## Convolution

Fully connected neural networks cannot work with large images. If there aren't enough neurons, the network won't be able to find all the connections, and if there are too many, the network will overtrain. Convolution is an easy fix for this.

In order to find the elements most important for classification, **convolution** applies the same operations to all pixels.

Let's start with **one-dimensional convolution**. Since there are no one-dimensional images, let's observe this operation in a sequence.

Let *w* be defined as weights, and *s* as a sequence.

Convolution (*с*) is done this way: the weights (*w*) move along the sequence (*s*), and the scalar product is calculated for each position on the sequence. The length *n* of the weights' vector is never longer than the length *m* of the sequence's vector; otherwise, there wouldn't be a position to which convolution could be applied.

![https://pictures.s3.yandex.net/resources/_2_1586705608.gif](https://pictures.s3.yandex.net/resources/_2_1586705608.gif)

Let's express a one-dimensional convolution operation with a formula:

![Chapter%20Summary%20Convolutional%20Neural%20Networks%20289a74bc0cfc44ab95dd95d4d63b5494/ck.jpg](Chapter%20Summary%20Convolutional%20Neural%20Networks%20289a74bc0cfc44ab95dd95d4d63b5494/ck.jpg)

Here, *t* is the index for calculating the scalar product, and *k* is any value from 0 to (m - n + 1).

The number (m - n + 1) is chosen so that the weights don't exceed the sequence.

Let's express a one-dimensional convolution in Python:

```python
def convolve(sequence, weights):
    convolution = np.zeros(len(sequence) - len(weights) + 1)
    for i in range(convolution.shape[0]):
        convolution[i] = np.sum(weights * sequence[i:i + len(weights)])
```

Now let's see how **two-dimensional convolution** (2D convolution) works. Let's take a two-dimensional image *s* with a size of *m×m* pixels and a weight matrix *w* of *n×n* pixels. This matrix is the **kernel** of the convolution.

The kernel moves inside the image from left to right, top to bottom. Its weights are multiplied by each pixel in every position. The products are summed up and recorded as the resulting pixels.

To see this in action, let's convolve the following matrices:

```python
s = [[1, 1, 1, 0, 0],
     [0, 1, 1, 1, 0],
     [0, 0, 1, 1, 1],
     [0, 0, 1, 1, 0],
     [0, 1, 1, 0, 0]]

w = [[1, 0, 1],
     [0, 1, 0],
     [1, 0, 1]]
```

Two-dimensional convolution can be expressed with the formula below:

![Chapter%20Summary%20Convolutional%20Neural%20Networks%20289a74bc0cfc44ab95dd95d4d63b5494/ck1.jpg](Chapter%20Summary%20Convolutional%20Neural%20Networks%20289a74bc0cfc44ab95dd95d4d63b5494/ck1.jpg)

You can find the contours of the image using convolution. Horizontal contours can be found using convolution with the following kernel:

```python
np.array([[-1, -2, -1],
          [ 0,  0,  0],
          [ 1,  2,  1]])
```

This kernel was discovered by American scientists Irwin Sobel and Gary Feldman and is meant specifically to find the contours of an image. It highlights contours better than the kernel from earlier in this lesson.

Use the following kernel to find vertical contours:

```python
np.array([[-1, 0, 1],
          [-2, 0, 2],
          [-1, 0, 1]])
```

## Convolutional Layers

Let's talk about convolutional layers and the role they play in convolutional neural networks (CNN). **Convolutional layers** apply a convolution operation to input images. They perform most of the computation within the network.

A convolutional layer consists of customizable and trainable **filters** (sets of weights), which are applied to the image. A filter is essentially a square matrix of size *K×K* pixels.

A third dimension, **depth**, is added to the filter if the input is a color image. In this case, the filter is no longer a matrix, but a tensor, or a multidimensional array.

Let's look at an example. Below you can see three color channels: red, blue, and green. A 3x3x3 filter (three pixels in width, height, and depth) moves through the input image in each channel, performing a convolution operation. It does not move through the third dimension, and each color has different weights. The resulting images are folded consequently into the end-result of the convolution.

![https://pictures.s3.yandex.net/resources/_2_1586706966.gif](https://pictures.s3.yandex.net/resources/_2_1586706966.gif)

A convolutional layer can have several filters, each returning a two-dimensional image which can be reconverted into a three-dimensional image. In the next convolutional layer, the depth of filters will be equal to the number of filters in the previous layer.

The asterisk (*) indicates a convolution operation.

![Chapter%20Summary%20Convolutional%20Neural%20Networks%20289a74bc0cfc44ab95dd95d4d63b5494/filter.jpg](Chapter%20Summary%20Convolutional%20Neural%20Networks%20289a74bc0cfc44ab95dd95d4d63b5494/filter.jpg)

Convolutional layers contain fewer parameters than fully connected layers. This makes them easier to train.

Let's take a look at the settings of a convolutional layer:

1. **Padding**. This setting adds zeros to the edges of the matrix (zero padding) so that the outermost pixels participate in the convolution at least as many times as the central pixels. This prevents the loss of important information. The added zeros also take part in the convolution, and the size of the padding determines the width of the zero padding.
    
    ![Chapter%20Summary%20Convolutional%20Neural%20Networks%20289a74bc0cfc44ab95dd95d4d63b5494/filter2.jpg](Chapter%20Summary%20Convolutional%20Neural%20Networks%20289a74bc0cfc44ab95dd95d4d63b5494/filter2.jpg)
    
2. **Striding**, or **Stride**. This setting shifts the filter by more than one pixel and generates a smaller output image.

Let's calculate the size of the output tensor for the convolutional layer. If the initial image has a size W×W×D, a K×K×D filter, padding (P), and step (S), then the new image size *W**'*** can be determined this way:

![Chapter%20Summary%20Convolutional%20Neural%20Networks%20289a74bc0cfc44ab95dd95d4d63b5494/w.jpg](Chapter%20Summary%20Convolutional%20Neural%20Networks%20289a74bc0cfc44ab95dd95d4d63b5494/w.jpg)

Check out [this visualizer on GitHub](https://ezyang.github.io/convolution-visualizer/index.html) to see how convolutions with different parameters behave.

## Convolutional Layers in Keras

Let's create a convolutional layer named **Conv2D.**

```python
keras.layers.Conv2D(filters, kernel_size, strides, padding, activation)
```

Here's what all the parameters mean:

- **Filters:** The number of filters, which corresponds to the size of the output tensor.
- **Kernel_size:** The spatial size of the filter *K.* Filter is a tensor with the size *K×K×D,* where *D* is equal to the depth of the input image.
- **Strides:** A stride determines how far the filter shifts over the input matrix. It's set to 1 by default.
- **Padding:** This parameter determines the width of the zero padding. There are two types of padding: *valid* and *same*. The default type of padding is *valid*, and is equal to zero. *Same* sets the size of the padding automatically so that the width and height of the output tensor is equal to the width and height of the input tensor.
- **Activation:** This function is applied immediately after the convolution. You can use the activation functions already familiar to you: `'relu'` and `'sigmoid'`. By default, this parameter is *None* (i.e. activation is disabled).

In order for the results of the convolutional layer to be compatible with a fully connected layer, connect a new layer named **Flatten**. It makes the multidimensional tensor one-dimensional.

For example, an input image with the size 32x32x3 goes through a convolutional layer, then a fully connected one, and a Flatten layer has to be placed between them:

```python
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense

model = Sequential()

# this tensor has a size of (None, 32, 32, 3)
# the first dimension defines different objects
# it's set to None because the size of the batch is unknown

model.add(Conv2D(filters=4, kernel_size=(3, 3), input_shape=(32, 32, 3)))

# this tensor has a size of (None, 30, 30, 4)

model.add(Flatten())

# this tensor has a size of (None, 3600)
# где 3600 = 30 * 30 * 4

model.add(Dense(...))
```

## LeNet Architecture

You can reduce the number of the model's parameters with **pooling** techniques. An example of pooling is the **Max Pooling** operation, which can be conducted this way:

1. The kernel size is determined (for example, 2x2).

2. The kernel starts moving left to right, top to bottom, and in each frame of four pixels there is a pixel with the maximum value.

3. The pixel with the maximum value remains, but the neighboring pixels disappear.

4. The result is a matrix formed only from the pixels with the maximum values.

![Chapter%20Summary%20Convolutional%20Neural%20Networks%20289a74bc0cfc44ab95dd95d4d63b5494/3.jpg](Chapter%20Summary%20Convolutional%20Neural%20Networks%20289a74bc0cfc44ab95dd95d4d63b5494/3.jpg)

In Keras, you can also use the **AveragePooling** operation. Here are the main differences between the techniques:

- *MaxPooling* returns the maximum pixel value from the pixel group within a channel. If the input image has a size of *W×W*, then the output image's size is *W/K*, where *K* is the kernel size.
- *AveragePooling* returns the average value of a group of pixels within a channel.

In Keras, the AveragePooling operation is written like this:

```python
keras.layers.AveragePooling2D(pool_size=(2, 2), strides=None, padding='valid', ...)
```

Let's go through each parameter:

- **Pool_size:** Pooling size. The larger it is, the more neighboring pixels involved.
- **Strides:** A stride determines how far the filter shifts over the input matrix. If *None* is specified, then the stride is equal to the pooling size.
- **Padding:** This parameter determines the width of the zero padding. The default type of padding is *valid*, which is equal to zero. *Same* sets the size of the padding automatically.

The parameters of *MaxPooling2D* are similar to these parameters.

We now have all the tools to create a popular architecture for classifying images with a size of 20-30 pixels, **LeNet**. The network is named after its creator, Yann André LeCun, the developer of the *DjVu* image compression technology and the head of Facebook's Artificial Intelligence Laboratory.

*LeNet* is structured as follows:

1. The network begins with two or three 5x5 layers alternating with *Average Pooling* with a size of 2x2. They gradually reduce the spatial resolution and collect all the information in the image into a small matrix of about 5 pixels.
2. The number of filters increases from layer to layer to prevent the loss of important information.
3. There are one or two fully connected layers at the end of the network. They collect all the features and classify them.

Here's how we create LeNet in Keras:

```python
model = Sequential()

model.add(Conv2D(6, (5, 5), padding='same', activation='tanh',
                 input_shape=(28, 28, 1)))
model.add(AvgPool2D(pool_size=(2, 2)))

model.add(Conv2D(16, (5, 5), padding='valid', activation='tanh'))
model.add(AvgPool2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(120, activation='tanh'))

model.add(Dense(84, activation='tanh'))

model.add(Dense(10, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', optimizer='sgd', metrics=['acc'])
model.summary()
```

## The Adam Algorithm

Stochastic gradient descent (*SGD*) isn't the most effective algorithm for training a neural network. If the stride is too small, the training may take too long. If it's too large, it might not manage the minimum required training. The **Adam** algorithm makes stride selection automatic. It selects different parameters for different neurons, which speeds up model training.

To understand how this algorithm works, consider this [visualization](https://bl.ocks.org/EmilienDupont/raw/aaf429be5705b219aaaf8d691e27ca87/) created by Emilien Dupont from Oxford University. It displays four algorithms: SGD **on the left, the *Adam* algorithm on the right, and between them there are two algorithms similar to *Adam* (we won't be discussing them in-depth). Out of the four of them, *Adam* is the fastest way to find the minimum.

Let's write the *Adam algorithm* into *Keras*:

```python
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', 
              metrics=['acc'])
```

Let's set the algorithm class to configure the hyperparameters:

```python
from tensorflow.keras.optimizers import Adam
optimizer = Adam()

model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', 
              metrics=['acc'])The main configurable hyperparameter in the *Adam* algorithm is the learning rate. This is the part of the gradient descent from where the algorithm starts. It's written as follows:
```

```python
optimizer = Adam(lr=0.01)
```

The default learning rate is 0.001. Reducing it can sometimes slow down learning, but that improves the overall quality of the model.

## Data Generators

Arrays are stored in the RAM, not on the computer's hard drive. Now what if you needed to make an array of terabytes of pictures? It's hard enough to even imagine such a thing! RAM resources are limited, after all.

To deal with such a huge amount of images, you need to implement dynamic data loading.

The Keras library has a convenient tool, **[ImageDataGenerator](https://keras.io/preprocessing/image/)**:

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator
```

The ImageDataGenerator class forms batches with images and class labels based on the photos in the folders. Let's put it to the test:

```python
# от англ. data generator
datagen = ImageDataGenerator()
```

To extract data from a folder, call the **flow_from_directory()** function:

```python
datagen_flow = datagen.flow_from_directory(
    # the folder with the dataset
    '/dataset/',
    # the target image size
    target_size=(150, 150), 
    # the batch size
    batch_size=16,
    # class mode
    class_mode='sparse',
    # set a random number generator
    seed=54321)
```

```
Found 1683 images belonging to 12 classes.
```

The data generator found 12 classes (folders) and a total of 1683 images.

Let's go through the arguments:

- `target_size=(150, 150)` — an argument with the target width and height of the image. The folders may contain images of different sizes, but the neural networks need all images to have the same dimensions.
- `batch_size=16` — the number of images in the batches. The more images there are, the more effective the model's training will be. Too many pictures won't fit in the GPU's memory, so 16 is the perfect starting value.
- `сlass_mode='sparse'` — an argument that indicates the class label output mode. `sparse` means that the labels will correspond to the number of the folder.
    
    You can find out how the class numbers relate to folder names this way:
    
    ```python
    # class indices
    print(datagen_flow.class_indices)
    ```
    

Calling the `datagen.flow_from_directory(...)` method will return an object from which "picture-label" pairs can be obtained by using the *next()* function:

```python
features, target = next(datagen_flow)

print(features.shape)
```

The result is a four-dimensional tensor with sixteen 150x150 images with three color channels.

To train the model on this data, let's pass the object `datagen_flow` to the *fit()* method*.* The epoch shouldn't be infinitely long. To limit the training time, let's specify the number of dataset batches in the `steps_per_epoch` parameter:

```python
model.fit(datagen_flow, steps_per_epoch=len(datagen_flow))
```

The `fit()` method has to contain both training and validation sets. To do this, create two data generators for each set.

```python
# indicate that the validation set contains 
# 25% random objects
datagen = ImageDataGenerator(validation_split=0.25)

train_datagen_flow = datagen.flow_from_directory(
    '/datasets/fruits_small/',
    target_size=(150, 150),
    batch_size=16,
    class_mode='sparse',
    # indicate that this is the data generator for the training set
    subset='training',
    seed=54321)

val_datagen_flow = datagen.flow_from_directory(
    '/datasets/fruits_small/',
    target_size=(150, 150),
    batch_size=16,
    class_mode='sparse',
    # indicate that this is the data generator for the validation set
    subset='validation',
    seed=54321)
```

Training is now initiated like this:

```python
model.fit(train_datagen_flow,
          validation_data=val_datagen_flow,
          steps_per_epoch=len(train_datagen_flow),
          validation_steps=len(val_datagen_flow))
```

## Image Data Augmentations

If there are too few training samples, the network may overtrain. Augmentation is used to expand datasets and avoid this problem. **Augmentation** is used to artificially expand a dataset by transforming the existing images. The changes are only applied to training sets, while test and validation sets remain the same.

Augmentation transforms the original image while still preserving its core features. For example, the image can be rotated or reflected.

There are several types of augmentation:

- Rotation
- Reflection
- Changing brightness and contrast
- Stretching and compression
- Blurring and sharpening
- Adding noise

You can apply more than one type of augmentation to a single image.

Augmentation can sometimes cause problems. For example, the image class can change, or the end result might end up resembling an impressionist painting because of all the alterations. This affects the quality of the model.

You can avoid these problems if you follow these recommendations:

- Do not apply augmentation on test and validation sets so as not to distort metric values.
- Add augmentations gradually, one at a time, and keep an eye on the quality metric in the validation set.
- Always leave some images in the dataset unchanged.

## Augmentations in Keras

There are many ways to add image augmentations in *ImageDataGenerator.* They're disabled by default. Let's apply a vertical flip:

```python
datagen = ImageDataGenerator(validation_split=0.25,
                             rescale=1./255,
                             vertical_flip=True)
```

Different generators have to be created for the training and validation sets:

```python
train_datagen = ImageDataGenerator(
    validation_split=0.25,
    rescale=1./255,
    horizontal_flip=True)

validation_datagen = ImageDataGenerator(
    validation_split=0.25,
    rescale=1./255)

train_datagen_flow = train_datagen.flow_from_directory(
    '/dataset/',
    target_size=(150, 150),
    batch_size=16,
    class_mode='sparse',
    subset='training',
    seed=54321)

val_datagen_flow = validation_datagen.flow_from_directory(
    '/dataset/',
    target_size=(150, 150),
    batch_size=16,
    class_mode='sparse',
    subset='validation',
    seed=54321)
```

Set the objects *train_datagen_flow* and *val_datagen_flow* to the same `seed` value to prevent the training and validation sets from sharing common elements.

## ResNet in Keras

Import *ResNet50* from Keras. (50 indicates the number of layers in the network.)

```python
from tensorflow.keras.applications.resnet import ResNet50

model = ResNet50(input_shape=None,
				         classes=1000,
				         include_top=True,
			           weights='imagenet')
```

Let's go through the arguments:

- `input_shape` — the size of the input image. For example: `(640, 480, 3)`.
- `classes=1000` — the number of neurons in the last fully connected layer where classification takes place.
- `weights='imagenet'` — the initialization of weights. *ImageNet* is the name of a large image database that was used to train the network to sort pictures into 1000 classes. If you start training the network on *ImageNet,* and then continue with your task, the result will be much better than if you'd just trained it from scratch. To initialize the weights at random, write `weights=None`.
- `include_top=True` — indicates that there are two layers (*GlobalAveragePooling2D* and *Dense*) at the end of ResNet. If you set it to *False*, these layers will be missing.

Let's go through the above-mentioned layers:

1. *GlobalAveragePooling2D* acts as a window to the entire tensor. Like *AveragePooling2D,* it returns the average value from a group of pixels inside a channel. *GlobalAveragePooling2D* is used to average the information throughout the image in order to get a pixel with a large number of channels (for example, 512 for ResNet50).

2. *Dense* is the fully connected layer responsible for classification.

Let's learn how to use a network that's been pre-trained on *ImageNet*. To adapt *ResNet50* to our task, let's remove the top and rebuild it:

```python
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.models import Sequential

backbone = ResNet50(input_shape=(150, 150, 3),
                    weights='imagenet', 
                    include_top=False)

model = Sequential()
model.add(backbone)
model.add(GlobalAveragePooling2D())
model.add(Dense(12, activation='softmax'))
```

The `backbone` is what's left of ResNet50.

Now here's a trick: let's say there's a very small dataset that only contains 100 pictures and two classes. If you train *ResNet50* on this dataset, it is guaranteed to overtrain because it has too many parameters (about 23 million)! The network will end up getting perfectly accurate predictions on the training set, but it'll get random ones on the test set.

To avoid this, we will "freeze" a part of the network: some layers will be left with *ImageNet* weights and won't be trained with gradient descent. Let's train only one or two fully connected layers at the top of the network. This way, the number of parameters in the network will be reduced, but the architecture itself will be preserved.

Let's freeze the network like this:

```python
backbone = ResNet50(input_shape=(150, 150, 3),
                    weights='imagenet', 
                    include_top=False)

# freeze ResNet50 with the top removed
backbone.trainable = False

model = Sequential()
model.add(backbone)
model.add(GlobalAveragePooling2D())
model.add(Dense(12, activation='softmax'))
```

We didn't freeze the fully connected layer above *backbone* so that the network is able to learn.

Freezing allows you to avoid overtraining and increase the network's learning rate (the gradient descent won't need to count derivatives for frozen layers).