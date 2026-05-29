import requests


def fetch_satellite_data():
    url = "https://api.wheretheiss.at/v1/satellites/25544"

    response = requests.get(url)
    data = response.json()

    return {
        "value": int(data["velocity"]),
        "service": "ISS",
        "status": "ok"
    }
