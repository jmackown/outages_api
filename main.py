import json
import os
from datetime import datetime

import click
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
headers = {
    "Accept": "application/json",
    "x-api-key": os.getenv("API_KEY"),
}


def get_outage_data():
    response = requests.get(url=f"{BASE_URL}/outages", headers=headers)
    return response.json()


def get_site_info_data(site_id):
    response = requests.get(f"{BASE_URL}/site-info/{site_id}", headers=headers)
    return response.json()


def get_unique_site_devices(site_data):
    return {
        x["id"]: x["name"] for k, v in site_data.items() for x in v if k == "devices"
    }


def filter_outages_by_date(outage_data, start_date="2022-01-01T00:00:00.000Z"):
    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
    filtered_outages = []
    for outage in outage_data:
        if datetime.strptime(outage["begin"], DATE_FORMAT) >= datetime.strptime(
            start_date, DATE_FORMAT
        ):
            filtered_outages.append(outage)
    return filtered_outages


def combine_outages_and_site_devices(devices, outage_data):
    combined = []
    for outage in outage_data:
        try:
            outage["name"] = devices[outage["id"]]
            combined.append(outage)
        except KeyError:
            pass
    return combined


def generate_post_data(outage_data, device_data):
    filtered = filter_outages_by_date(outage_data=outage_data)
    combined_data = combine_outages_and_site_devices(
        devices=device_data, outage_data=filtered
    )
    return combined_data


def post_data(payload, site_id):

    response = requests.post(
        f"{BASE_URL}/site-outages/{site_id}", headers=headers, data=json.dumps(payload)
    )
    print(response)
    return response.json()


@click.command()
@click.option("--site_id", prompt="What site id are you searching for?")
def run(site_id):
    pass
    click.echo("Getting outage data")
    outage_data = get_outage_data()
    print(f"outage_data: {outage_data}")
    click.echo(f"Getting site data for '{site_id}'")
    site_data = get_site_info_data(site_id=site_id)
    print(f"site_data: {site_data}")
    click.echo(f"Getting device data for '{site_id}'")
    device_data = get_unique_site_devices(site_data=site_data)
    print(f"device_data: {device_data}")

    payload_data = generate_post_data(outage_data=outage_data, device_data=device_data)

    post_data(payload=payload_data, site_id=site_id)


if __name__ == "__main__":
    run()
