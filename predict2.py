import tensorflow as tf
from keras import models
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from modelv2 import tokenizer_seq, tokenizer_struc, seq2ngrams, max_length
from keras.preprocessing.text import Tokenizer
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

model = models.load_model('protein_model2.h5', compile=False)


def onehot_to_seq(oh_seq, index):
    s = ''
    for o in oh_seq:
        i = np.argmax(o)
        if i != 0:
            s += index[i]
        else:
            break
    return s

def plot_results(x, y_):
    print("---")
    print("Input: " + str(x))
    print("Result: " + str(onehot_to_seq(y_, revsere_decoder_index).upper()))

input_sequence = ['SRGTQTE', 'YCQKWMWTCDEERKCCEGLVCRLWCKRIINM', 
'MKRQKRDRLERAHQRGYQAGIAGRSKEMCPYQTLNQRSQWLGGWREAMADRVVMAHHHHHH']

input_sequence = seq2ngrams(input_sequence)

    
revsere_decoder_index = {value:key for key,value in tokenizer_struc.word_index.items()}
revsere_encoder_index = {value:key for key,value in tokenizer_seq.word_index.items()}

tokenizer_seq = Tokenizer()
tokenizer_seq.fit_on_texts(input_sequence)

input_sequence = tokenizer_seq.texts_to_sequences(input_sequence)
input_sequence = pad_sequences(input_sequence, maxlen=max_length, padding='post')


N=3
y_pred = model.predict(input_sequence[:N])
print('Predictions:')
for i in range(N):
    plot_results(input_sequence[i], y_pred[i])

print("y_pred:" + str(y_pred[0]))
