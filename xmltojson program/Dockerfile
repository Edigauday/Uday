# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and XML file to the container
COPY . /app
COPY XMLtoJSON.py /testwork/
RUN pip install xmltodict

# Run the Python script when the container starts
ENTRYPOINT ["python", "XMLtoJSON.py"]
