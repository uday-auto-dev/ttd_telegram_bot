import json
import requests
from datetime import datetime


from utils.file_utils import save_notifications

data_path = "data/info.json"
with open(data_path) as f:
    data_json = json.load(f)
    data = data_json["data"][0]

BOT_TOKEN = data["BOT_TOKEN"]
CHAT_ID = data["CHAT_ID"]

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    response = requests.post(url, data=payload)
    assert response.status_code == 200, "Unable to send Telegram Message !!!"
    return response.status_code

def compare_and_send_notifications(current_notifications, known_notifications):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not known_notifications:
        # First-time run: send all
        message = (
            f"📢 <b>TTD Notification List (Initial Load) {timestamp} </b>\n\n" +
            "\n\n".join(f"🔹 {msg}" for msg in current_notifications)
        )
        send_telegram_message(message)
        save_notifications(current_notifications)
    else:
        new_notifications = list(set(current_notifications) - set(known_notifications))

        if new_notifications:
            message = (
                f"🆕 <b>New TTD Notification(s) - {timestamp}</b>\n\n" +
                "\n".join(f"🔹 {msg}" for msg in new_notifications)
            )
            send_telegram_message(message)

            # Append new to a known list and save
            updated_notifications = known_notifications + new_notifications
            save_notifications(updated_notifications)
        else:
            print("No new notifications.")
            send_telegram_message(f"✅ No new TTD notifications at this time.<b> {timestamp}</b>\n")