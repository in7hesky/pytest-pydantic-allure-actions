import allure
import requests
from requests import Response

from data.headers import Headers
from models.response.created_user_model import CreatedUserModel
from services.users.endpoints import Endpoints
from utils.decorators import attach_response, validate_response


class UsersService:

    def __init__(self):
        self.endpoints = Endpoints()
        self.headers = Headers()

    @validate_response(CreatedUserModel)
    @attach_response
    @allure.step("Create user with payload")
    def create_user_with_payload(self, payload: dict) -> Response:
        response =  requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic_auth,
            json=payload
        )

        return response
