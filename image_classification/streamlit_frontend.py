import streamlit as st
import requests

# URL of the Flask backend for image classification
FLASK_IMAGE_BACKEND_URL = 'http://localhost:5001/upload_image'

# URL of the Flask backend for face detection
FLASK_FACE_BACKEND_URL = 'http://localhost:5001/upload_face'

st.title('AI Classification App')

# Image AI Classification
st.header("Image AI Classification")

# File uploader widget for image classification
uploaded_image = st.file_uploader("Choose an image for classification...", type=["jpg", "jpeg", "png"])
if uploaded_image is not None:
    # Show the uploaded image
    st.image(uploaded_image, caption='Uploaded Image.', use_column_width=True)
    st.write("Processing Image...")

    # Send the image file to the Flask backend for image classification
    files = {'file': (uploaded_image.name, uploaded_image, 'multipart/form-data')}
    response_image = requests.post(FLASK_IMAGE_BACKEND_URL, files=files)

    if response_image.status_code == 200:
        # Display the response from the backend for image classification
        result_image = response_image.json()
        predicted_class_image = result_image['message']
        prediction_score_image = result_image.get('score', None)
        if prediction_score_image is not None:
            st.write(f"Predicted Class: {predicted_class_image}")
            st.write(f"Prediction Score: {prediction_score_image:.2f}")
        else:
            st.write("Failed to get prediction score for image.")
    else:
        st.write("Failed to process the image for image AI classification.")

# Face AI Classification
st.header("Face AI Classification")

# File uploader widget for face detection
uploaded_face = st.file_uploader("Choose an image for face detection...", type=["jpg", "jpeg", "png"])
if uploaded_face is not None:
    # Show the uploaded image
    st.image(uploaded_face, caption='Uploaded Image.', use_column_width=True)
    st.write("Processing Face Image...")

    # Send the image file to the Flask backend for face detection
    files = {'file': (uploaded_face.name, uploaded_face, 'multipart/form-data')}
    response_face = requests.post(FLASK_FACE_BACKEND_URL, files=files)

    if response_face.status_code == 200:
        # Display the response from the backend for face detection
        result_face = response_face.json()
        predicted_class_face = result_face['message']
        prediction_score_face = result_face.get('score', None)
        if prediction_score_face is not None:
            st.write(f"Predicted Class: {predicted_class_face}")
            st.write(f"Prediction Score: {prediction_score_face:.2f}")
        else:
            st.write("Failed to get prediction score for face.")
    else:
        st.write("Failed to process the image for face AI classification.")
