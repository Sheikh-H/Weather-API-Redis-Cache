from flask import Flask, request
from flask_limiter import Limiter
from dotenv import load_dotenv
import requests
import os
import jsonify
import redis
from services.cached_data import get_data

load_dotenv()

API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

# url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/manchester/2026-05-31/2026-06-15?unitGroup=uk&key=KWGGLKXSLHEDMHADL9GWHBUWD&contentType=json"


@app.route("/weather", methods=["GET"])
def weather():
    location = request.args.get("location")
    date_from = request.args.get("date_from")
    date_to = request.args.get("date_to")

    if location and date_from and date_to:
        url = f"{base_url}{location}/{date_from}/{date_to}?unitGroup=uk&key={API_KEY}&contentType=json"
        get_data(url)
    elif location and date_from:
        url = f"{base_url}{location}/{date_from}?unitGroup=uk&key={API_KEY}&contentType=json"
        get_data(url)
    elif location:
        url = f"{base_url}{location}/?unitGroup=uk&key={API_KEY}&contentType=json"
        get_data(url)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port, host="127.0.0.1")
