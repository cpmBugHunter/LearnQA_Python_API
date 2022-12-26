import pytest


class TestUserInput:

    def test_check_input_length(self):
        phrase = input('Enter a phrase less than 15 symbols: ')
        assert len(phrase) < 15, f"You entered {len(phrase)} symbols"
