# Image Encryption Tool

This Python script provides a simple tool to encrypt and decrypt images using basic pixel manipulation techniques. The program modifies the RGB values of an image by applying a mathematical operation with a user-specified key.

## Features
- **Encryption**: Adds a key to the pixel values and wraps them using modulo 256.
- **Decryption**: Reverses the encryption process by subtracting the key from pixel values.
- Supports images in common formats such as PNG, JPEG, BMP, etc.

## How It Works
1. **Encryption**:
   - Each pixel's RGB values are increased by the encryption key.
   - The values wrap around using modulo 256 to ensure they stay valid.

2. **Decryption**:
   - Each pixel's RGB values are decreased by the encryption key.
   - The values wrap around using modulo 256 to reverse the encryption.

## Prerequisites
- Python 3.x
- Install the required library using pip:
  ```bash
  pip install pillow
  ```

## Usage
### Steps to Run
1. Clone or download this repository.
2. Navigate to the directory containing the script.
3. Run the script:
   ```bash
   python image_encryption_tool.py
   ```
4. Choose an option: `encrypt`, `decrypt`, or `exit`.
5. Provide the required inputs:
   - Path to the input image file.
   - Path to save the output image.
   - Encryption/Decryption key (integer).

### Example
#### Encryption:
- Input:
  - Image: `input.png`
  - Key: `50`
- Output:
  - Encrypted Image: `encrypted_output.png`

#### Decryption:
- Input:
  - Image: `encrypted_output.png`
  - Key: `50`
- Output:
  - Decrypted Image: `output.png` (identical to `input.png`)

## Code Overview
### Functions
1. **`encrypt_image`**:
   - Encrypts the image by adding the key to the pixel values.
   - Saves the encrypted image to the specified output path.

2. **`decrypt_image`**:
   - Decrypts the image by subtracting the key from the pixel values.
   - Saves the decrypted image to the specified output path.

3. **`main`**:
   - Provides an interactive interface for users to select encryption or decryption and provide inputs.

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

## Contributions
Contributions are welcome! If you encounter any issues or have ideas for improvements, please open an issue or submit a pull request.

---

Happy Encrypting and Decrypting!
