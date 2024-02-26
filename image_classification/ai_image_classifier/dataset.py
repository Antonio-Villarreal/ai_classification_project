from utils import *

realifake_dataset = os.path.join('dataset', 'Realifake')
# https://www.kaggle.com/datasets/sattyam96/realifake

realifake_files = {
    'data': realifake_dataset,
    'data_fake': os.path.join(realifake_dataset, 'fake'),
    'data_real': os.path.join(realifake_dataset, 'real'),
}


def realifake_datasets():
    training_dataset = keras.utils.image_dataset_from_directory(
        directory=realifake_files['data'],
        labels='inferred',
        label_mode='binary',
        batch_size=hyperparams['BATCH_SIZE'],
        image_size=(hyperparams['IMG_SIZE'], hyperparams['IMG_SIZE']),
        validation_split=0.2,
        subset='training',
        seed=123
    )

    validation_dataset = keras.utils.image_dataset_from_directory(
        directory=realifake_files['data'],
        labels='inferred',
        label_mode='binary',
        batch_size=hyperparams['BATCH_SIZE'],
        image_size=(hyperparams['IMG_SIZE'], hyperparams['IMG_SIZE']),
        validation_split=0.2,
        subset='validation',
        seed=123
    )

    testing_dataset = keras.utils.image_dataset_from_directory(
        directory=realifake_files['data'],
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
    display_random_images(realifake_files)
