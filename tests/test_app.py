"""Tests for app.py - you'll add more!"""

from app import add, is_even, reverse_string, multiply


class TestMath:
    """Tests for math functions."""

    def test_add_positive(self):
        assert add(2, 3) == 5

    def test_add_negative(self):
        assert add(-1, -1) == -2


class TestStrings:
    """Tests for string functions."""

    def test_reverse(self):
        assert reverse_string("hello") == "olleh"

    def test_is_even(self):
        assert is_even(4) is True
        assert is_even(3) is False

class TestMul:
    """test for multiplications"""

    def test_mul_positive(self):
        assert multiply(2, 3) == 6

    def test_mul_negative(self):
        assert multiply(2, -6) == -12

    def test_mul_zero(self):
        assert multiply(2, 0) == 0
    