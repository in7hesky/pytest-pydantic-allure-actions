import allure
import requests
from requests import Response

from data.headers import Headers
from data.models.users.user_model import UserModel
from data.payloads.users_payloads import UsersPayloads
from services.users.data.endpoints import Endpoints


class UsersService:

    def __init__(self):
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Create user with random user payload")
    def create_user(self) -> Response:
        response =  requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic_auth,
            json=UsersPayloads.create_user()
        )

        UserModel.model_validate(response.json())

        return response
