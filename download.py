import os
import gdown
import json


def download_from_google_drive(url, output_file):
    gdown.download(url, output_file, quiet=False)


if __name__ == "__main__":
    destination_directory = "application/models"

    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    json_file_path = os.path.join(destination_directory, "models.json")
    with open(json_file_path, "r") as json_file:
        model_info = json.load(json_file)

    # Download face_model.h5
    face_model_link = model_info["face_model"]
    filename_1 = "face_model.h5"
    destination_1 = os.path.join(destination_directory, filename_1)
    download_from_google_drive(face_model_link, destination_1)

    # Download image_model.h5
    image_model_link = model_info["image_model"]
    filename_2 = "image_model.h5"
    destination_2 = os.path.join(destination_directory, filename_2)
    download_from_google_drive(image_model_link, destination_2)
