# Use an official Python runtime as a parent image
FROM python:3.8-slim
RUN pip install pyats[full]
RUN apt-get update && apt-get install -y openssh-client

# Set the working directory in the container
WORKDIR /testwork

# Copy the Python script to the container
COPY two_testbeds.yaml /testwork/
COPY two_devices_interface.py /testwork/

# Run the Python script when the container launches
ENTRYPOINT ["python", "/testwork/two_devices_interface.py"]
