import json

import pytest

from main import post_data

with open("data/post_data.json") as f:
    test_payload = json.loads(f.read())

test_site_id = "kingfisher"


def test_post_data(mock_outages_endpoint_post):

    result = post_data(payload=test_payload, site_id=test_site_id)

    assert result is None


@pytest.mark.failed
def test_post_data_422(mock_outages_endpoint_post):

    with pytest.raises(Exception) as error:
        post_data(payload=test_payload, site_id=test_site_id)

    assert str(error.value) == "422"
