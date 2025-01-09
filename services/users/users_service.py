import allure
import requests
from requests import Response

from services.base_service import BaseService
from services.users.users_endpoints import UsersEndpoints
from utils.decorators import attach_response


class UsersService(BaseService):

    def __init__(self):
        super().__init__()
        self.endpoints = UsersEndpoints()

    @attach_response
    @allure.step("Create user with payload")
    def create_user_with_payload(self, payload: dict) -> Response:
        response =  requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic_auth,
            json=payload
        )

        return response
