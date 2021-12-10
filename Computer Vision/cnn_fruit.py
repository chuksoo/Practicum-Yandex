import numpy as np
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense, AveragePooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam


def load_train(path):
    datagen = ImageDataGenerator(
        horizontal_flip=True, vertical_flip=True, rescale=1/255)

    train_datagen_flow = datagen.flow_from_directory(
        path,
        target_size=(150, 150),
        batch_size=16,
        class_mode='sparse',
        seed=12345)

    return train_datagen_flow


def create_model(input_shape):

    model = Sequential()

    model.add(
        Conv2D(
            filters=6,
            kernel_size=(3, 3),
            activation='relu',
            input_shape=(150, 150, 3),
        )
    )
    model.add(AveragePooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dense(12, activation='softmax'))
    optimizer = Adam(lr=0.001)
    model.compile(optimizer=optimizer,
                  loss='sparse_categorical_crossentropy', metrics=['acc']
                  )

    return model


def train_model(
    model,
    train_data,
    test_data,
    batch_size=None,
    epochs=10,
    steps_per_epoch=None,
    validation_steps=None,
):

    model.fit(
        train_data,
        validation_data=test_data,
        epochs=epochs,
        verbose=2,
        #steps_per_epoch=7,
        batch_size=batch_size,
        steps_per_epoch=steps_per_epoch,
        validation_steps=validation_steps,
    )

    return model


