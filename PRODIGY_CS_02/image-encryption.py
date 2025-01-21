from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    """
    Encrypt an image by applying a mathematical operation to pixel values.

    :param input_path: Path to the input image.
    :param output_path: Path to save the encrypted image.
    :param key: Integer key used for encryption.
    """
    try:
        # Open the image and convert it to RGB mode
        img = Image.open(input_path).convert('RGB')
        img_array = np.array(img)

        # Apply encryption (add the key to each pixel value and wrap around using modulo)
        encrypted_array = (img_array + key) % 256

        # Save the encrypted image
        encrypted_img = Image.fromarray(encrypted_array.astype('uint8'), 'RGB')
        encrypted_img.save(output_path)
        print(f"Encrypted image saved at {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def decrypt_image(input_path, output_path, key):
    """
    Decrypt an image by reversing the encryption operation.

    :param input_path: Path to the encrypted image.
    :param output_path: Path to save the decrypted image.
    :param key: Integer key used for decryption.
    """
    try:
        # Open the image and convert it to RGB mode
        img = Image.open(input_path).convert('RGB')
        img_array = np.array(img)

        # Apply decryption (subtract the key from each pixel value and wrap around using modulo)
        decrypted_array = (img_array - key) % 256

        # Save the decrypted image
        decrypted_img = Image.fromarray(decrypted_array.astype('uint8'), 'RGB')
        decrypted_img.save(output_path)
        print(f"Decrypted image saved at {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Image Encryption Tool")
    while True:
        choice = input("Choose an option (encrypt/decrypt/exit): ").strip().lower()
        if choice == 'exit':
            print("Exiting program. Goodbye!")
            break
        elif choice not in ['encrypt', 'decrypt']:
            print("Invalid choice. Please choose 'encrypt', 'decrypt', or 'exit'.")
            continue

        input_path = input("Enter the path to the input image: ").strip()
        output_path = input("Enter the path to save the output image: ").strip()
        try:
            key = int(input("Enter the encryption/decryption key (integer): "))
        except ValueError:
            print("Invalid key. Please enter an integer.")
            continue

        if choice == 'encrypt':
            encrypt_image(input_path, output_path, key)
        elif choice == 'decrypt':
            decrypt_image(input_path, output_path, key)

if __name__ == "__main__":
    main()
