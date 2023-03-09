import tensorflow as tf
from keras import models
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from modelv2 import tokenizer_seq, tokenizer_struc, X_train, X_test, y_train, y_test
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

model = models.load_model('protein_model2.h5', compile=False)

model.summary()

sequences = ['HEI', 'OKI', 'KCK']

#Encode the sequences with padding

sequences = tokenizer_seq.texts_to_sequences(sequences)
input_data = pad_sequences(sequences, maxlen=128, padding='post')

#y_pred = model.predict(sequences)

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
    #print("Target: " + str(onehot_to_seq(y, revsere_decoder_index).upper()))
    print("Result: " + str(onehot_to_seq(y_, revsere_decoder_index).upper()))
    #fig = plt.figure(figsize=(10,2))
    #plt.imshow(y.T, cmap='Blues')
    #plt.imshow(y_.T, cmap='Reds', alpha=.5)
    #plt.yticks(range(4), [' '] + [revsere_decoder_index[i+1].upper() for i in range(3)])
    #plt.show()
    
revsere_decoder_index = {value:key for key,value in tokenizer_struc.word_index.items()}
revsere_encoder_index = {value:key for key,value in tokenizer_seq.word_index.items()}

y_pred = model.predict(['HEI'])
plot_results('HEI', y_pred[0])

# N=3
# y_train_pred = model.predict(X_train[:N])
# y_test_pred = model.predict(X_test[:N])
# print('training')
# for i in range(N):
#     plot_results('HEI', y_train[i], y_train_pred[i])
# print('testing')
# for i in range(N):
#     plot_results('HEI', y_test[i], y_test_pred[i])