import string
import random


class PasswordGenerator:
    def __init__(self):
        """
        Initializes the PasswordGenerator object with default character sets for letters, numbers, and special characters.
        """
        self.characters = string.ascii_letters
        self.nums = string.digits
        self.specials = string.punctuation

    def generate_password(self, min_length, digits=True, special_characters=True):
        """
        Generates a random password based on specified criteria.

        Parameters:
        - min_length (int): Minimum length of the generated password.
        - digits (bool): Whether to include digits in the password (default is True).
        - special_characters (bool): Whether to include special characters in the password (default is True).

        Returns:
        - str: The generated password.

        Note: The password will include letters by default, and it may include digits and special characters based on the provided criteria.
        """
        characters = self.characters

        # Include digits in the character set if specified
        if digits:
            characters += self.nums

        # Include special characters in the character set if specified
        if special_characters:
            characters += self.specials

        psw = ""

        # Continue adding random characters to the password until the desired length is reached
        while len(psw) < min_length:
            psw += random.choice(characters)

        return psw


if __name__ == '__main__':
    # Create an instance of the PasswordGenerator class
    password_generator = PasswordGenerator()

    while True:
        try:
            # Get user input for password length and criteria
            length = int(input("How long would you like your password to be: "))
            has_digits = input("Do you want to include digits (y/n)? ").lower() == "y"
            has_special_characters = input("Do you want to include special characters (y/n)? ").lower() == "y"

            # Generate and print the password based on user input
            password = password_generator.generate_password(length, has_digits, has_special_characters)
            print("Generated Password:", password)
            break
        except ValueError:
            print("Incorrect password length.")
