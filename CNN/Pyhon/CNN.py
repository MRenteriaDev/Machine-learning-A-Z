# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 17:26:45 2021

@author: mrent
"""

## Redes neuronales convolucionales


# Parte 1 - Creación de la CNN
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# Inicializar la CNN
classifier = Sequential()


# Paso 1 - Convolución
classifier.add(Conv2D(filters =32, kernel_size = (3, 3), 
                      input_shape = (64,64,3), activation="relu"))

# Paso - Max Pooling
classifier.add(MaxPooling2D(pool_size=(2,2)))

# Paso 3 - Flattening
classifier.add(Flatten())

# Paso 4 - Full Connection
classifier.add(Dense(units = 128, activation="relu"))
classifier.add(Dense(units = 1, activation="sigmoid"))

# Compilar la Red Neuronal de Convolución
classifier.compile(optimizer = 'adam', loss="binary_crossentropy", metrics=["accuracy"])

# Parte 2 - Ajustar las imágenes a la CNN para entrenar
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True
    )

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
        './dataset/training_set',
        target_size=(64,64),
        batch_size=32,
        class_mode='binary'
    )

testing_dataset = test_datagen.flow_from_directory(
        './dataset/test_set',
        target_size=(64,64),
        batch_size=32,
        class_mode="binary"
    )

classifier.fit_generator(
        training_set,
        steps_per_epoch=2000,
        epochs=50,
        validation_data=testing_dataset,
        validation_steps=800)












