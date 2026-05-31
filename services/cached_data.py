import redis
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

TIME = int(os.environ.get("CACHE_EXPIRATION"))

redis_client = redis.Redis(
    host=os.environ.get("REDIS_HOST"),
    port=int(os.environ.get("REDIS_PORT")),
    db=int(os.environ.get("REDIS_DB")),
)


# Main function that houses all the other functions to work.
def get_data(url):
    data = get_data_from_redis(url)
    if data == False:
        get_data_from_api(url)
    else:
        return json.loads(data)


# First look for the data inside redis, if data is < 12 hours, then return:
def get_data_from_redis(url):
    data = redis_client.get(url)
    if data:  # response null or error
        return json.loads(data)
    else:
        data = get_data_from_api(url)
        return json.loads(data)


# If not available, get the data from the api
def get_data_from_api(url):
    response = requests.get(url)
    data = response.json()
    store_data_in_redis(url, data, TIME)
    return json.loads(data)


# Update the data in the redis database and set expiration to being 12 hours
def store_data_in_redis(key, value, expiration):
    pass
