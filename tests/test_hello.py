from hello import greet


def test_greet_with_name():
    assert greet("Furina") == "Hello, Furina!"


def test_greet_without_name():
    assert greet("") == "Hello, World!"
