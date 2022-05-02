import json

from main import post_data

with open("data/post_data.json") as f:
    test_payload = json.loads(f.read())

test_site_id = "kingfisher"


def test_post_data(mock_outages_endpoint_post):

    result = post_data(payload=test_payload, site_id=test_site_id)

    assert result == {}
