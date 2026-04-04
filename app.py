import time
import requests
from datetime import datetime
import urllib3
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://apis.gyantantra.org/"
CHECK_INTERVAL = 1800
TIMEOUT = 10

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_IDS").split(",")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})

def check_website():
    try:
        response = requests.get(URL, timeout=TIMEOUT, verify=False)
        if response.status_code == 200:
            status = "✅ UP"
        else:
            status = f"⚠️ Status Code: {response.status_code}"
    except Exception as e:
        status = f"❌ DOWN\nError: {e}"
    return status

while True:
    status = check_website()

    message = (
        f"🌐 Website Status Update\n\n"
        f"URL: {URL}\n"
        f"Status: {status}\n"
        f"Time: {datetime.now()}"
    )

    print(message)
    send_telegram_message(message)

    time.sleep(CHECK_INTERVAL)
