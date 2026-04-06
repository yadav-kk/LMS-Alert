import time
import requests
from datetime import datetime
import pytz
import urllib3
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

IST = pytz.timezone("Asia/Kolkata")
m="https://learn.gyantantra.org/"
URL = "https://api.gyantantra.org/"
CHECK_INTERVAL = 1800
TIMEOUT = 10

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID").split(",")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})

def check_website():
    try:
        response = requests.get(URL, timeout=TIMEOUT, verify=False)
        if response.status_code == 200:
            status = "✅ UP! Yes, It is working"
        else:
            status = f"⚠️ Status Code: {response.status_code}"
    except Exception as e:
        status = f"❌ DOWN\n\n!Web Is down, Please take a look at this, \nError: {e}"
    return status

while True:
    status = check_website()

    message = (
        f"🌐 Website Status Update\n{m}\n"
        f"URL: {URL}\n"
        f"Status: {status}\n"
        f"Time: {datetime.now(IST)}"
    )

    print(message)
    send_telegram_message(message)

    time.sleep(CHECK_INTERVAL)
