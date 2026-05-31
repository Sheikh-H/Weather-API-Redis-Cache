import redis
import requests
import json
import jsonify
import os
from dotenv import load_dotenv

load_dotenv()

TIME = int(os.environ.get("CACHE_EXPIRATION"))

redis_client = redis.Redis(
    host=os.environ.get("REDIS_HOST"),
    port=int(os.environ.get("REDIS_PORT")),
    db=int(os.environ.get("REDIS_DB")),
)


def get_data(url):
    data = get_data_from_redis(url)
    if data == False:
        get_data_from_api(url)
    else:
        return jsonify(data)


def get_data_from_redis(url):
    data = redis_client.get(url)
    if data:
        return jsonify(data)
    else:
        data = get_data_from_api(url)
        return jsonify(data)


def get_data_from_api(url):
    try:
        response = requests.get(url)
        data = response.json()
        store_data_in_redis(url, json.dumps(data, indent=2), TIME)
    except Exception as e:
        print(e)
    return jsonify(data)


def store_data_in_redis(key, value, expiration):
    redis_client.set(key, value, ex=expiration)
