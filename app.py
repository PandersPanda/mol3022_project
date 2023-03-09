from flask import Flask, send_from_directory, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
import tensorflow as tf
import numpy as np

app = Flask(__name__, static_url_path='', static_folder='mol3022/public')
CORS(app) #comment this on deployment
api = Api(app)

model = tf.keras.models.load_model('modelv2.h5')

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
    
    pred = model.predict(data['input'])

    input_str = "example input string"
    input_seq = tokenizer_encoder.texts_to_sequences([input_str])[0]
    input_seq = pad_sequences([input_seq], maxlen=max_encoder_seq_length, padding='post')
    input_seq = to_categorical(input_seq, num_classes=num_encoder_tokens)

    y_pred = model.predict(input_seq)

    result_str = onehot_to_seq(y_pred[0], revsere_decoder_index).upper()
    print("Input: " + input_str)
    print("Result: " + result_str)


    response = {'predictions': str(onehot_to_seq(y_, revsere_decoder_index).upper())}

    return response
