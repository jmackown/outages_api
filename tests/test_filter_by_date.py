import json

from main import filter_outages_by_date
from tests.conftest import data_dir_path

with open(f"{data_dir_path}/outages.json") as f:
    test_outages_data = json.loads(f.read())


def test_filter_by_date():

    expected_result = [
        {
            "id": "002b28fc-283c-47ec-9af2-ea287336dc1b",
            "begin": "2022-05-23T12:21:27.377Z",
            "end": "2022-11-13T02:16:38.905Z",
        },
        {
            "id": "002b28fc-283c-47ec-9af2-ea287336dc1b",
            "begin": "2022-12-04T09:59:33.628Z",
            "end": "2022-12-12T22:35:13.815Z",
        },
        {
            "id": "04ccad00-eb8d-4045-8994-b569cb4b64c1",
            "begin": "2022-07-12T16:31:47.254Z",
            "end": "2022-10-13T04:05:10.044Z",
        },
        {
            "id": "086b0d53-b311-4441-aaf3-935646f03d4d",
            "begin": "2022-07-12T16:31:47.254Z",
            "end": "2022-10-13T04:05:10.044Z",
        },
    ]
    result = filter_outages_by_date(outage_data=test_outages_data)

    assert result == expected_result
