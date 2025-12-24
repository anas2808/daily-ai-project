import re

def check_password_strength(password):
    score = 0
    feedback_messages = []

    # --- Length check ---
    if len(password) < 8:
        feedback_messages.append("Password is too short. Needs at least 8 characters.")
        # If the password is critically short, it's immediately classified as "Very Weak".
        # No further scoring is needed as it fails a fundamental requirement.
        return "Very Weak", feedback_messages
    elif len(password) >= 8 and len(password) < 12:
        score += 1 # 1 point for meeting the minimum length (8-11 characters)
        feedback_messages.append("Length is good (8-11 characters). Consider making it longer (12+ characters) for better strength.")
    else: # len(password) >= 12
        score += 2 # 2 points for excellent length (12+ characters)
        # No negative feedback message is added here as length is optimal.

    # --- Character type checks ---
    # Using regular expressions to check for character presence
    has_lowercase = bool(re.search(r"[a-z]", password))
    has_uppercase = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"\d", password))
    # Special characters include common symbols, adjust regex if needed
    has_special = bool(re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]", password))

    if has_lowercase:
        score += 1
    else:
        feedback_messages.append("Add lowercase letters.")

    if has_uppercase:
        score += 1
    else:
        feedback_messages.append("Add uppercase letters.")

    if has_digit:
        score += 1
    else:
        feedback_messages.append("Add numbers.")

    if has_special:
        score += 1
    else:
        feedback_messages.append("Add special characters (e.g., !@#$%^&*).")

    # --- Determine strength level based on total score ---
    # The maximum possible score is 6 (2 for length + 1 each for 4 character types).
    strength = ""
    if score <= 2:
        strength = "Very Weak"
    elif score == 3:
        strength = "Weak"
    elif score == 4:
        strength = "Medium"
    elif score == 5:
        strength = "Strong"
    else: # score == 6
        strength = "Very Strong"
    
    return strength, feedback_messages

# --- Main program loop ---
print("Welcome to the Password Strength Checker!")
print("Enter a password to check its strength (type 'exit' to quit).")

while True:
    user_password = input("\nEnter your password: ") # Prompt for input with a newline for clarity

    if user_password.lower() == 'exit':
        break # Exit the loop if the user types 'exit'

    if not user_password:
        print("Password cannot be empty. Please try again.")
        continue # Ask for input again if the password is empty

    strength_level, feedback_messages = check_password_strength(user_password)

    print(f"\nPassword Strength: {strength_level}")
    print("Feedback:")
    if feedback_messages:
        # If there are specific feedback messages (i.e., deficiencies), print them
        for msg in feedback_messages:
            print(f"- {msg}")
    else:
        # If feedback_messages is empty, it means all criteria for a very strong password were met
        print("- All criteria met for a very strong password!")
    print("-" * 30) # Separator for better readability between checks

print("Thank you for using the Password Strength Checker!")