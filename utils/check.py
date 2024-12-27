from pydantic import BaseModel


class Check:

    @classmethod
    def all_fields_are_equal(cls, dict1: dict, dict2: dict):
        cls.__check_dicts_not_empty(dict1, dict2)
        if len(dict1) != len(dict2):
            raise ValueError("Dicts must be of equal len")

        for k in dict1.keys():
            assert dict1[k] == dict2[k]

    @classmethod
    def target_fields_are_equal(cls, dict1: dict, dict2: dict, *args: str):
        cls.__check_dicts_not_empty(dict1, dict2)

        for a in args:
            if not isinstance(a, str):
                raise ValueError("Bad argument")
            assert dict1[a] == dict2[a]

    @staticmethod
    def object_is_valid(target: object, model_class: type[BaseModel]):
        model_class.model_validate(target)

    @staticmethod
    def __check_dicts_not_empty(*args: dict):
        for d in args:
            if not isinstance(d, dict):
                raise ValueError("Dict argument expected")
            if len(d) == 0:
                raise ValueError("Dict must not be empty")
