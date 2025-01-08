import itertools
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_digits = input("Include digits? (y/n): ").lower() == 'y'
include_symbols = input("Include special symbols? (y/n): ").lower() == 'y'

characters = ''
if include_lowercase:
    characters += lowercase
if include_uppercase:
    characters += uppercase
if include_digits:
    characters += digits
if include_symbols:
    characters += symbols

password_length = int(input("Enter password length: "))
file_path = input("Enter the file path to save the password dictionary: ")

with open(file_path, 'w') as f:
    for password in itertools.product(characters, repeat=password_length):
        f.write(''.join(password) + '\n')
