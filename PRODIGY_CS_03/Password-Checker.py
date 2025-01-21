import re

def assess_password_strength(password):
    """
    Assess the strength of a password based on predefined criteria.

    :param password: The password string to evaluate.
    :return: A tuple containing the strength score and feedback message.
    """
    score = 0
    feedback = []

    # Length criteria
    if len(password) >= 12:
        score += 2
        feedback.append("Good length.")
    elif len(password) >= 8:
        score += 1
        feedback.append("Moderate length. Consider making it longer.")
    else:
        feedback.append("Too short. Use at least 8 characters.")

    # Uppercase letter criteria
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("Contains uppercase letters.")
    else:
        feedback.append("Add uppercase letters for better security.")

    # Lowercase letter criteria
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("Contains lowercase letters.")
    else:
        feedback.append("Add lowercase letters for better security.")

    # Number criteria
    if re.search(r'\d', password):
        score += 1
        feedback.append("Contains numbers.")
    else:
        feedback.append("Add numbers to strengthen your password.")

    # Special character criteria
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
        feedback.append("Contains special characters.")
    else:
        feedback.append("Add special characters to make your password stronger.")

    # Final evaluation
    if score >= 5:
        strength = "Strong"
    elif 3 <= score < 5:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

def main():
    print("Password Strength Assessment Tool")
    while True:
        password = input("Enter a password to assess (or type 'exit' to quit): ").strip()
        if password.lower() == 'exit':
            print("Exiting program. Goodbye!")
            break

        strength, feedback = assess_password_strength(password)
        print(f"\nPassword Strength: {strength}")
        print("Feedback:")
        for comment in feedback:
            print(f"- {comment}")
        print()

if __name__ == "__main__":
    main()
