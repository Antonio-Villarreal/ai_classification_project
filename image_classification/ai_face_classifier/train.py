from utils import *
from dataset import *
from model import cnn_model


def train_model(model, training_dataset, validation_dataset, epochs=10):
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    history = model.fit(
        training_dataset,
        validation_data=validation_dataset,
        epochs=hyperparams['EPOCHS'],
        batch_size=hyperparams['BATCH_SIZE'],
        verbose=1
    )

    loss, accuracy = model.evaluate(validation_dataset, verbose=0)

    results = {
        'accuracy': accuracy,
        'loss': loss,
        'history': history.history
    }
    return results


def evaluate_model(model, testing_dataset):
    test_loss, test_accuracy = model.evaluate(testing_dataset)
    results = {
        'test_accuracy': test_accuracy,
        'test_loss': test_loss
    }
    return results


def model_workflow():
    model = cnn_model()
    training_dataset, validation_dataset, testing_dataset = datasets()
    training_results = train_model(model, training_dataset, validation_dataset, epochs=hyperparams['EPOCHS'])
    evaluation_results = evaluate_model(model, training_dataset)
    save_results(model, training_results, evaluation_results, hyperparams)


if __name__ == "__main__":
    model_workflow()
