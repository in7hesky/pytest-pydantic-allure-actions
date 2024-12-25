import json
from functools import wraps
import allure
from pydantic import BaseModel
from allure_commons.types import AttachmentType


def attach_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)

        allure.attach(body=json.dumps(response.json(), indent=4), \
                      name="API Response", \
                      attachment_type=AttachmentType.JSON)

        return response

    return wrapper

def validate_response(model_class: type[BaseModel]):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)

            model_class.model_validate(response.json())

            return response

        return wrapper

    return decorator
