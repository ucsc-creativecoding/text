from __future__ import print_function
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random
import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
from keras.models import load_model

model = load_model('rnn_model.h5')
text = open('./data/input.txt').read().lower()
chars = sorted(list(set(text)))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

# cut the text in semi-redundant sequences of maxlen characters
maxlen = 9
# text generation

def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

def init_text_generation(init_length):
    while 1 > 0 :
        s = text[random.randint(0, len(text)-1)]
        if len(s) > init_length:
            return s[0:init_length]

diversity = 0.5
text = text.split("\n");
for interation in range(10):

    generated = ''
    sentence = init_text_generation(maxlen)
    generated += sentence
    sys.stdout.write(generated)

    for i in range(100):
        x_pred = np.zeros((1, maxlen, len(chars)))
        for t, char in enumerate(sentence):
            x_pred[0, t, char_indices[char]] = 1.

        preds = model.predict(x_pred, verbose=0)[0]
        next_index = sample(preds, diversity)
        next_char = indices_char[next_index]

        generated += next_char
        sentence = sentence[1:] + next_char
        sys.stdout.write(next_char)
        sys.stdout.flush()
        if next_char==".":
            break
    print()
