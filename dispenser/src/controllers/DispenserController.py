import time
#from src.controllers.ServoController import ServoController as Servo
from src.config.Parameters import OPEN_SECONDS, OPEN_ANGLE, CLOSE_ANGLE


class DispenserController: 
    @staticmethod
    def dispense_food(open_angle=OPEN_ANGLE
                    , close_angle=CLOSE_ANGLE
                    , open_seconds=OPEN_SECONDS):

        #servo = Servo(pin=11)
        #servo.startup()

        print("Open")
        #servo.rotate_to_angle(angle=open_angle)
        print("Waiting " + str(open_seconds) + " seconds")
        time.sleep(open_seconds)
        print("Close")
        #servo.rotate_to_angle(angle=close_angle)

        #servo.cleanup()