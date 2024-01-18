import string
import random


class PasswordGenerator:
    def __init__(self):
        self.characters = string.ascii_letters
        self.nums = string.digits
        self.specials = string.punctuation

    def generate_password(self, min_length, digits=True, special_characters=True):
        characters = self.characters
        if digits:
            characters += self.nums
        if special_characters:
            characters += self.specials

        psw = ""

        while len(psw) < min_length:
            for char in random.choice(self.characters):
                psw += char

        return psw


if __name__ == '__main__':
    password_generator = PasswordGenerator()
    while True:
        try:
            length = int(input("How long would you like your password to be: "))
            has_digits = input("Do you want to include digits (y/n)? ").lower() == "y"
            has_special_characters = input("Do you want to include special characters (y/n)? ").lower() == "y"
            password = password_generator.generate_password(length, has_digits, has_special_characters)
            print(password)
            break
        except ValueError:
            print("Incorrect password length.")
