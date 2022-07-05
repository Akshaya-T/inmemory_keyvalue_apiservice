# inmemory_keyvalue_apiservice

# Local setup without docker

Install all the requirements

pip install -r requirement.txt

Server Start command

uvicorn app:app --reload

# with Docker

docker build -t apiserver .
docker run -d -p 8000:8000 apiserver

# Run prometheus server as a docker container

docker run -p 9090:9090 -d prom/prometheus

# Run redis server locally in a docker container

docker run -p 6379:6379 -d redis
