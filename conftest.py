import os
import requests
import pytest
from utils.url_resolver import UrlResolver as Url

@pytest.fixture(scope="session", autouse=True)
def setup_env():
    requests.post(
        url=f"{Url.resolve()}/setup",
        headers={"Authorization": f"Bearer {os.environ["API_TOKEN"]}"}
    )
