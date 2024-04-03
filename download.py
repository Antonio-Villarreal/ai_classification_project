import os
import requests

def download_file_from_google_drive(url, destination):
    session = requests.Session()

    # Extract file ID from URL
    file_id = url.split('/')[-2]

    # Create the URL for the file download
    URL = "https://drive.google.com/uc?id=" + file_id

    # Make request to download the file
    response = session.get(URL, stream=True)

    # Save the file to the destination directory
    with open(destination, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)

    print(f"File downloaded to: {destination}")

if __name__ == "__main__":
    # Provide the Google Drive link and the destination directory
    google_drive_link = "https://drive.google.com/file/d/1iqh5EraZ8fF4YTAFA3_Q9lWYJ4tOGlBH/view?usp=drive_link"
    destination_directory = "application/models"
    filename = "face_model.h5"
    destination = os.path.join(destination_directory, filename)

    # Call the function to download the file
    download_file_from_google_drive(google_drive_link, destination)
    
    # Provide the Google Drive link and the destination directory
    google_drive_link = "https://drive.google.com/file/d/13MUAaQYZt_C2bpmevP7FaeOmNYJp4_j5/view?usp=drive_link"
    destination_directory = "application/models"
    filename = "image_model.h5"
    destination = os.path.join(destination_directory, filename)

    # Call the function to download the file
    download_file_from_google_drive(google_drive_link, destination)
