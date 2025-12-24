import re

def validate_email(email):
    """
    Validates an email address using a basic regular expression pattern.
    Aims to cover common email formats.
    """
    # This regular expression is a common pattern for email validation.
    # It checks for:
    # 1. Start of string (^)
    # 2. One or more allowed characters for the local part (alphanumeric, ., _, %, +, -)
    # 3. An "@" symbol
    # 4. One or more allowed characters for the domain name (alphanumeric, ., -)
    # 5. A period (.)
    # 6. Two or more letters for the top-level domain (e.g., com, org, net)
    # 7. End of string ($)
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.fullmatch(email_pattern, email):
        return True
    else:
        return False

def main():
    print("Welcome to the Email Validator!")
    print("Enter 'exit' at any time to quit.")

    while True:
        user_input = input("\nEnter an email address to validate: ")

        if user_input.lower() == 'exit':
            print("Exiting Email Validator. Goodbye!")
            break

        if not user_input:
            print("You didn't enter anything. Please try again.")
            continue

        if validate_email(user_input):
            print(f"'{user_input}' is a VALID email address!")
        else:
            print(f"'{user_input}' is an INVALID email address.")
            print("Please ensure it follows a common format (e.g., example@domain.com).")

if __name__ == "__main__":
    main()