import allure

from tests.base_test import BaseTest
from models.created_user_model import CreatedUserModel


@allure.feature("Users Service")
class TestUsersService(BaseTest):

    def test_create_user(self, valid_user_payload):
        response = self.users_service \
            .create_user_with_payload(valid_user_payload)

        assert response.status_code == 200
        self.check.target_fields_are_equal(
            response.json(), valid_user_payload, "email", "name", "nickname")
        self.check.object_is_valid(response.json(), CreatedUserModel)
