import os
import gdown
import json


def download_from_google_drive(url, output_file):
    gdown.download(url, output_file, quiet=False)


if __name__ == "__main__":
    json_file_path = os.path.join("models.json")
    with open(json_file_path, "r") as json_file:
        model_info = json.load(json_file)
            
    # Download image_model.h5 if it doesn't exist
    if not os.path.exists("image_model.h5"):
        image_model_id = model_info["image_model"]
        image_model_url = f"https://drive.google.com/uc?id={image_model_id}"
        filename_2 = "image_model.h5"
        destination_2 = os.path.join(filename_2)
        download_from_google_drive(image_model_url, destination_2)

    # Download face_model.h5 if it doesn't exist
    if not os.path.exists("face_model.h5"):
        face_model_id = model_info["face_model"]
        face_model_url = f"https://drive.google.com/uc?id={face_model_id}"
        filename_1 = "face_model.h5"
        destination_1 = os.path.join(filename_1)
        download_from_google_drive(face_model_url, destination_1)


