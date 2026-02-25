import pytest
from lib.palindrome import longest_palindromic_substring


@pytest.mark.parametrize("input_str, expected", [
    ("babad", ["bab", "aba"]),
    ("cbbd", ["bb"]),
    ("racecar", ["racecar"]),
])
def test_basic_cases(input_str, expected):
    result = longest_palindromic_substring(input_str)
    assert result in expected


def test_single_character():
    assert longest_palindromic_substring("a") == "a"


def test_two_different_characters():
    result = longest_palindromic_substring("ac")
    assert result in ["a", "c"]


def test_all_same_characters():
    assert longest_palindromic_substring("aaaa") == "aaaa"


def test_no_palindrome_longer_than_one():
    result = longest_palindromic_substring("abcde")
    assert len(result) == 1


def test_empty_string():
    assert longest_palindromic_substring("") == ""


def test_non_string_input():
    with pytest.raises(TypeError):
        longest_palindromic_substring(123)