from tensorflow.keras.datasets import fashion_mnist
import numpy as np
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense, AvgPool2D
from tensorflow.keras.optimizers import Adam


def load_train(path):
    features_train = np.load('/datasets/fashion_mnist/train_features.npy')
    target_train = np.load('/datasets/fashion_mnist/train_target.npy')
    features_test = np.load('/datasets/fashion_mnist/test_features.npy')
    target_test = np.load('/datasets/fashion_mnist/test_target.npy')

    features_train = features_train.reshape(-1, 28, 28, 1) / 255.0
    features_test = features_test.reshape(-1, 28, 28, 1) / 255.0
    return features_train, target_train

def create_model(input_shape):
    model = Sequential()
    # first hidden layer with 100 neutrons
    model.add(
        Conv2D(
            filters=4,
            kernel_size=(3, 3),
            padding='same',
            activation="relu",
            input_shape=(28, 28, 1),
        )
    )
    model.add(AvgPool2D(pool_size=(2, 2)))
    #second layer
    model.add(Conv2D(16, (5, 5), padding='valid', activation='relu'))
    model.add(AvgPool2D(pool_size=(2, 2)))
    
    model.add(Flatten())
    model.add(Dense(100, activation='relu'))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(units=10, activation='softmax'))
    # set algorithm class to configure hyperparameters
    optimizer = Adam(lr=0.01)
    model.compile(
        optimizer= optimizer,
        loss='sparse_categorical_crossentropy',
        metrics=['acc'],
    )
    model.summary()
    return model

def train_model(
    model,
    train_data,
    test_data,
    batch_size=None,
    epochs=20,
    steps_per_epoch=None,
    validation_steps=None
):

    features_train, target_train = train_data
    features_test, target_test = test_data
    model.fit(
        features_train,
        target_train,
        epochs=300,
        verbose=1,
        steps_per_epoch=1,
        batch_size=500,
    )
    return model


