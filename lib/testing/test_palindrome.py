import pytest
from lib.palindrome import longest_palindromic_substring


# -------------------------
# BASIC CASES
# -------------------------

@pytest.mark.parametrize("input_str, expected", [
    ("babad", ["bab", "aba"]),      # odd-length
    ("cbbd", ["bb"]),               # even-length
    ("racecar", ["racecar"]),       # entire string
    ("level", ["level"]),           # another full palindrome
])
def test_basic_cases(input_str, expected):
    result = longest_palindromic_substring(input_str)
    assert result in expected


# -------------------------
# EDGE CASES
# -------------------------

def test_single_character():
    assert longest_palindromic_substring("a") == "a"


def test_two_characters_same():
    assert longest_palindromic_substring("aa") == "aa"


def test_two_characters_different():
    result = longest_palindromic_substring("ab")
    assert result in ["a", "b"]


def test_all_same_characters():
    assert longest_palindromic_substring("aaaaaa") == "aaaaaa"


def test_no_palindrome_longer_than_one():
    result = longest_palindromic_substring("abcdefg")
    assert len(result) == 1
    assert result in list("abcdefg")


def test_empty_string():
    assert longest_palindromic_substring("") == ""


# -------------------------
# BOUNDARY CASES (CONSTRAINTS)
# -------------------------

def test_minimum_length_boundary():
    # length = 1 (minimum allowed by constraint)
    assert longest_palindromic_substring("x") == "x"


def test_maximum_length_boundary():
    # length = 1000 (maximum allowed by constraint)
    s = "a" * 1000
    result = longest_palindromic_substring(s)
    assert result == s


# -------------------------
# FAILURE CASES
# -------------------------

def test_non_string_input():
    with pytest.raises(TypeError):
        longest_palindromic_substring(123)


def test_none_input():
    with pytest.raises(TypeError):
        longest_palindromic_substring(None)


def test_list_input():
    with pytest.raises(TypeError):
        longest_palindromic_substring(["a", "b"])