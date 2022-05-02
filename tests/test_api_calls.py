import json

from main import get_outage_data, get_site_info_data

with open("data/outages.json") as f:
    test_outages_data = json.loads(f.read())

with open("data/site-info.json") as f:
    test_site_info_data = json.loads(f.read())

test_devices = {
    "002b28fc-283c-47ec-9af2-ea287336dc1b": "Battery 1",
    "086b0d53-b311-4441-aaf3-935646f03d4d": "Battery 2",
}

test_site_id = "kingfisher"


def test_get_outage_data(mock_outages_endpoint):
    result = get_outage_data()

    # assert result.status_code == 200
    assert result == test_outages_data


def test_get_site_info_data(mock_site_info_endpoint):
    result = get_site_info_data(site_id=test_site_id)

    # assert result.status_code == 200
    assert result == test_site_info_data
