import json

import pytest

from main import get_outage_data, get_site_info_data
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


def test_get_outage_data(mock_outages_endpoint):
    result = get_outage_data()
    assert result == test_outages_data


@pytest.mark.failed
def test_get_outage_data_500(mock_outages_endpoint):

    with pytest.raises(Exception) as error:
        get_outage_data()

    assert str(error.value) == "500"


def test_get_site_info_data(mock_site_info_endpoint):
    result = get_site_info_data(site_id=test_site_id)

    assert result == test_site_info_data


@pytest.mark.failed
def test_get_site_info_data_500(mock_site_info_endpoint):

    with pytest.raises(Exception) as error:
        get_site_info_data(site_id=test_site_id)

    assert str(error.value) == "500"
