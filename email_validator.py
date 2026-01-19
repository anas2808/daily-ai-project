import re

def is_valid_email(email):
    """
    Validates the given email address using regex.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    # Define a regex pattern for validating an email address
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Use re.match to check if the email matches the pattern
    if re.match(email_regex, email):
        return True
    else:
        return False

def validate_email_list(email_list):
    """
    Validates a list of email addresses, returning only the valid ones.
    
    Args:
        email_list (list): List of email addresses to validate.
    
    Returns:
        list: List of valid email addresses.
    """
    valid_emails = []
    for email in email_list:
        if is_valid_email(email):
            valid_emails.append(email)
    return valid_emails

def main():
    """
    Main function to demonstrate the email validation.
    """
    # Sample list of email addresses for testing
    test_emails = [
        "valid.email@example.com",
        "invalid-email.com",
        "another.valid.email@domain.org",
        "invalid@domain@domain.com",
        "valid-email123@sub.domain.co.uk",
        "missing-at-sign.com",
        "@missingusername.com"
    ]
    
    try:
        print("Validating email addresses...")
        valid_emails = validate_email_list(test_emails)
        print("Valid emails are:")
        for email in valid_emails:
            print(email)
    except Exception as e:
        print(f"An error occurred during email validation: {e}")

if __name__ == "__main__":
    main()