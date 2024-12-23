import requests
from services.users.data.payloads import Payloads
from services.users.data.endpoints import Endpoints
from config.headers import Headers


class UsersService:

    def __init__(self):
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    def create_user(self):
        print(self.endpoints.create_user)
        return requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic_auth,
            json=self.payloads.create_user
        )
