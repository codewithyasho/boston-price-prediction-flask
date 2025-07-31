import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, url_for, render_template
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('xgboost_model.pkl')
scalar = joblib.load('boston_housing_scaler.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json["data"]
    print("\nReceived data:", data)

    # Convert the data into array and reshape it
    input_data = np.array(list(data.values())).reshape(1, -1)
    print("\nInput data reshaped:", input_data)

    # Scale the input data
    scaled_data = scalar.transform(input_data)
    print("\nScaled data:", scaled_data)

    # Make a prediction
    prediction = model.predict(scaled_data)
    print("\nPrediction:", prediction)

    return jsonify(prediction[0])


@app.route('/predict', methods=['POST'])
def predict():
    received_data = [float(x) for x in request.form.values()]
    print("\nReceived data from form:", received_data)

    # Convert the received_data into array and reshape it
    scaled_data = scalar.transform(np.array(received_data).reshape(1, -1))
    print("\nScaled data from form:", scaled_data)

    # Make a prediction
    prediction = model.predict(scaled_data)
    print("\nPrediction from form:", prediction[0])

    return render_template('index.html', predicted_result='Predicted Price : {:.2f}$ Thousand Dollars'.format(prediction[0]))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
