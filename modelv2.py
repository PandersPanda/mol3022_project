#Code inspired by https://www.kaggle.com/code/helmehelmuto/secondary-structure-prediction-with-keras
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import *
from keras.utils import  to_categorical
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import text, sequence
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

#Load the data
data = pd.read_csv('./Data/2018-06-06-ss.cleaned.csv')
data.len.hist(bins=100)
max_length = 128
print(data.shape)

#Remove sequences that are too long and sequences that contain non-standard amino acids
sequences, structures = data[['seq', 'sst3']][(data.len <= max_length) & (~data.has_nonstd_aa)].values.T 

#For saving memory
data = []

#Making the sequences into grams, because this makes it easier for the model to learn
def seq2ngrams(seqs, n=3):
    return np.array([[seq[i:i+n] for i in range(len(seq))] for seq in seqs], dtype=object)

sequences = seq2ngrams(sequences)

#Preprocess the data

#Encode the sequences with padding
tokenizer_seq = Tokenizer()
tokenizer_seq.fit_on_texts(sequences)
sequences = tokenizer_seq.texts_to_sequences(sequences)
sequences = pad_sequences(sequences, maxlen=max_length, padding='post')

print(sequences[1])

#sequence back to its string value
print(tokenizer_seq.sequences_to_texts(sequences[1:2])[0])

#Encode the structures, and categorize them
tokenizer_struc = Tokenizer(char_level=True)
tokenizer_struc.fit_on_texts(structures)
structures = tokenizer_struc.texts_to_sequences(structures)
structures = pad_sequences(structures, maxlen=max_length, padding='post')
structures = to_categorical(structures)

print(structures[1])

structures.shape, sequences.shape

#Finding the amount of words and tags, so we can use it in the model, with the correct dimensions
word_amount = len(tokenizer_seq.word_index) + 1
tag_amount = len(tokenizer_struc.word_index) + 1

# Define the model architecture
model = Sequential()
model.add(Embedding(input_dim = word_amount, output_dim= 128, input_length=max_length))
model.add(Bidirectional(LSTM(units=64, dropout=0.2, recurrent_dropout=0.2, return_sequences=True)))
model.add(Dense(tag_amount, activation='softmax'))
model.summary()

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(sequences, structures, test_size=0.3, random_state=42)

# Train and save the model
model.fit(X_train, y_train, batch_size=128, epochs=5, validation_data=(X_test, y_test), verbose=1)
model.save("protein_model3.h5")