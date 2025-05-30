from datetime import datetime

from notification import fetch_ttd_notifications
from telegram_msg import compare_and_send_notifications
from utils.file_utils import load_known_notifications

def send_ttd_notifications():
    # Get the current Notifications from the TTD website
    current_notifications = fetch_ttd_notifications()

    # Load already available notifications
    known_notifications = load_known_notifications()

    # Compare both current and know notification if any new notification comes in send a telegram message
    compare_and_send_notifications(current_notifications, known_notifications)


if __name__ == "__main__":
    send_ttd_notifications()
    print("🟢 TTD Bot ran at:", datetime.now())