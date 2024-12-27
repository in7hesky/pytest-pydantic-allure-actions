from tests.abstract.base_test import BaseTest
from utils.assertions import assert_fields_are_equal


class TestUsersService(BaseTest):

    def test_create_user(self, valid_user_payload):
        response = self.users_service \
            .create_user_with_payload(valid_user_payload)

        assert response.status_code == 200
        assert_fields_are_equal(response.json(), valid_user_payload, \
                                "email", "name", "nickname")
