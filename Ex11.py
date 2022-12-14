import pytest
import requests

from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestCookies(BaseCase):

    url = "https://playground.learnqa.ru/api/homework_cookie"
    response = requests.get(url)

    def test_endpoint_returns_cookie(self):
        assert bool(self.response.cookies), f"Cookies was empty"
        for c in self.response.cookies:
            print(f"Cookie: {c.name}; Value: {c.value}")

    def test_cookie_has_correct_value(self):
        cookie = self.get_cookie(self.response, 'HomeWork')
        expected = "hw_value"
        assert cookie == expected, f"Expected cookie value: {expected}, actual value was: {cookie}"

