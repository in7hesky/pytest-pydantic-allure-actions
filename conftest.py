import os
import requests
import pytest
from dotenv import load_dotenv

load_dotenv()

HOST = "https://release-gs.qa-playground.com/api/v1" \
        if os.getenv("STAGE") == "prod" \
        else "https://dev-gs.qa-playground.com/api/v1"


@pytest.fixture(scope="session", autouse=True)
def setup_env():
    response = requests.post(
        url=f"{HOST}/setup",
        headers={"Authorization": f"Bearer {os.environ["API_KEY"]}"}
    )
