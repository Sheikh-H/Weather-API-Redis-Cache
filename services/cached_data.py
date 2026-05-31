import redis
import requests
import json
import os
from dotenv import load_dotenv
from flask import jsonify

load_dotenv()

TIME = 43200

redis_client = redis.Redis(
    host=os.environ.get("REDIS_HOST"),
    port=int(os.environ.get("REDIS_PORT")),
    db=int(os.environ.get("REDIS_DB")),
    decode_responses=True,
)


def get_data(url):
    data = get_data_from_redis(url)
    if data:
        return jsonify(data)
    else:
        data = get_data_from_api(url)
    return jsonify(data)


def get_data_from_redis(url):
    data = redis_client.get(url)
    if data:
        return json.loads(data)
    return None


def get_data_from_api(url):
    response = requests.get(url)
    data = response.json()
    response.raise_for_status()
    store_data_in_redis(url, json.dumps(data, indent=2), TIME)
    return data


def store_data_in_redis(key, value, expiration):
    redis_client.set(key, value, ex=expiration)
