#main.py

from flask import Flask, request, jsonify
from inference_preprocessing import preprocess_input
import joblib
import pandas as pd

app = Flask(__name__)

transformer_path = 'app/transformers/rf_column_transformer.joblib'
model_path = 'app/models/random_forest_model.joblib'
vat_code_mapping_path = 'app/code_mappings/rf_code_mapping.joblib'

transformer = joblib.load(transformer_path)
model = joblib.load(model_path)
vat_code_mapping = joblib.load(vat_code_mapping_path)


@app.route('/predict', methods=['POST'])
def predict_vat_code():
    input_json = request.get_json()
    
    # Preprocess the input data
    X = preprocess_input(input_json, transformer)

    # Run the model inference
    prediction = model.predict(X)
    predicted_vat_code_name = vat_code_mapping.get(prediction[0], "Unknown VAT CODE")

    # Append the prediction to the input_json
    input_json['VAT CODE'] = predicted_vat_code_name

    return jsonify(input_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
