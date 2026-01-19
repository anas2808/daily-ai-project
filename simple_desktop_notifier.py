import time
from plyer import notification

def send_notification(title: str, message: str, app_icon: str = None, timeout: int = 10) -> None:
    """
    Send a desktop notification.

    :param title: Title of the notification
    :param message: Message body of the notification
    :param app_icon: Path to the icon file (optional)
    :param timeout: Duration in seconds for which the notification is displayed
    """
    try:
        notification.notify(
            title=title,
            message=message,
            app_icon=app_icon,
            timeout=timeout
        )
    except Exception as e:
        print(f"Error sending notification: {e}")

def main():
    """
    Main function to execute the desktop notifier.
    """
    # Example notification details
    notification_title = "Reminder"
    notification_message = "Time to take a break!"
    notification_icon = None  # Specify icon path if available
    notification_interval = 60 * 60  # Repeat every hour

    while True:
        send_notification(
            title=notification_title,
            message=notification_message,
            app_icon=notification_icon,
            timeout=10
        )
        # Sleep for the specified interval
        time.sleep(notification_interval)

if __name__ == "__main__":
    main()