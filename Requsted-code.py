# Requsted-code.py
def is_palindrome(num):
    # Convert the number to a string
    num_str = str(num)
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

# Unit tests
def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(-121) == False  # Negative numbers aren't palindromes
    assert is_palindrome(10) == False
    assert is_palindrome(12321) == True
    assert is_palindrome(0) == True
    assert is_palindrome(123456) == False
    assert is_palindrome(123454321) == True
    assert is_palindrome(99999) == True
    assert is_palindrome(1001) == True
    assert is_palindrome(123456789987654321) == True
    
test_is_palindrome()