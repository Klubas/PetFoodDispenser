import sys
import time
import signal
import schedule
from threading import Thread
from datetime import datetime

from src.app import runApp, app
from src.controllers.DispenserController import DispenserController as Dispenser

from src.config.Parameters import DEBUG, SCHEDULE_TIMES, TZ


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


def signal_handler(signal, frame):
    print("Killing threads and exiting...")
    sys.exit(0)


def main():
   signal.signal(signal.SIGINT, signal_handler)

   #test
   if DEBUG:
      print("Start (Test): " + date_time())
      Dispenser.dispense_food()
      print("End (Test): " + date_time())
   
   try:
      t1 = Thread(target=run_schedules)
      t1.daemon = True
      t1.start()

      t2 = Thread(target=runApp())
      t2.daemon = True
      t2.start()

      t1.join()
      t2.join()

   except Exception as e:
      print("Exception:")
      print(e)

if __name__ == "__main__":
   main()
