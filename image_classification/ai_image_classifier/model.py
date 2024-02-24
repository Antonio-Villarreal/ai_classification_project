from utils import *


# def cnn_model(input_shape=(hyperparams['IMG_SIZE'], hyperparams['IMG_SIZE'], 3), num_classes=2):
#     tf.keras.backend.clear_session()
#     model = models.Sequential()

#     # Convolutional layers
#     model.add(layers.Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=input_shape))
#     model.add(layers.BatchNormalization())
#     model.add(layers.Conv2D(32, (3, 3), padding='same', activation='relu'))
#     model.add(layers.BatchNormalization())
#     model.add(layers.MaxPooling2D(pool_size=(2, 2)))

#     model.add(layers.Conv2D(64, (3, 3), padding='same', activation='relu'))
#     model.add(layers.BatchNormalization())
#     model.add(layers.Conv2D(64, (3, 3), padding='same', activation='relu'))
#     model.add(layers.BatchNormalization())
#     model.add(layers.MaxPooling2D(pool_size=(2, 2)))

#     model.add(layers.Conv2D(128, (3, 3), padding='same', activation='relu'))
#     model.add(layers.BatchNormalization())
#     model.add(layers.Conv2D(128, (3, 3), padding='same', activation='relu'))
#     model.add(layers.BatchNormalization())
#     model.add(layers.MaxPooling2D(pool_size=(2, 2)))

#     model.add(layers.Conv2D(256, (3, 3), padding='same', activation='relu'))
#     model.add(layers.BatchNormalization())
#     model.add(layers.Conv2D(256, (3, 3), padding='same', activation='relu'))
#     model.add(layers.BatchNormalization())
#     model.add(layers.MaxPooling2D(pool_size=(2, 2)))

#     model.add(layers.Conv2D(512, (3, 3), padding='same', activation='relu'))
#     model.add(layers.BatchNormalization())
#     model.add(layers.Conv2D(512, (3, 3), padding='same', activation='relu'))
#     model.add(layers.BatchNormalization())
#     model.add(layers.MaxPooling2D(pool_size=(2, 2)))

#     model.add(layers.Flatten())

#     # Dense layers
#     model.add(layers.Dense(512, activation='relu'))
#     model.add(layers.Dropout(0.5))
#     model.add(layers.Dense(1, activation='sigmoid'))  # Binary classification

#     model.summary()
#     return model


def resnet_block(x, filters, conv_size, pooling=True):
    # Shortcut path
    shortcut = layers.Conv2D(filters, kernel_size=1, strides=(2 if pooling else 1), padding='same', kernel_initializer='he_normal')(x)
    shortcut = layers.BatchNormalization()(shortcut)

    # Residual path
    x = layers.Conv2D(filters, conv_size, strides=(2 if pooling else 1), padding='same', kernel_initializer='he_normal')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    
    x = layers.Conv2D(filters, conv_size, padding='same', kernel_initializer='he_normal')(x)
    x = layers.BatchNormalization()(x)
    
    x = layers.add([shortcut, x])
    x = layers.Activation('relu')(x)
    
    if pooling:
        x = layers.MaxPooling2D((2, 2))(x)
    
    return x

def resnet_model(input_shape=(224, 224, 3), num_classes=2):
    inputs = layers.Input(shape=input_shape)
    
    x = layers.Conv2D(64, 7, strides=2, padding='same', kernel_initializer='he_normal')(inputs)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    x = layers.MaxPooling2D((3, 3), strides=2)(x)

    x = resnet_block(x, 64, 3)
    x = resnet_block(x, 128, 3)
    x = resnet_block(x, 256, 3)
    x = resnet_block(x, 512, 3)

    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dense(512, activation='relu', kernel_regularizer=regularizers.l2(0.001))(x)
    x = layers.Dropout(0.5)(x)
    
    outputs = layers.Dense(num_classes, activation='softmax')(x)

    model = models.Model(inputs, outputs)
    model.summary()
    return model

