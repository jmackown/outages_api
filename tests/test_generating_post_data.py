import json

from main import generate_post_data
from tests.conftest import data_dir_path

with open(f"{data_dir_path}/outages.json") as f:
    test_outages_data = json.loads(f.read())

with open(f"{data_dir_path}/site-info.json") as f:
    test_site_info_data = json.loads(f.read())

test_devices = {
    "002b28fc-283c-47ec-9af2-ea287336dc1b": "Battery 1",
    "086b0d53-b311-4441-aaf3-935646f03d4d": "Battery 2",
}

test_site_id = "kingfisher"


def test_generating_post_data(monkeypatch):
    with open(f"{data_dir_path}/post_data.json") as f:
        expected_result = json.loads(f.read())

    result = generate_post_data(outage_data=test_outages_data, device_data=test_devices)

    assert result == expected_result
