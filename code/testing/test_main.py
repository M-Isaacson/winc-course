import main


def test_get_none():
    assert main.get_none() == None


def test_flatten_dict():
    test_dict = {"a": 2, "b": 4, "c": {"d": 1, "e": 3}, "f": 5, "g": {"h": 6, "i": {"j": 7, "k": 8, "l": {"m": 9}}}}
    assert type(main.flatten_dict(test_dict)) == list
    assert main.flatten_dict(test_dict) != []
    for value in main.flatten_dict(test_dict):
        assert type(value) != str
