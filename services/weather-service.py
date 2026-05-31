def fetch_request(location, date_to=None, date_from=None):
    base_url = "127.0.0.1:5000/weather?"
    if date_from and date_to:
        url = f"{base_url}{location}/{date_to}/{date_to}"
    elif date_to:
        url = f"{base_url}{location}/{date_to}"
    else:
        url = f"{base_url}{location}"
    # Get data and place in redis
    # Display result on terminal after request.

def place_request():
    # Place request in redis function