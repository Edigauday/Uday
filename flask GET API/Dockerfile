# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables for Flask
ENV FLASK_APP getapi.py

ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 5000

# Set the working directory in the container

WORKDIR /flask
# Copy the current directory contents into the container at /app
COPY getapi.py /flask

# Install any needed packages specified in requirements.txt
RUN pip install flask

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define the command to run your application
CMD ["flask", "run"]
