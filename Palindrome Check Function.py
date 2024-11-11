def is_palindrome(s):
    # Remove spaces and convert to lowercase for comparison
    clean_s = ''.join(s.split()).lower()
    return clean_s == clean_s[::-1]

# Example usage
print(is_palindrome("madam"))  # True
print(is_palindrome("nurses run"))  # True
print(is_palindrome("hello"))  # False
