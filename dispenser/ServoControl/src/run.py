import os
import time
import schedule
from datetime import datetime
from Servo import Servo

OPEN_SECONDS = float(os.getenv('OPEN_SECONDS', default=2))
OPEN_ANGLE = float(os.getenv('OPEN_ANGLE', default=30))
CLOSE_ANGLE = float(os.getenv('CLOSE_ANGLE', default=0))

TZ = os.getenv("TZ") 
TZ = TZ if TZ else "America/Sao_Paulo"

DEBUG = os.getenv("DEBUG")
DEBUG = True if DEBUG == "1" else False


def date_time():
   now = datetime.now()
   dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
   return dt_string


def job():
   print("Start: " + date_time())
   task()
   print("End: " + date_time())


def task():
   servo1 = Servo(pin=11)
   servo1.startup()
   
   print("Open")
   servo1.rotate_to_angle(angle=OPEN_ANGLE)
   print("Waiting " + str(OPEN_SECONDS) + " seconds")
   time.sleep(OPEN_SECONDS)
   print("Close")
   servo1.rotate_to_angle(angle=CLOSE_ANGLE)

   servo1.cleanup()


def schedules():
   schedule.every().day.at("06:00", TZ).do(job)
   schedule.every().day.at("09:00", TZ).do(job)
   schedule.every().day.at("12:00", TZ).do(job)
   schedule.every().day.at("15:00", TZ).do(job)
   schedule.every().day.at("15:45", TZ).do(job)
   schedule.every().day.at("18:00", TZ).do(job)
   schedule.every().day.at("21:00", TZ).do(job)


if __name__ == "__main__":
   # test 
   if DEBUG:
      print("Start (Test): " + date_time())
      task()
      print("End (Test): " + date_time())

   # Create schedules
   schedules()

   # Run
   while True:
    schedule.run_pending()
    time.sleep(1)
