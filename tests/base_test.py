import pytest
from services.users.users_service import UsersService
from services.games.games_service import GamesService
from utils.check import Check


class BaseTest:

    check: Check

    users_service: UsersService
    games_service: GamesService

    @pytest.fixture(autouse=True)
    def setup(self):
        self.check = Check

        self.users_service = UsersService()
        self.games_service = GamesService()
