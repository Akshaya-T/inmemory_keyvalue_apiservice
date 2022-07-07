FROM python:3.8-slim

ADD requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

ADD prometheus_exporter.py /code/prometheus_exporter.py
WORKDIR /code
ENV PYTHONPATH '/code/'
ENTRYPOINT [ "python" , "/code/prometheus_exporter.py"]
CMD ["localhost"]
