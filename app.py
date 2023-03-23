from flask import Flask, send_from_directory, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment

import tensorflow as tf
import numpy as np
from keras import models
from tensorflow.keras.preprocessing.sequence import pad_sequences
from modelv2 import tokenizer_seq, tokenizer_struc, max_length
from keras.preprocessing.text import Tokenizer
import pandas as pd

app = Flask(__name__, static_url_path='', static_folder='mol3022/public')
CORS(app) #comment this on deployment
api = Api(app)

model = models.load_model('protein_model2.h5', compile=False)

def onehot_to_seq(oh_seq, index):
    s = ''
    for o in oh_seq:
        #print(o)
        #print(np.argmax(o))
        i = np.argmax(o)
        if i != 0:
            s += index[i]
        else:
            break
    return s

revsere_decoder_index = {value:key for key,value in tokenizer_struc.word_index.items()}
revsere_encoder_index = {value:key for key,value in tokenizer_seq.word_index.items()}

# This one is purely for testing purposes
@app.route('/input', methods=['POST'])
def input():
    data = request.get_json()
    input_str = data['input']
    output_str = input_str[::-1]
    return {'output': output_str}


@app.route('/predict', methods=['POST'])
def predict():
    
    data = request.get_json()

    input_seq = data['input']
    seq = [[input_seq[i:i+3] for i in range(len(input_seq))]]

    seq = tokenizer_seq.texts_to_sequences(seq)
    seq = pad_sequences(seq, maxlen=max_length, padding='post')
    y_pred = model.predict(seq[:1])

    result_str = str(onehot_to_seq(y_pred[0], revsere_decoder_index).upper())

    return {'predictions': result_str}
