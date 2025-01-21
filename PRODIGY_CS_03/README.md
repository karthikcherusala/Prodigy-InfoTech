# Password Strength Assessment Tool

This Python script evaluates the strength of a password based on multiple criteria, such as length, the presence of uppercase and lowercase letters, numbers, and special characters. It provides feedback to help users create stronger passwords.

## Features
- **Comprehensive Evaluation**: Checks the password against key security criteria:
  - Length
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- **Feedback**: Offers actionable suggestions to improve password strength.
- **Simple to Use**: Enter a password, and receive an instant assessment.

## Prerequisites
- Python 3.x installed on your system.

## Usage
### Steps to Run
1. Clone or download this repository.
2. Navigate to the directory containing the script.
3. Run the script using:
   ```bash
   python password_strength_tool.py
   ```
4. Enter a password when prompted. Type `exit` to quit the program.

### Example
#### Input:
```
Enter a password to assess (or type 'exit' to quit): MyP@ssw0rd123
```

#### Output:
```
Password Strength: Strong
Feedback:
- Good length.
- Contains uppercase letters.
- Contains lowercase letters.
- Contains numbers.
- Contains special characters.
```

#### Weak Password Example:
```
Enter a password to assess (or type 'exit' to quit): pass123
```

Output:
```
Password Strength: Weak
Feedback:
- Moderate length. Consider making it longer.
- Add uppercase letters for better security.
- Contains lowercase letters.
- Contains numbers.
- Add special characters to make your password stronger.
```

## Criteria Breakdown
- **Strong Password**: Meets all criteria with a score of 5.
- **Moderate Password**: Meets 3-4 criteria.
- **Weak Password**: Meets less than 3 criteria.

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

## Contributions
Contributions are welcome! If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

---

**Stay secure by creating strong passwords!**
