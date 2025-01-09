import allure

from tests.base_test import BaseTest


@allure.feature("Games Service")
class TestGamesService(BaseTest):

    def test_get_users_list(self):
        response = self.games_service.get_games_list()

        assert response.status_code == 200
        assert response.json()["meta"]["total"] == 10
