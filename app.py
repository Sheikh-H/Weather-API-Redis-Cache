from flask import Flask, request
from flask_limiter import Limiter
from dotenv import load_dotenv
import requests
import os
import jsonify

load_dotenv()

API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

# url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/manchester/2026-05-31/2026-06-15?unitGroup=uk&key=KWGGLKXSLHEDMHADL9GWHBUWD&contentType=json"


@app.route("/weather", methods=["GET"])
def weather():
    pass


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port, host="127.0.0.1")
