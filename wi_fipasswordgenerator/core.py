#!/usr/bin/env python

# Imports
import string
from random import choice  # Import 'choice' only.


# Function definitions
# Input size always between 8 and 63.
def verify_input_size(size_input):
    return max(8, min(size_input, 63))


# Whether to use hard or easy characters to type or copy
def verify_characters(characters_input):
    # return "easy" if characters_input == 1 else "hard"
    return easy_characters if characters_input == 0 else hard_characters


# Generate password with the strings below.
def generate_password(size_input=63, chars=1):
    return "".join(choice(verify_characters(chars)) for _ in range(size_input))
    # return "".join(choice(hard_characters) for _ in range(size_input))


# Why easy characters:
# \, " and ' may be hard to type or copy in some keyboards;
# |, I and l are hard to differ in some modern or not monospaced fonts.


# easy_characters = "e" # replacing I and l for "" and leaving | out of the list.
easy_characters = (
    string.ascii_letters.replace("I", "").replace("l", "")
    + string.digits
    + "!@#$%^&*()-_=+[]{};:,.<>/?"
)

# All characters.
# hard_characters = "h"
hard_characters = string.ascii_letters + string.digits + string.punctuation + " "

if __name__ == "__main__":

    # Input handling
    size_input = int(
        input("Type the password size you want between 8 and 63 characters: ")
    )

    characters_input = int(input("0 - Easy Characters:\n1 - Hard Characters: "))

    # Validate input size
    validated_size = verify_input_size(size_input)

    # Function application
    print(generate_password(validated_size))
