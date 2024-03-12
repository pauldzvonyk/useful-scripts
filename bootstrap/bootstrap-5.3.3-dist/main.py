# Palindrome function without the string method.
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
