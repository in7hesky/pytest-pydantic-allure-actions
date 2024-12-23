from utils.url_resolver import UrlResolver as Url


class Endpoints:

    __HOST = Url.resolve()
    create_user = f"{__HOST}/users"
    get_users_list = f"{__HOST}/users"
    get_user_by_uuid = lambda self, uuid: f"{self.__HOST}/users/{uuid}"
