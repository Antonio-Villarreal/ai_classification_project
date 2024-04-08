from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import load_model

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

app = Flask(__name__)

# Directory to save uploaded images
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load the image classification model
model_image_path = 'image_model.h5'  # Path to the image classification model
model_image = load_model(model_image_path)

# Load the face detection model
model_face_path = 'face_model.h5'  # Path to the face detection model
model_face = load_model(model_face_path)

# Define hyperparameters for image classification
hyperparams_image = {
    'IMG_SIZE': 224  # Example value, adjust as per your model requirements
}

# Define hyperparameters for face detection
hyperparams_face = {
    'IMG_SIZE': 224  # Example value, adjust as per your model requirements
}

# Image preprocessing function for image classification
def preprocess_image_image(image_path):
    img = image.load_img(image_path, target_size=(hyperparams_image['IMG_SIZE'], hyperparams_image['IMG_SIZE']))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions to match model input shape
    return img_array

# Image preprocessing function for face detection
def preprocess_image_face(image_path):
    img = image.load_img(image_path, target_size=(hyperparams_face['IMG_SIZE'], hyperparams_face['IMG_SIZE']))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions to match model input shape
    return img_array

# Route for image classification
@app.route('/upload_image', methods=['POST'])
def upload_file_image():
    if 'file' not in request.files:
        return jsonify(error="No file part"), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify(error="No selected file"), 400
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Preprocess the image for image classification
        img_array = preprocess_image_image(file_path)
        
        # Make predictions for image classification
        predictions = model_image.predict(img_array)
        prediction_score = float(predictions[0][0])  # Convert prediction score to float
        predicted_class = 'Real' if prediction_score > 0.5 else 'AI'
        
        # Return response with predicted class and score for image classification
        return jsonify(message=predicted_class, score=prediction_score)

# Route for face detection
@app.route('/upload_face', methods=['POST'])
def upload_file_face():
    if 'file' not in request.files:
        return jsonify(error="No file part"), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify(error="No selected file"), 400
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Preprocess the image for face detection
        img_array = preprocess_image_face(file_path)
        
        # Make predictions for face detection
        predictions = model_face.predict(img_array)
        prediction_score = float(predictions[0][0])  # Convert prediction score to float
        predicted_class = 'Real' if prediction_score > 0.5 else 'AI'
        
        # Return response with predicted class and score for face detection
        return jsonify(message=predicted_class, score=prediction_score)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
