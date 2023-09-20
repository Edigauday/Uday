#Use an official Python runtime as a parent image
FROM python:3.8-slim

#Set the working directory in the container
WORKDIR /one-to-many

#Copy the current directory contents into the container at /app
COPY server1.py /one-to-many
COPY server2.py /one-to-many
COPY config.json /one-to-many

#Install any needed packages specified in requirements.txt
# If you have a requirements.txt file for dependencies

 
#Expose the ports for both servers
EXPOSE 5000
EXPOSE 5001
