FROM python:3.8-slim

WORKDIR /app

ADD requirement.txt /app/requirement.txt
ADD entrypoint.sh /app/entrypoint.sh

RUN pip install -r /app/requirement.txt && \
    chmod +x /app/entrypoint.sh

ADD app.py /app/app.py

ENTRYPOINT ["/app/entrypoint.sh"]
EXPOSE 8000
