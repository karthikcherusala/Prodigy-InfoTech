# Caesar Cipher Encryption and Decryption

This Python program allows you to encrypt and decrypt messages using the Caesar Cipher algorithm. The Caesar Cipher is a simple substitution cipher that shifts the letters of the alphabet by a specified number of positions.

## Features
- **Encryption**: Input a message and shift value to encrypt the text.
- **Decryption**: Input an encrypted message and shift value to recover the original text.
- Handles both uppercase and lowercase letters.
- Leaves non-alphabetic characters unchanged.

## How It Works
### Encryption:
Each letter in the text is shifted forward in the alphabet by the specified shift value.

*Example:* With a shift of `3`, `A` becomes `D`, `B` becomes `E`, etc.

### Decryption:
Each letter in the text is shifted backward in the alphabet by the specified shift value.

*Example:* With a shift of `3`, `D` becomes `A`, `E` becomes `B`, etc.

## Usage
### Prerequisites
Python 3.x installed on your system.

### Steps to Run
1. Clone or download this repository.
2. Navigate to the directory containing the script.
3. Run the script:
   ```
   python caesar_cipher.py
   ```
4. Follow the prompts to:
   - Choose the mode: `encrypt`, `decrypt`, or `exit`.
   - Enter the message.
   - Specify the shift value (integer).

### Example
#### Encryption:
**Input:**
- Message: `Hello, World!`
- Shift: `3`

**Output:** `Khoor, Zruog!`

#### Decryption:
**Input:**
- Encrypted Message: `Khoor, Zruog!`
- Shift: `3`

**Output:** `Hello, World!`

## Program Overview
### Function: `caesar_cipher`
This function performs both encryption and decryption based on the mode:

- **Parameters:**
  - `text`: The input message (string).
  - `shift`: The shift value (integer).
  - `mode`: Either `encrypt` or `decrypt`.
- **Returns:** The processed text (string).

### Main Function
Provides an interactive interface to choose modes, input messages, and shift values.

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

## Contributions
Contributions are welcome! If you encounter any issues or have ideas for improvements, please open an issue or create a pull request.

---

*Happy encrypting and decrypting!*
