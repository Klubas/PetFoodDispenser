"""
Schedules module
"""
import os
import time
from datetime import datetime

import schedule

from config.Parameters import SCHEDULE_TIMES, TZ, PICTURE_DIR, ENABLE_CAMERA, TELEGRAM_ENABLE
from controllers.Dispenser import Dispenser as Dispenser
from controllers.Telegram import TelegramBot


def date_time():
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    return dt_string


def job():
    print("Start: " + date_time())
    Dispenser.dispense_food()
    print("End: " + date_time())


def purge_pictures():
    print("Running purge job")

    if TELEGRAM_ENABLE:
        bot = TelegramBot()
        bot.send_text("Running purge job")

    for root, dirs, files in os.walk(PICTURE_DIR):
        for file in files:
            filepath = os.path.join(PICTURE_DIR, file)
            if os.path.getmtime(filepath) < datetime.now().timestamp() - 86400 * 7:
                try:
                    print('Deleting file ' + filepath)
                    os.remove(filepath)
                except (FileNotFoundError, Exception) as fnf:
                    print('ERROR: File ' + filepath + ' not deleted')
                    print(str(fnf))


# Run schedules
def run_schedules():
    # create schedules
    for hour in SCHEDULE_TIMES:
        schedule.every().day.at(hour, TZ).do(job)
        print("Feed schedule created every day at " + hour + " TZ: " + TZ)

    if ENABLE_CAMERA:
        schedule.every().saturday.do(purge_pictures)
        print("Purge schedule created every saturday")

    # run loop
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    job()
    purge_pictures()
    run_schedules()
