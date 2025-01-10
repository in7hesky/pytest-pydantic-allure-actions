import os
from data.urls import Urls


class UrlResolver:

    __HOST = None

    @classmethod
    def resolve(cls) -> str:
        if cls.__HOST is not None:
            return cls.__HOST

        cls.__HOST = Urls.URL_PROD.value if cls.is_prod() \
            else Urls.URL_DEV.value
        return cls.__HOST

    @staticmethod
    def is_prod() -> bool:
        return os.getenv("STAGE") == "prod"
