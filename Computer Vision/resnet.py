import numpy as np
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.models import Sequential
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

    backbone = ResNet50(
        input_shape=(150, 150, 3), weights='imagenet', include_top=False
    )

    model = Sequential()
    model.add(backbone)
    model.add(GlobalAveragePooling2D())
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
    epochs=3,
    steps_per_epoch=None,
    validation_steps=None,
):

    model.fit(
        train_data,
        validation_data=test_data,
        epochs=10,
        verbose=2,
        #steps_per_epoch=7,
        batch_size=batch_size,
        steps_per_epoch=steps_per_epoch,
        validation_steps=validation_steps,
    )

    return model
