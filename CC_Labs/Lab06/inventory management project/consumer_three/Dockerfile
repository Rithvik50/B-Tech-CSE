FROM python

RUN mkdir -p /home

COPY . /home

RUN pip install --no-cache-dir pika mysql-connector-python


CMD ["python","/home/one.py"]