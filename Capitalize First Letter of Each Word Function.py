def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

# Example usage
print(capitalize_words("hi"))  # "Hi"
print(capitalize_words("i love programming"))  # "I Love Programming"
