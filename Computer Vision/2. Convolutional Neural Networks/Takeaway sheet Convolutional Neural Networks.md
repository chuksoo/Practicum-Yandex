# Takeaway sheet: Convolutional Neural Networks

### Practice

```python
# one-dimensional convolution

def convolve(sequence, weights):
    convolution = np.zeros(len(sequence) - len(weights) + 1)
    for i in range(convolution.shape[0]):
        convolution[i] = np.sum(weights * sequence[i:i + len(weights)])
```

```python
# two-dimensional convolutional layer in keras
# filters - the number of filters which corresponds to the size of the output tensor.
# kernel_size - the spatial size of the filter *K.*
# strides - determines how far the filter shifts over the input matrix. (Set to 1 by default.)
# padding - determines the width of the zero padding. 
# There are two types of padding: valid **and same*. 
#* The default type of padding is — valid, and is equal to zero. 
# Same sets the size of the padding automatically,
# so that the width and height of the output tensor is equal to the width and height of the input tensor. 
# activation - activation function which is applied immediately after the convolution. 

keras.layers.Conv2D(filters, kernel_size, strides, padding, activation)
```

```python
# Layer FLatten that makes the multidimensional tensor one-dimensional

keras.layers.Flatten()
```

```python
# Pooling layer
# pool_size — pooling size.
# strides — determines how far the filter shifts over the input matrix. If *None* is specified, then the stride is equal to the pooling size.
# padding — determines the width of the zero padding. 

keras.layers.MaxPooling2D(pool_size=(2, 2), strides=None, padding='valid', ...)
keras.layers.AveragePooling2D(pool_size=(2, 2), strides=None, padding='valid', ...)
```

```python
# Data generator

from tensorflow.keras.preprocessing.image import ImageDataGenerator
datagen = ImageDataGenerator()

# extract data from a folder
datagen_flow = datagen.flow_from_directory(
    # the folder with the dataset
    '/dataset/',
    # the target image size
    target_size=(150, 150), 
    # the batch size
    batch_size=16,
    # class mode
    class_mode='sparse',
		# indicate that this is the data generator for the training set (if necessary)
    subset='training', 
		# indicate that this is the data generator for the validation set (if necessary)
    subset='validation',
    # set a random number generator
    seed=12345)

# obtain the next batch
features, target = next(datagen_flow)

# training the model using data generators
# using full dataset
model.fit(datagen_flow, steps_per_epoch=len(datagen_flow))

# with only training and validation sets 
model.fit(train_datagen_flow,
          validation_data=val_datagen_flow,
          steps_per_epoch=len(train_datagen_flow),
          validation_steps=len(val_datagen_flow))
```

```python
# Adding augmentation in data generators
# horizontal_flip - horizontal rotation
# vertical_flip - vertical rotation

datagen = ImageDataGenerator(validation_split=0.25,
                             rescale=1./255,
                             horizontal_flip=True,
                             vertical_flip=True)
```

```python
# Implementing ResNet architecture
# input_shape — the size of the input image
# classes=1000 — the number of neurons in the last fully connected layer where classification takes place
# weights='imagenet' — the initialization of weights 
# ImageNet — the name of a large image database which
# was used to train the network to sort pictures into 1000 classes 
# To initialize the weights at random, write weights=None.
# include_top=True — indicates that there are two layers at the end of ResNet: 
# GlobalAveragePooling2D and Dense. If you set it to False, these layers will be missing.

from tensorflow.keras.applications.resnet import ResNet50

model = ResNet50(input_shape=None,
				         classes=1000,
				         include_top=True,
			           weights='imagenet')
```

```python
# Creating your own network based on ResNet50

backbone = ResNet50(input_shape=(150, 150, 3),
                    weights='imagenet', 
                    include_top=False)

# freeze ResNet50 with the top removed (optional)
backbone.trainable = False

model = Sequential()
model.add(backbone)
model.add(GlobalAveragePooling2D())
model.add(Dense(12, activation='softmax'))
```

### Theory

**Сonvolution*:*** A function that applies the same operations to all pixels to extract image elements that are important for classification.

**Convolution neural network:** A class of neural networks that use convolutional layers. They perform most of the computation within the network.

**Convolution layer:** A layer where the convolution operation is applied to input images.

**Filter:** A component of the convolutional layer, a set of weights that are applied to the image.

**Padding:** This setting adds zeros to the edges of the matrix (zero padding) so that the outermost pixels participate in the convolution at least as many times as the central pixels.

**Striding**, or **Stride:** This setting shifts the filter by more than one pixel and generates a smaller output image.

**Pooling:** Compacting a group of pixels to one pixel using some transformation: for example, calculating the maximum or arithmetic mean.

**Augmentation*:*** A technique which is used to artificially expand a dataset by transforming existing images. The changes are only applied to training sets, while test and validation sets remain the same. Augmentation transforms the original image while still preserving its core features.