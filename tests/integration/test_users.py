from tests.abstract.base_test import BaseTest


class TestUsersService(BaseTest):

    def test_create_user(self):
        response = self.users_service.create_user()
        print(response.json())
        assert response.status_code == 200, response.json()

