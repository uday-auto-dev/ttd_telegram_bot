import os

NOTIFY_FILE = "data/known_notifications.txt"

def load_known_notifications():
    if not os.path.exists(NOTIFY_FILE):
        return []
    with open(NOTIFY_FILE, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]


def save_notifications(notification_list):
    with open(NOTIFY_FILE, "w", encoding="utf-8") as file:
        file.write("\n".join(notification_list))

