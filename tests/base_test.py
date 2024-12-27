import pytest
from services.users.users_service import UsersService
from utils.check import Check


class BaseTest:

    check: Check

    users_service: UsersService

    @pytest.fixture(autouse=True)
    def setup(self):
        self.check = Check

        self.users_service = UsersService()
