from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
from urllib.parse import quote
import os
from services.cached_data import get_data

load_dotenv()

API_KEY = os.getenv("API_KEY")

app = Flask(__name__)
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
)

base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"


@app.route("/weather", methods=["GET"])
@limiter.limit("50 per hour")
def weather():
    location = request.args.get("location").strip()
    location = quote(location)
    # Use a strptime and strftime to rearrange the date as necessary. Maybe change it to being something slightly different like using day, month and year instead to form the date fields. this would make it easier for the user to enter dates into the url and prevent input errors
    date_from = request.args.get("datefrom")
    date_to = request.args.get("dateto")

    if not location:
        return {"error": "Please enter a location"}, 400
    if location and date_from and date_to:
        url = f"{base_url}{location}/{date_from}/{date_to}?unitGroup=uk&key={API_KEY}&contentType=json"
        return get_data(url), 200
    elif location and date_from:
        url = f"{base_url}{location}/{date_from}?unitGroup=uk&key={API_KEY}&contentType=json"
        return get_data(url), 200
    elif location:
        url = f"{base_url}{location}/?unitGroup=uk&key={API_KEY}&contentType=json"
        return get_data(url), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
