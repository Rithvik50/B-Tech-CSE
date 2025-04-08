FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=password

ENV MYSQL_DATABASE=mydatabase
ENV MYSQL_USER=myuser
ENV MYSQL_PASSWORD=password

# Copy the SQL script containing schema and data setup into the container
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the MySQL port
EXPOSE 3307

# Start MySQL service automatically when the container starts
CMD ["mysqld"]
