import requests


def test_basic_math():
    assert 1 + 1 == 2


def test_requests_importable():
    # Just confirms the dependency installed correctly
    assert requests.__name__ == "requests"
