import tensorflow as tf
from keras import models
from tensorflow.keras.preprocessing.sequence import pad_sequences
from modelv2 import tokenizer_seq, tokenizer_struc, max_length
from keras.preprocessing.text import Tokenizer
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

model = models.load_model('protein_model.h5', compile=False)

def onehot_to_seq(oh_seq, index):
    s = ''
    for o in oh_seq:
        i = np.argmax(o)
        if i != 0:
            s += index[i]
        else:
            break
    return s
    
revsere_decoder_index = {value:key for key,value in tokenizer_struc.word_index.items()}
revsere_encoder_index = {value:key for key,value in tokenizer_seq.word_index.items()}

sequence = 'MKRQKRDRLERAHQRGYQAGIAGRSKEMCPYQTLNQRSQWLGGWREAMADRVVMAHHHHHH'
seq = [[sequence[i:i+3] for i in range(len(sequence))]]
#seq = seq2ngrams(sequence)
print(seq)

#seq = [sequence[i:i + 3] for i in range(len(sequence))]
#seq = np.array([seq, []], object)[0]

tokenizer_seq = Tokenizer()
tokenizer_seq.fit_on_texts(seq)

seq = tokenizer_seq.texts_to_sequences(seq)
seq = pad_sequences(seq, maxlen=max_length, padding='post')
y_pred = model.predict(seq[:1])

print("---")
print("Input: " + str(sequence))
print("Result: " + str(onehot_to_seq(y_pred[0], revsere_decoder_index).upper()))
