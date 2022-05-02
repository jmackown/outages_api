import json

import pytest
import responses


@pytest.fixture(autouse=True)
def no_http_requests(monkeypatch):
    def urlopen_mock(self, method, url, *args, **kwargs):
        raise RuntimeError(
            f"The test was about to {method} {self.scheme}://{self.host}{url}"
        )

    monkeypatch.setattr(
        "urllib3.connectionpool.HTTPConnectionPool.urlopen", urlopen_mock
    )


with open("data/outages.json") as f:
    test_outages_data = json.loads(f.read())

with open("data/site-info.json") as f:
    test_site_info_data = json.loads(f.read())

test_devices = {
    "002b28fc-283c-47ec-9af2-ea287336dc1b": "Battery 1",
    "086b0d53-b311-4441-aaf3-935646f03d4d": "Battery 2",
}

test_site_id = "kingfisher"


@pytest.fixture()
def mock_outages_endpoint():
    with responses.RequestsMock() as rsps_success:
        rsps_success.add(
            responses.GET,
            "http://example.com/outages",
            body=json.dumps(test_outages_data),
            status=200,
            content_type="application/json",
        )
        yield rsps_success

@pytest.fixture()
def mock_outages_endpoint_post():
    with responses.RequestsMock() as rsps_success:
        rsps_success.add(
            responses.POST,
            "http://example.com/outages",
            body=json.dumps({}),
            status=200,
            content_type="application/json",
        )
        yield rsps_success


@pytest.fixture()
def mock_site_info_endpoint():
    with responses.RequestsMock() as rsps_success:
        rsps_success.add(
            responses.GET,
            f"http://example.com/site-info/{test_site_id}",
            body=json.dumps(test_site_info_data),
            status=200,
            content_type="application/json",
        )
        yield rsps_success
