from flask import Flask, send_from_directory, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
import tensorflow as tf
import numpy as np

app = Flask(__name__, static_url_path='', static_folder='mol3022/public')
CORS(app) #comment this on deployment
api = Api(app)

model = tf.keras.models.load_model('modelv2.h5')


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
    
    predictions = model.predict(data['input'])

    response = {'predictions': predictions.tolist()}

    return response
