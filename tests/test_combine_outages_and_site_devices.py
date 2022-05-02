import json

from main import combine_outages_and_site_devices
from tests.conftest import data_dir_path

with open(f"{data_dir_path}/outages.json") as f:
    test_outages_data = json.loads(f.read())

test_devices = {
    "002b28fc-283c-47ec-9af2-ea287336dc1b": "Battery 1",
    "086b0d53-b311-4441-aaf3-935646f03d4d": "Battery 2",
}


def test_combine_outages_and_site_devices():
    expected_result = [
        {
            "id": "002b28fc-283c-47ec-9af2-ea287336dc1b",
            "name": "Battery 1",
            "begin": "2021-07-26T17:09:31.036Z",
            "end": "2021-08-29T00:37:42.253Z",
        },
        {
            "id": "002b28fc-283c-47ec-9af2-ea287336dc1b",
            "name": "Battery 1",
            "begin": "2022-05-23T12:21:27.377Z",
            "end": "2022-11-13T02:16:38.905Z",
        },
        {
            "id": "002b28fc-283c-47ec-9af2-ea287336dc1b",
            "name": "Battery 1",
            "begin": "2022-12-04T09:59:33.628Z",
            "end": "2022-12-12T22:35:13.815Z",
        },
        {
            "id": "086b0d53-b311-4441-aaf3-935646f03d4d",
            "name": "Battery 2",
            "begin": "2022-07-12T16:31:47.254Z",
            "end": "2022-10-13T04:05:10.044Z",
        },
    ]

    result = combine_outages_and_site_devices(
        devices=test_devices, outage_data=test_outages_data
    )

    assert result == expected_result
