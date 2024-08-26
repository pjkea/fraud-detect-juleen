import os
from flask import Flask, request, jsonify, render_template
import tensorflow as tf

app = Flask(__name__)

# Load the model
model = tf.keras.models.load_model('lstm_model.h5', custom_objects={'focal_loss_fixed': focal_loss()})


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Preprocess the input data as needed
    input_data = preprocess_input(data['input'])
    prediction = loaded_model.predict(input_data)
    return jsonify({'prediction': prediction.tolist()})


def preprocess_input(input_data):
    # Implement your preprocessing logic here
    # This should match how you preprocessed your training data
    return processed_data


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
