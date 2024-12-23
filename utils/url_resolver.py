import os
from config.urls import Urls


class UrlResolver:

    @classmethod
    def resolve(cls) -> str:
        return Urls.URL_PROD if cls.is_prod() else Urls.URL_DEV

    @staticmethod
    def is_prod() -> str | None:
        return os.getenv("STAGE") == "prod"
