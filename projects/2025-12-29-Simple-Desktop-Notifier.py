# Make sure to install plyer first: pip install plyer

import time
from plyer import notification

print("Hello! This is my first Python desktop notifier!")
print("Let's set up some reminders for you.")

# Ask the user for the notification details
title = input("What should be the title of your notification? (e.g., 'Drink Water', 'Break Time'): ")
message = input("What message do you want to see? (e.g., 'Time to hydrate!', 'Stand up and stretch!'): ")

# Ask for the delay, making sure it's a valid number
while True:
    try:
        delay_input = input("How often should I remind you? (Enter delay in seconds, e.g., 300 for 5 minutes): ")
        delay_seconds = int(delay_input)
        if delay_seconds <= 0:
            print("Delay must be a positive number. Please try again.")
        else:
            break # Exit loop if input is valid
    except ValueError:
        print("Oops! That's not a valid number. Please enter a whole number for seconds.")

print(f"\nOkay, I will send you a notification titled '{title}' with message '{message}' every {delay_seconds} seconds.")
print("The notifier will start now. You can close this window or press Ctrl+C to stop it.")
print("Waiting for the first notification...")

# Loop to send notifications
while True:
    try:
        notification.notify(
            title=title,
            message=message,
            app_name="My Python Notifier", # This helps identify the app on some systems
            timeout=10 # How long the notification stays visible (in seconds)
        )
        print(f"Notification sent at {time.strftime('%H:%M:%S')}")
        time.sleep(delay_seconds) # Wait for the specified time before sending the next notification
    except KeyboardInterrupt:
        print("\nNotifier stopped by user. Goodbye!")
        break # Exit the loop when Ctrl+C is pressed
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Stopping the notifier due to an error.")
        break # Exit on other unexpected errors