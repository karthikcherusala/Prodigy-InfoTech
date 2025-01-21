def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts a message using the Caesar Cipher algorithm.

    :param text: The input message to encrypt or decrypt.
    :param shift: The number of positions to shift (key).
    :param mode: Either 'encrypt' or 'decrypt'.
    :return: The resulting encrypted or decrypted message.
    """
    result = ''

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():  # Check if the character is a letter
            start = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using modulo
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char  # Non-alphabetic characters remain unchanged

    return result


def main():
    print("Caesar Cipher Encryption and Decryption")
    while True:
        mode = input("Choose mode (encrypt/decrypt/exit): ").strip().lower()
        if mode == 'exit':
            print("Exiting program. Goodbye!")
            break
        elif mode not in ['encrypt', 'decrypt']:
            print("Invalid mode. Please enter 'encrypt', 'decrypt', or 'exit'.")
            continue

        text = input("Enter your message: ")
        try:
            shift = int(input("Enter the shift value (integer): "))
        except ValueError:
            print("Invalid input. Shift value must be an integer.")
            continue

        result = caesar_cipher(text, shift, mode)
        print(f"Result ({mode}ed text): {result}\n")


if __name__ == "__main__":
    main()
