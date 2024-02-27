from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import pickle
from keras.models import load_model
import predict

app = Flask(__name__)

# Directory to save uploaded images
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def process_image(model_path, image_path):
    return predict.predict(model_path, image_path)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify(error="No file part"), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify(error="No selected file"), 400
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        path_to_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(path_to_dir, "face_classifier_model_20240226000456.h5")
        file.save(file_path)
        # Process the image and get a response
        response = process_image(model_path, file_path)
        return jsonify(message=response)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
