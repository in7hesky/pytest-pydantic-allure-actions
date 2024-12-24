from tests.abstract.base_test import BaseTest
from data.payloads.users_payloads import UsersPayloads
from utils.assertions import assert_fields_are_equal


class TestUsersService(BaseTest):

    def test_create_user(self):
        user_payload = UsersPayloads.get_random_valid_user()

        response = self.users_service \
            .create_user_with_payload(user_payload)

        assert response.status_code == 200
        assert_fields_are_equal(response.json(), user_payload, \
                                "email", "name", "nickname")
