from flask import Flask, send_from_directory, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
import tensorflow as tf
import numpy as np
from keras import models
from tensorflow.keras.preprocessing.sequence import pad_sequences
from modelv2 import tokenizer_seq, tokenizer_struc, X_train, X_test, y_train, y_test

app = Flask(__name__, static_url_path='', static_folder='mol3022/public')
CORS(app) #comment this on deployment
api = Api(app)

#model = tf.keras.models.load_model('modelv2.h5')
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

def seq2ngrams(seqs, n=3):
    return np.array([[seq[i:i+n] for i in range(len(seq))] for seq in seqs])

@app.route('/input', methods=['POST'])
def input():
    data = request.get_json()
    input_str = data['input']
    output_str = input_str[::-1]
    return {'output': output_str}

@app.route('/predict', methods=['POST'])
def predict():
    # Use the h5 model to predict protein structure from input
    data = request.get_json()

    input_seq = [data['input']]

    sequences = tokenizer_seq.texts_to_sequences(input_seq)
    input_data = pad_sequences(sequences, maxlen=128, padding='post')

    revsere_decoder_index = {value:key for key,value in tokenizer_struc.word_index.items()}
    revsere_encoder_index = {value:key for key,value in tokenizer_seq.word_index.items()}

    y_ = model.predict(input_data)

    result_str = onehot_to_seq(y_[0], revsere_decoder_index).upper()


    
    """
    pred = model.predict(data['input'])

    input_str = "example input string"
    input_seq = tokenizer_encoder.texts_to_sequences([input_str])[0]
    input_seq = pad_sequences([input_seq], maxlen=max_encoder_seq_length, padding='post')
    input_seq = to_categorical(input_seq, num_classes=num_encoder_tokens)

    y_pred = model.predict(input_seq)

    result_str = onehot_to_seq(y_pred[0], revsere_decoder_index).upper()
    print("Input: " + input_str)
    print("Result: " + result_str)
    """


    response = {'predictions': result_str}

    return response
