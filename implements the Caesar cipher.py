def caesar_cipher(msg, shift, fn):
    result = ""  # Initialize result as an empty string

    # Iterate over each character in the message
    for char in msg:
        if char.isalpha():  # Check if the character is a letter
            if char.isupper():
                if fn == "e":
                    result += chr((ord(char) + shift - 65) % 26 + 65)
                elif fn == "d":
                    result += chr((ord(char) - shift - 65) % 26 + 65)
            elif char.islower():
                if fn == "e":
                    result += chr((ord(char) + shift - 97) % 26 + 97)
                elif fn == "d":
                    result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # Directly add non-alphabetic characters
            result += char

    return result

# Get user input
msg = input("Enter your message: ")
shift = int(input("Enter shift value: "))  # Convert shift to integer
fn = input('Enter "e" to encrypt\nEnter "d" to decrypt\n: ').strip().lower()

if fn in ["e", "d"]:
    result = caesar_cipher(msg, shift, fn)
    print(f"The result is: {result}")  # Corrected f-string formatting
else:
    print('Enter a valid function: "e" or "d"')
