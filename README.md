# inmemory_keyvalue_apiservice

# Local setup without docker

```
cd ./app

Install all the requirements

pip install -r requirement.txt

Server Start command

uvicorn app:app --reload
```

### Dependancies:

redis

---

Run Unit tests

```
cd ./app/tests

# Run the command

pytest

```

---

# with Docker

```
docker build -t apiserver .

docker run -d -p 8000:8000 apiserver

### Run prometheus server as a docker container

docker run -p 9090:9090 -v ./prometheus.yml:/etc/prometheus/prometheus.yml -d prom/prometheus


### Run redis server locally in a docker container

docker run -p 6379:6379 -d redis

### Run Prometheus exporter

docker build -t exporter .

docker run -d -p 8080:8080 exporter
```

---

# with Docker compose

```
docker-compose up

docker-compose down
```

---

# K8s setup

```
### Run Redis in Helm

helm repo add bitnami https://charts.bitnami.com/bitnami

helm install redis bitnami/redis -f k8s/redis/redis.yaml --debug --version 16.13.2

### Apply server k8s resources

kubectl apply -f k8s/apiserver

### Apply cache exporter

kubectl apply -f k8s/cache_exporter/cache_exporter.yaml
```

### Server Endpoints

Once the docker is up check the following endpoints,


Server: http://localhost:8000/docs

Prometheus exporter: http://localhost:8080

Prometheus: http://localhost:9090


