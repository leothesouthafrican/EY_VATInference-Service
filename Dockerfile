# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5003 available to the world outside this container
EXPOSE 5004

# Define environment variable
ENV NAME World

# Run main.py when the container launches
CMD ["python", "./app/main.py"]
