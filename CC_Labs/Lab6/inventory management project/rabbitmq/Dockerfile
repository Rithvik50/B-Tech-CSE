# Use the official RabbitMQ image from Docker Hub
FROM rabbitmq:3-management


# Expose the AMQP and management ports
EXPOSE 5672 15672

# Define environment variables for RabbitMQ configuration
ENV RABBITMQ_DEFAULT_USER=PES2UG22CS451
ENV RABBITMQ_DEFAULT_PASS=password
ENV RABBITMQ_HOST=rabbitmqcontainer

# Set the entry point to run RabbitMQ server
CMD ["rabbitmq-server"]


