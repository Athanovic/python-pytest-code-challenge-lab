def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring.
    """
    # Handle edge cases
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    n = len(s)

    # If string is empty or single character
    if n < 2:
        return s

    start = 0
    max_len = 1

    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(n):
        # Odd length palindrome
        len1 = expand_around_center(i, i)
        # Even length palindrome
        len2 = expand_around_center(i, i + 1)

        max_curr_len = max(len1, len2)

        if max_curr_len > max_len:
            max_len = max_curr_len
            start = i - (max_len - 1) // 2

    return s[start:start + max_len]