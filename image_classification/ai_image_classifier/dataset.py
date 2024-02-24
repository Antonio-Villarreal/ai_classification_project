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
    datagen = ImageDataGenerator(
        rotation_range=20,  # randomly rotate images in the range (degrees, 0 to 20)
        width_shift_range=0.2,  # randomly shift images horizontally (fraction of total width)
        height_shift_range=0.2,  # randomly shift images vertically (fraction of total height)
        horizontal_flip=True,  # randomly flip images
        vertical_flip=True,  # randomly flip images
        rescale=1./255,  # rescale pixel values to [0, 1]
        validation_split=0.2  # split validation set
    )
    
    # training_dataset = keras.utils.image_dataset_from_directory(
    #     directory=dalle_recognition_files['training'],
    #     labels='inferred',
    #     label_mode='binary',
    #     batch_size=hyperparams['BATCH_SIZE'],
    #     image_size=(hyperparams['IMG_SIZE'], hyperparams['IMG_SIZE'])
    # )

    # validation_dataset = keras.utils.image_dataset_from_directory(
    #     directory=dalle_recognition_files['validation'],
    #     labels='inferred',
    #     label_mode='binary',
    #     batch_size=hyperparams['BATCH_SIZE'],
    #     image_size=(hyperparams['IMG_SIZE'], hyperparams['IMG_SIZE'])
    # )
    
    training_dataset = datagen.flow_from_directory(
        directory=dalle_recognition_files['training'],
        target_size=(hyperparams['IMG_SIZE'], hyperparams['IMG_SIZE']),
        batch_size=hyperparams['BATCH_SIZE'],
        class_mode='binary',
        subset='training'
    )

    validation_dataset = datagen.flow_from_directory(
        directory=dalle_recognition_files['training'],
        target_size=(hyperparams['IMG_SIZE'], hyperparams['IMG_SIZE']),
        batch_size=hyperparams['BATCH_SIZE'],
        class_mode='binary',
        subset='validation'
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
