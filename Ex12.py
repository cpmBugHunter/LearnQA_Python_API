import pytest
import requests

from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestCookies(BaseCase):

    url = "https://playground.learnqa.ru/api/homework_header"
    response = requests.get(url)

    def test_endpoint_returns_header(self):
        assert bool(self.response.headers), f"Headers was empty"
        headers_as_dict = self.response.headers.items()
        print(headers_as_dict)

    def test_header_has_correct_value(self):
        header = self.get_header(self.response, 'x-secret-homework-header')
        expected = "Some secret value"
        assert header == expected, f"Expected header value: {expected}, actual value was: {header}"

