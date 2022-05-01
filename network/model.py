import numpy as np
from tensorflow.python.keras import Sequential, layers
from keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.utils.np_utils import to_categorical

from dataset import load_dataset_do, load_dataset_thing


class ThingModel:
    def __init__(self, max_chars=100):
        self.max_chars = max_chars
        self.input_tokenizer = Tokenizer(char_level=True, lower=True, num_words=max_chars)
        self.output_tokenizer = Tokenizer(char_level=False, lower=True)

    def _refactor_dataset(self, xx, yy):
        self.input_tokenizer.fit_on_texts(xx)
        self.output_tokenizer.fit_on_texts(yy)
        xx = [[*item, *[0 for _ in range(self.max_chars - len(item))]] for item in
              self.input_tokenizer.texts_to_sequences(xx)]
        xx = [[to_categorical(letter_id, len(self.input_tokenizer.word_index) + 1) for letter_id in word] for word in
              xx]
        yy = [to_categorical(yyy[0], len(self.output_tokenizer.word_index) + 1) for yyy in
              self.output_tokenizer.texts_to_sequences(yy)]
        return np.array(xx), np.array(yy)

    def _set_model(self, input_shape, output_shape):
        self.layers = [
            layers.Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=input_shape),
            layers.MaxPooling2D((2, 2), strides=2),
            layers.Conv2D(64, (3, 3), padding='same', activation='relu'),
            layers.MaxPooling2D((2, 2), strides=2),
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dropout(0.3),
            layers.Dense(64, activation='relu'),
            layers.Dropout(0.2),
            layers.Dense(output_shape, activation='softmax', name='Output')
        ]
        self.model = Sequential(self.layers)
        self.model.compile('adam', 'categorical_crossentropy', 'accuracy')

    def train(self, x_train, y_train):
        x_train, y_train = self._refactor_dataset(x_train, y_train)
        x_train = np.expand_dims(x_train, 3)
        self._set_model(x_train[0].shape, y_train.shape[0])
        self.model.fit(x_train, y_train)

    def predict(self, text):
        xx = [[*item, *[0 for _ in range(self.max_chars - len(item))]] for item in
              self.input_tokenizer.texts_to_sequences([text])]
        xx = [[to_categorical(letter_id, len(self.input_tokenizer.word_index) + 1) for letter_id in word] for word in
              xx]
        pred = self.model.predict(xx)[0]
        pred = np.argmax(pred)
        return self.output_tokenizer.word_index[pred]


if __name__ == '__main__':
    x, y = load_dataset_thing()
    model = ThingModel()
    model.train(x, y)

    print(x[0], model.predict(x[0]))