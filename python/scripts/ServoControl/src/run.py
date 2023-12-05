import os
import time
from Servo import Servo

OPEN_SECONDS = float(os.getenv('OPEN_SECONDS', default=2))
OPEN_ANGLE = float(os.getenv('OPEN_ANGLE', default=30))
CLOSE_ANGLE = float(os.getenv('CLOSE_ANGLE', default=0))

if __name__ == "__main__":
   servo1 = Servo(11, GPIO.BOARD)
   servo1.startup()

   print("Open")
   servo1.rotate_to_angle(angle=OPEN_ANGLE)
   print("Waiting " + str(OPEN_SECONDS) + " seconds")
   time.sleep(OPEN_SECONDS)
   print("Close")
   servo1.rotate_to_angle(angle=CLOSE_ANGLE)
   
   servo1.cleanup()
