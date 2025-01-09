import requests
import allure
from requests import Response

from services.base_service import BaseService
from services.games.games_endpoints import GamesEndpoints
from utils.decorators import attach_response


class GamesService(BaseService):

    def __init__(self):
        super().__init__()
        self.endpoints = GamesEndpoints

    @attach_response
    @allure.step("Get users list")
    def get_games_list(self) -> Response:
        return requests.get(
            url=self.endpoints.get_games_list,
            headers=self.headers.basic_auth
        )
