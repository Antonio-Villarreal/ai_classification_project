import os
import gdown
from onedrivedownloader import download
import json


def download_from_google_drive(url, output_file):
    gdown.download(url, output_file, quiet=False)


if __name__ == "__main__":
    json_file_path = os.path.join("models.json")
    with open(json_file_path, "r") as json_file:
        model_info = json.load(json_file)

    # Download image_model.h5 if it doesn't exist
    if not os.path.exists("image_model.h5"):
        # Attempt Google Drive Download
        image_model_id = model_info["image_model"]['google_drive_id']
        image_model_url = f"https://drive.google.com/uc?id={image_model_id}"
        image_model_destination = os.path.join("image_model.h5")
        try:
            download_from_google_drive(image_model_url, image_model_destination)
        except Exception as e:
            print("Google Drive download failed. Attempting OneDrive download.")
            # Attempt OneDrive Download
            try:
                download(model_info["image_model"]['onedrive_url'], image_model_destination)
            except Exception as e:
                print("OneDrive download failed:", e)

    # Download face_model.h5 if it doesn't exist
    if not os.path.exists("face_model.h5"):
        # Attempt Google Drive Download
        face_model_id = model_info["face_model"]['google_drive_id']
        face_model_url = f"https://drive.google.com/uc?id={face_model_id}"
        face_model_destination = os.path.join("face_model.h5")
        try:
            download_from_google_drive(face_model_url, face_model_destination)
        except Exception as e:
            print("Google Drive download failed. Attempting OneDrive download.")
            # Attempt OneDrive Download
            try:
                download(model_info["face_model"]['onedrive_url'], face_model_destination)
            except Exception as e:
                print("OneDrive download failed:", e)
