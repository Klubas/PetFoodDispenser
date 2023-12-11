import os
import time
import schedule
from datetime import datetime
from Servo import Servo

OPEN_SECONDS   = float(os.getenv('OPEN_SECONDS', default=2))
OPEN_ANGLE     = float(os.getenv('OPEN_ANGLE', default=30))
CLOSE_ANGLE    = float(os.getenv('CLOSE_ANGLE', default=0))
SCHEDULE_TIMES = os.getenv('SCHEDULE_TIMES', default="06:00,09:00,12:00,15:00,18:00,21:00").split(',')
TZ             = os.getenv('TZ', default="America/Sao_Paulo") 
DEBUG          = True if os.getenv('DEBUG', default=0) == "1" else False


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
   for hour in SCHEDULE_TIMES:
      schedule.every().day.at(hour, TZ).do(job)
      print("Schedule created every day at " + hour + " TZ: " + TZ)


if __name__ == "__main__":
   try:
      #test
      if DEBUG:
         print("Start (Test): " + date_time())
         task()
         print("End (Test): " + date_time())

      # Create schedules
      schedules()

      # Run schedules
      while True:
         schedule.run_pending()
         time.sleep(1)

   except KeyboardInterrupt:
      print("Exiting...")
   except Exception as e:
      print("Unexpect error.")
      print(str(e))