import pytest
from services.users.users_service import UsersService


class BaseTest:

    users_service: UsersService

    @pytest.fixture(autouse=True)
    def setup(self):
        self.users_service = UsersService()
