import json

from app import get_unique_site_devices


with open("data/site-info.json") as f:
    test_site_info_data = json.loads(f.read())

def test_site_devices():
    expected_result = {
        "002b28fc-283c-47ec-9af2-ea287336dc1b": "Battery 1",
        "086b0d53-b311-4441-aaf3-935646f03d4d": "Battery 2",
    }
    result = get_unique_site_devices(site_data=test_site_info_data)

    assert result ==expected_result
