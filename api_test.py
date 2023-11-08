# api_test.py

import requests
import json

# API endpoint; adjust if hosted elsewhere
API_ENDPOINT = 'http://172.17.0.1:5004/predict'

# Input and output file paths
input_file_path = '/workspaces/EY_VATInference-Service/json_input/test.json'
output_file_path = '/workspaces/EY_VATInference-Service/json_output/predicted_output.json'

# Load the input data
with open(input_file_path, 'r') as input_file:
    payload = json.load(input_file)

# Make the POST request to the Flask API
response = requests.post(API_ENDPOINT, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Load the response data
    response_data = response.json()
    
    # Save the output to a file
    with open(output_file_path, 'w') as output_file:
        json.dump(response_data, output_file, indent=4)
    
    print(f'Response successfully saved to {output_file_path}')
else:
    print(f'Failed to get a successful response. Status code: {response.status_code}')
