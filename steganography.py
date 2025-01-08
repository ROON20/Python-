from PIL import Image
import os

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary_string):
    return ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8))

def encrypt_image(image_path, text, save_dir="/home/roni/Download"):
    binary_text = text_to_binary(text) + '1111111111111110'  # End delimiter
    img = Image.open(image_path)
    width, height = img.size

    if len(binary_text) > width * height * 3:
        raise ValueError("Image is too small to hold the text.")

    encoded_img = img.copy()
    data_index = 0

    for y in range(height):
        for x in range(width):
            pixel = list(encoded_img.getpixel((x, y)))
            for i in range(3):
                if data_index < len(binary_text):
                    pixel[i] = (pixel[i] & ~1) | int(binary_text[data_index])
                    data_index += 1
            encoded_img.putpixel((x, y), tuple(pixel))
            if data_index >= len(binary_text):
                break

    # Ensure the save directory exists
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    save_path = os.path.join(save_dir, "encrypted_image.png")
    encoded_img.save(save_path)
    print(f"Image encrypted and saved as '{save_path}'.")

def decrypt_image(image_path):
    img = Image.open(image_path)
    binary_text = ""
    width, height = img.size

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            for i in range(3):
                binary_text += str(pixel[i] & 1)

    binary_text = binary_text.split('1111111111111110')[0]
    return binary_to_text(binary_text)

def main():
    choice = input("Enter your choice (1 for Encrypt, 2 for Decrypt): ")

    if choice == '1':
        image_path = input("Enter the image path: ")
        text = input("Enter the text to hide: ")
        encrypt_image(image_path, text)
    elif choice == '2':
        image_path = input("Enter the encrypted image path: ")
        decrypted_text = decrypt_image(image_path)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice, please enter 1 or 2.")

if __name__ == "__main__":
    main()
