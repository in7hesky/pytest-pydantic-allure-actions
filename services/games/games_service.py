import requests
from requests import Response

from services.base_service import BaseService
from services.games.games_endpoints import GamesEndpoints


class GamesService(BaseService):

    def __init__(self):
        super().__init__()
        self.endpoints = GamesEndpoints

    def get_games_list(self) -> Response:
        return requests.get(
            url=self.endpoints.get_games_list,
            headers=self.headers.basic_auth
        )
