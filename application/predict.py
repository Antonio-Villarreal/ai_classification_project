import tensorflow as tf
from PIL import Image
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np


def predict(model_path, image_path):
    model = keras.model.load_model(model_path)
    # model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    prediction = model.predict(img_array)
    return prediction

if __name__ == "__main__":
    model_path = 'model/face_classifier_model_20240225014658.keras'
    test_image = 'images/00001.jpg'
    print(predict(model_path, test_image))