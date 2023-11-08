# VAT Inference Service

This microservice performs VAT code predictions based on structured input data using a pre-trained machine learning model.

## How It Works

The service accepts JSON data containing various attributes like country, description, supplier, etc., preprocesses this data, runs it through a machine learning model, and returns the predicted VAT code.

## Usage

To make a prediction, send a POST request to the `/predict` endpoint with the required data in JSON format.

### Example:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"Country":"Luxembourg","Description":"HR solutions and corporate support","Month":"February","Supplier":"CompanyXYZ Luxembourg SA","Year":"2018"}' http://localhost:4003/predict
