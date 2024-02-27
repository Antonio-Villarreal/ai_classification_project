import streamlit as st
import requests

# URL of the Flask backend
FLASK_BACKEND_URL = 'http://localhost:5001/upload'

st.title('Image Processing App')

# File uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # Show the uploaded image
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    st.write("Processing...")
    
    # Send the file to the Flask backend for processing
    files = {'file': (uploaded_file.name, uploaded_file, 'multipart/form-data')}
    response = requests.post(FLASK_BACKEND_URL, files=files)
    
    if response.status_code == 200:
        # Display the response from the backend
        result = response.json()['message']
        st.write(result)
    else:
        st.write("Failed to process the image.")

