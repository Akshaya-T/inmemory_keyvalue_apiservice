from fastapi import FastAPI, Request, Response
import redis
import json
import os
import argparse
import logging as logger
from prometheus_fastapi_instrumentator import Instrumentator
from schemas import Payload


app = FastAPI()
Instrumentator().instrument(app).expose(app)

# Creating redis client

pool = redis.ConnectionPool(host=os.getenv("REDIS_HOST"), port=6379)
redis_client = redis.Redis(connection_pool=pool)


@app.get("/")
def ping():
    return "pong"


@app.get("/get/{key}")
def fetch_key(key: str):
    """
    fetch key from the redis key value store returns the value
    """
    try:
        if redis_client.exists(key):
            value = redis_client.get(key).decode()
            return {"value": value}
        else:
            return Response("Key Not Found in the cache", status_code=404)
    except Exception as e:
        logger.exception(msg=e)
        return Response("Internal server error", status_code=500)


@app.post("/set")
def store_key(request: Payload):
    """
    store key value to the redis
    """
    try:
        req_body = request.dict()
        redis_client.set(req_body["key"], req_body["val"])
        return {req_body["key"]: req_body["val"]}
    except Exception as e:
        logger.exception(msg=e)
        return Response("Internal server error", status_code=500)


@app.get("/search")
def search(prefix: str = "", suffix: str = ""):
    """
    search for the given key prefix/suffix and returns the list of matching keys
    """
    try:
        matches = redis_client.keys(prefix+"*"+suffix)
        return {"results": matches}
    except Exception as e:
        logger.exception(msg=e)
        return Response("Internal server error", status_code=500)
