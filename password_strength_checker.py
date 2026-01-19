import re

def password_strength(password):
    """
    Evaluate the strength of a given password based on several criteria.

    Parameters:
    password (str): The password string to be evaluated.

    Returns:
    str: A string representing the strength of the password ('Weak', 'Moderate', 'Strong').
    """
    
    # Check length of the password
    if len(password) < 8:
        return 'Weak'

    # Initialize strength parameters
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[\W_]', password))

    # Calculate strength based on criteria
    strength_criteria = sum([has_lower, has_upper, has_digit, has_special])

    if strength_criteria == 1:
        return 'Weak'
    elif strength_criteria == 2:
        return 'Moderate'
    elif strength_criteria > 2:
        return 'Strong'

    return 'Weak'

def main():
    """
    Main function to run the password strength checker program.
    """
    try:
        # Prompt user for password input
        password = input("Enter a password to check its strength: ").strip()
        
        # Check if password is empty
        if not password:
            raise ValueError("Password cannot be empty")

        # Evaluate and output the strength of the password
        strength = password_strength(password)
        print(f"The strength of the password is: {strength}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()