import time
from datetime import datetime

import schedule

from config.Parameters import SCHEDULE_TIMES, TZ, DEBUG
from controllers.DispenserController import DispenserController as Dispenser


def date_time():
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    return dt_string


def job():
    print("Start: " + date_time())
    Dispenser.dispense_food()
    print("End: " + date_time())


# Run schedules
def run_schedules():
    # create schedules
    for hour in SCHEDULE_TIMES:
        schedule.every().day.at(hour, TZ).do(job)
        print("Schedule created every day at " + hour + " TZ: " + TZ)

    for _job in schedule.get_jobs():
        print(_job)

    # run loop
    while True:
        schedule.run_pending()
        time.sleep(1)


def test():
    if DEBUG:
        print("Start (Test): " + date_time())
        Dispenser.dispense_food()
        print("End (Test): " + date_time())


if __name__ == "__main__":
    test()
    run_schedules()
