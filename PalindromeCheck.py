def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome.

    Args:
    s (str): The string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    return s == s[::-1]

if __name__ == '__main__':
    # Example usage
    test_string = "A man, a plan, a canal, Panama"
    print(f"The string '{test_string}' is a palindrome: {is_palindrome(test_string)}")