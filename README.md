# VAT Inference Service

This microservice performs VAT code predictions based on structured input data using a pre-trained machine learning model.

## How It Works

The service accepts JSON data containing various attributes like country, description, supplier, etc., preprocesses this data, runs it through a machine learning model, and returns the predicted VAT code.

## Usage

To make a prediction, send a POST request to the `/predict` endpoint with the required data in JSON format.

### Example:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"Country":"Luxembourg","Description":"HR solutions and corporate support","Month":"February","Supplier":"CompanyXYZ Luxembourg SA","Year":"2018"}' http://localhost:5004/predict
```

## Building and Running with Docker

To build and run the microservice using Docker, follow these steps:

1. Ensure Docker is installed on your system. You can download it from the [Docker website](https://www.docker.com/products/docker-desktop).

2. Build the Docker image by running the following command in your terminal:

```bash
docker build -t text-to-structure-microservice .
docker run -p 5004:5004 text-to-structure-microservice