import requests
from requests import Response
from services.users.data.payloads import Payloads
from services.users.data.endpoints import Endpoints
from config.headers import Headers
from models.users.user_model import UserModel


class UsersService:

    def __init__(self):
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    def create_user(self) -> Response:
        response =  requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic_auth,
            json=self.payloads.create_user
        )

        UserModel.model_validate(response.json())

        return response
