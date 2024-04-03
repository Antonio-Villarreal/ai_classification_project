# Standard library imports
import json
import os
import pickle
import random
from datetime import datetime

# Third-party library imports
import matplotlib.pyplot as plt
import tensorflow as tf
from PIL import Image
from tensorflow import keras
from tensorflow.keras import layers, models, optimizers, regularizers
from keras.layers import BatchNormalization
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras_tuner.engine.hyperparameters import HyperParameters

hyperparams = {
    'BATCH_SIZE': 32,
    'IMG_SIZE': 224,
    'EPOCHS': 10,
    'MODEL': 'CNN'
}


def check_gpu():
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        print("GPU is available:")
        for gpu in gpus:
            print(gpu)
    else:
        print("No GPU is available.")


def save_model_keras(model, model_file):
    model_directory = os.path.join('model', model_file + '.keras')
    model.save(model_directory)
    print(f"Model saved to {model_file}.keras")
    return model_file + '.keras'


def save_model_h5(model, model_file):
    model_directory = os.path.join('model', model_file + '.h5')
    model.save(model_directory)
    print(f"Model saved to {model_file}.h5")
    return model_file + '.h5'


def save_results(model, training_results, evaluation_results, hyperparameters, save_h5: bool = False):
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    model_filename = f"face_classifier_model_{timestamp}"
    json_filename = f"face_classifier_training_{timestamp}.json"

    if save_h5:
        file = save_model_h5(model, model_filename)
    else:
        file = save_model_keras(model, model_filename)

    data = {
        'model_filename': file,
        'training_results': training_results,
        'evaluation_results': evaluation_results,
        'hyperparams': hyperparameters
    }

    json_directory = os.path.join('json', json_filename)
    with open(json_directory, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"JSON file '{json_filename}' created successfully.")


if __name__ == "__main__":
    check_gpu()
