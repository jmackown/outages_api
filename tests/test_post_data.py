import json

from app import post_data

with open("data/post_data.json") as f:
    test_payload = json.loads(f.read())


def test_post_data(mock_outages_endpoint_post):

    result = post_data(payload=test_payload)

    assert result == {}