import pytest


@pytest.fixture
def valid_user_payload(faker):
    return {
        "email": faker.email(),
        "password": faker.password(),
        "name": faker.first_name(),
        "nickname": faker.user_name()
    }
