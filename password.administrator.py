import random
import string
import pyperclip  # Install with `pip install pyperclip`

def generate_password(length=12, use_hyphens=True):
    """
    Generates a strong password containing lowercase, uppercase, digits, and special characters.
    Optionally inserts hyphens every 4 characters for readability.

    Parameters:
        length (int): Desired password length (excluding hyphens). Minimum is 8.
        use_hyphens (bool): If True, includes hyphens every 4 characters.

    Returns:
        str: Generated password (with hyphens if option selected).
    
    Raises:
        ValueError: If length is less than 8.
    """
    if length < 8:
        raise ValueError("Password length must be at least 8 characters for best security.")
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*?/+=_-><."
    all_chars = lowercase + uppercase + digits + special_chars

    # Ensure at least one character of each type
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    password_chars += random.choices(all_chars, k=length - 4)
    random.shuffle(password_chars)

    raw = ''.join(password_chars)

    if use_hyphens:
        # Insert hyphens every 4 characters
        formatted = '-'.join(raw[i:i+4] for i in range(0, len(raw), 4))
        return formatted
    else:
        return raw

def check_password_strength(password):
    """
    Evaluates the strength of an existing password.
    Returns a score (0–5) and a dict indicating which criteria are missing.
    """
    length_error = len(password) < 8
    lowercase_error = not any(c.islower() for c in password)
    uppercase_error = not any(c.isupper() for c in password)
    digit_error = not any(c.isdigit() for c in password)
    special_error = not any(c in "!@#$%^&*?/+=_-" for c in password)

    errors = {
        "Length insufficient": length_error,
        "Missing lowercase letter": lowercase_error,
        "Missing uppercase letter": uppercase_error,
        "Missing digit": digit_error,
        "Missing special character": special_error,
    }

    score = 5 - sum(errors.values())
    return score, errors

def main():
    print("Welcome to the Password Generator tool!")
    print("Options:")
    print("1. Check Current Password Strength.")
    print("2. Generate a Unique Strong Password.")

    choice = input("Choose 1 or 2: ").strip()
    if choice == "1":
        pwd = input("Enter your password: ")
        score, issues = check_password_strength(pwd)
        print(f"Password Strength: {score}/5")
        for issue, has_error in issues.items():
            if has_error:
                print(f"- {issue}")

    elif choice == "2":
        try:
            length = int(input("Enter desired password length (minimum 8): "))
        except ValueError:
            print("Invalid number. Exiting.")
            return

        hyphens_choice = input("Insert hyphens every 4 chars for readability? (Y/N): ").strip().lower()
        use_hyphens = hyphens_choice in ("y", "yes")

        pwd = generate_password(length, use_hyphens)
        print(f"\nGenerated password:\n{pwd}")

        if input("Copy to clipboard? (Y/N): ").strip().lower() in ("y", "yes"):
            pyperclip.copy(pwd)
            print("✅ Password copied to clipboard!")
        else:
            print("❌ Not copied.")

    else:
        print("Invalid option. Restart and choose 1 or 2.")

if __name__ == "__main__":
    main()

