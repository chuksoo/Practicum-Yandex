# Takeaway sheet: Fully Connected Networks

## Practice

```python
# Training linear regression in Keras
# import Keras
from tensorflow import keras

# create the model
model = keras.models.Sequential()
# indicate how the neural network is arranged
# units - the number of neurons in the layer
# input_dim - the number of inputs in the layer
model.add(keras.layers.Dense(units=1, input_dim=features.shape[1]))
# indicate how the neural network is trained
model.compile(loss='mean_squared_error', optimizer='sgd')

# train the model
model.fit(features, target)
```

```python
# Training logistic regression in Keras
# import Keras
from tensorflow import keras

# create the model
model = keras.models.Sequential()
# indicate how the neural network is arranged
# units - the number of neurons in the layer
# input_dim - the number of inputs in the layer
# activation - activation function
model.add(keras.layers.Dense(units=1, input_dim=features_train.shape[1], 
														activation='sigmoid'))
# indicate how the neural network is trained
model.compile(loss='binary_crossentropy', optimizer='sgd')

# train the model
model.fit(features, target)
```

```python
# Training fully connected neural networks in Keras
# import Keras
from tensorflow import keras

# create the model
model = keras.models.Sequential()
# indicate how the neural network is arranged 
# We have two layers: the first one has 10 neurons, the second one has one neuron
# units - the number of neurons in the layer
# input_dim - the number of inputs in the layer
# activation - activation function
model.add(keras.layers.Dense(units=10, input_dim=features_train.shape[1], 
                             activation='sigmoid'))
model.add(keras.layers.Dense(units=1, activation='sigmoid'))

# indicate how the neural network is trained
model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['acc'])

# train the model
model.fit(features, target)
```

```python
# Working with Images in Python
import numpy as np
from PIL import Image

# Importing the image
image = Image.open('image.png')
image_array = np.array(image)
print(image_array)

# Plotting the image
plt.imshow(image_array)

# Plotting the black and white image 
plt.imshow(image_array, cmap='gray')

# Adding the color bar to the image
plt.colorbar()
```