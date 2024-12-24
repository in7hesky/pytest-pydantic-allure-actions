def assert_fields_are_equal(target1: dict, target2: dict, *args: str):
    for a in args:
        if not isinstance(a, str):
            raise ValueError("Bad argument")
        assert target1[a] == target2[a]
