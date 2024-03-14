"""The following code is divided in 2 methods, the first one is comparing an actual
int numbers, the second is dealing with a string, which is more direct, faster and simple.
It's up to you to decide which one is more appropriate for your use case."""
# Function without the string method.
def isPalindrome(x):
    original_number = x
    reversed_number = 0
    while x > 0:
        digit = x % 10
        # print(digit)
        reversed_number = reversed_number * 10 + digit
        x //= 10
    if original_number == reversed_number:
        return True
    else:
        return False


print(isPalindrome(121))


# Transfotming int into string.
def is_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False


print(is_palindrome(151))
