# AI Classification Project

## Project Description

With generative machine learning models such as Dall-E and Chat-GPT becoming better and more realistic, it is becoming difficult to determine what exactly has been AI-generated. Distinguishing between AI-generated and real images has become increasingly challenging. Our team proposes a project to train a model that will determine whether an image is real or AI-generated. By taking a large dataset we found on Kaggle, we hope to train our image classification model to deploy an application where users can submit an image to identify whether the image is real or AI-generated. We will utilize Streamlit and Flask to help deploy this application for an easy-to-use user interface.

Through this project, we aim to empower users with the ability to navigate through different images, distinguishing between AI algorithms and human creation. This project not only serves as an exploration of AI capabilities but also as a tool for users to enhance their understanding and awareness of AI-generated content.

For more details, please refer to the provided links.

## Training
### Run Training Script (Windows, Linux, Mac)
The actual datasets are at least 80,000 images each so a subsection of one of the datasets has been provided to show that the train script works (Face Classifier Training).
1. `cd training/ai_face_classifier`
2. Activate Conda Environment or Virtual Environment
3. Install `requirements.txt`
4. Run `train.py`

## Web Application
### Run with Docker (Windows, Linux, Mac)
1. Install Docker or Docker Desktop (Open Docker Desktop for Windows)
2. Clone Repository
3. Give Permissions for Bash Scripts (linux - `chmod +x ./docker_run.sh ./docker_stop.sh`)
4. Run `./docker_run.sh`

### Run with Local Build (Linux)
1. Install Python3.10
2. Clone Repository
3. Give Permissions for Bash Script (linux - `chmod +x ./build.sh`)
4. Run `./build.sh`

## Manual Model Download
Either build process can have issues with downloading the .h5 model files. Below are the steps to download them manually.
1. Open the OneDrive link below.
2. Download `image_model.h5` and  `face_model.h5`.
3. Copy two files into /application directory.
4. Rerun local or docker build process.

## Links

### Classifier Models

- **Face and Image Classifier Models:** [OneDrive Link](https://uflorida-my.sharepoint.com/:f:/g/personal/a_villarreal1_ufl_edu/Eg0w-ssmdKtCspEwaFvHlzABQ4Yy8VpkbhzV2S-udj6ClQ?e=8zTvaQ)

### Datasets

- **Face Classifier Dataset:** [Kaggle Dataset](https://www.kaggle.com/datasets/xhlulu/140k-real-and-fake-faces/data)
- **Image Classifier Dataset:** [Kaggle Dataset](https://www.kaggle.com/datasets/sattyam96/realifake)

### Additional Resources

- **Midpoint Presentation:** [YouTube Link](https://youtu.be/npR-YJRWkTA?si=t-RTi0n4hXT8kVhW)

### Helpful Links

- **GPU Enabled TensorFlow:** [Link](https://www.tensorflow.org/install/pip#windows-native_1)


