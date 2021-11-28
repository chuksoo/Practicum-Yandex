from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
import numpy as np


def load_train(path):
    features_train = np.load(path + 'train_features.npy')
    target_train = np.load(path + 'train_target.npy')
    features_train = (
        features_train.reshape(features_train.shape[0], 28 * 28) / 255.0
    )
    return features_train, target_train


def create_model(input_shape):
    model = Sequential()
    model.add(Dense(100, input_shape=input_shape, activation='relu'))  # first hidden layer with 100 neutrons
    model.add(Dense(100, activation='softmax'))  # second hidden layer with 100 neutrons
    # model.add(Dense(10, activation='softmax'))  # third hidden layer with 5 neutrons
    model.compile(
        optimizer='sgd',
        loss='sparse_categorical_crossentropy',
        metrics=['acc'],
    )
    return model


def train_model(
    model,
    train_data,
    test_data,
    batch_size=32,
    epochs=20,
    steps_per_epoch=None,
    validation_steps=None
):

    features_train, target_train = train_data
    features_test, target_test = test_data
    model.fit(
        features_train,
        target_train,
        validation_data=(features_test, target_test),
        batch_size=batch_size,
        epochs=epochs,
        steps_per_epoch=steps_per_epoch,
        validation_steps=validation_steps,
        verbose=2,
        shuffle=True,
    )
    return model
