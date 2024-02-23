from utils import *

dalle_recognition_dataset = os.path.join('dataset', 'dalle_recognition')
# https://www.kaggle.com/datasets/gauravduttakiit/dalle-recognition-dataset

dalle_recognition_files = {
    'training': os.path.join(dalle_recognition_dataset, 'train'),
    'training_fake': os.path.join(dalle_recognition_dataset, 'train', 'fake'),
    'training_real': os.path.join(dalle_recognition_dataset, 'train', 'real'),
    'testing': os.path.join(dalle_recognition_dataset, 'test'),
    'testing_fake': os.path.join(dalle_recognition_dataset, 'test', 'fake'),
    'testing_real': os.path.join(dalle_recognition_dataset, 'test', 'real'),
}


def dalle_recognition_datasets():
    training_dataset = keras.utils.image_dataset_from_directory(
        directory=dalle_recognition_files['training'],
        labels='inferred',
        label_mode='binary',
        batch_size=hyperparams['BATCH_SIZE'],
        image_size=(hyperparams['IMG_SIZE'], hyperparams['IMG_SIZE'])
    )

    validation_dataset = keras.utils.image_dataset_from_directory(
        directory=dalle_recognition_files['validation'],
        labels='inferred',
        label_mode='binary',
        batch_size=hyperparams['BATCH_SIZE'],
        image_size=(hyperparams['IMG_SIZE'], hyperparams['IMG_SIZE'])
    )

    testing_dataset = keras.utils.image_dataset_from_directory(
        directory=dalle_recognition_files['testing'],
        labels='inferred',
        label_mode='binary',
        batch_size=hyperparams['BATCH_SIZE'],
        image_size=(hyperparams['IMG_SIZE'], hyperparams['IMG_SIZE'])
    )

    return training_dataset, validation_dataset, testing_dataset


def display_random_image(directory: str):
    image = random.choice(os.listdir(directory))
    jpg_image_path = os.path.join(directory, image)
    jpg_image = Image.open(jpg_image_path)

    print(f"Path: {jpg_image_path}")
    print(f"Size: {jpg_image.size}")
    print(f"Number of Channels: {jpg_image.mode}")
    print('')

    fig, ax = plt.subplots(1, 1, figsize=(1, 1))
    ax.imshow(jpg_image, interpolation='nearest')
    ax.axis("off")
    plt.show()


def display_random_images(dictionary: dict):
    for label, path in dictionary.items():
        if 'fake' in label or 'real' in label:
            display_random_image(path)


if __name__ == "__main__":
    display_random_images(dalle_recognition_files)
