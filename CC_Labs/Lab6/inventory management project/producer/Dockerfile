# Use Python base image
FROM python

# Set the working directory in the container
WORKDIR /home

# Copy the application files to the container
COPY . /home

# Install dependencies
RUN pip install --no-cache-dir pika Flask mysql-connector-python

# Expose the port on which the Flask app will run
EXPOSE 5050

# Command to run the Flask application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5050" ]


