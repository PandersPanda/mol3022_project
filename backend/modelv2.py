#Code inspired by https://www.kaggle.com/code/helmehelmuto/secondary-structure-prediction-with-keras
#This file is used so that the backend can import the tokenizers
#The code that you can run to train and evaluate the model is in modelv2.ipynb, not this one

import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import *
from tensorflow.keras.utils import to_categorical
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import text, sequence
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

#Load the data
data = pd.read_csv('./Data/2018-06-06-ss.cleaned.csv')
data.len.hist(bins=100)
max_length = 128
#print(data.shape)

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

#Encode the structures, and categorize them
tokenizer_struc = Tokenizer(char_level=True)
tokenizer_struc.fit_on_texts(structures)
structures = tokenizer_struc.texts_to_sequences(structures)
structures = pad_sequences(structures, maxlen=max_length, padding='post')
structures = to_categorical(structures)

structures.shape, sequences.shape

#Finding the amount of words and tags, so we can use it in the model, with the correct dimensions
word_amount = len(tokenizer_seq.word_index) + 1
tag_amount = len(tokenizer_struc.word_index) + 1

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(sequences, structures, test_size=0.3, random_state=42)
