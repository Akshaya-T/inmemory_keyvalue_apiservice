from typing import Union

from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
import redis
import json
import logging as logger

redis_client = redis.Redis(host='localhost')

app = FastAPI()


class Payload(BaseModel):
    key: str
    val: str


@app.get("/")
def ping():
    return "pong"


@app.get("/get/{key}")
def fetch_key(key: str):
    try:
        value = redis_client.get(key).decode()
        return {"value": value}
    except Exception as e:
        logger.exception(msg=e)
        return Response("Internal server error", status_code=500)


@app.post("/set")
def store_key(request: Payload):
    try:
        req_body = request.dict()
        redis_client.set(req_body["key"], req_body["val"])
        return {req_body["key"]: req_body["val"]}
    except Exception as e:
        logger.exception(msg=e)
        return Response("Internal server error", status_code=500)


@app.get("/search")
def search(prefix: str = "", suffix: str = ""):
    try:
        matches = redis_client.keys(prefix+"*"+suffix)
        return {"results": matches}
    except Exception as e:
        logger.exception(msg=e)
        return Response("Internal server error", status_code=500)
