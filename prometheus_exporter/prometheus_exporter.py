import time
import os
import argparse
import redis
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server

parser = argparse.ArgumentParser(description='Parse docker args')
parser.add_argument('redis_host', type=str, help='Redis host')
args = parser.parse_args()


class CustomCacheCollector(object):
    def __init__(self):
        self.redis_host = args.redis_host
        self.redis_client = redis.Redis(host=self.redis_host, port=6379)

    def collect(self):
        g = GaugeMetricFamily(
            "redis_keys", 'Total number of keys in redis db', labels=['app', 'redis_host'])
        total_keys = self.redis_client.dbsize()
        g.add_metric(["redis", self.redis_host], total_keys)
        yield g


if __name__ == '__main__':
    start_http_server(8080)
    REGISTRY.register(CustomCacheCollector())
    while True:
        time.sleep(1)
