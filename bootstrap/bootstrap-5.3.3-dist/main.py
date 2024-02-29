def isPalindrome(x):
        original_number = x
        reversed_number = 0
        while x > 0:
            digit = x % 10
            #print(digit)
            reversed_number = reversed_number * 10 + digit
            x //= 10
            print(reversed_number)
        print(x)
        if original_number == reversed_number:
              return True
        else:
              return False
        
print(isPalindrome(122))