import time

from controllers.ServoController import ServoControllerFactory as Servo
from controllers.CameraController import CameraController as Camera
from config.Parameters import OPEN_SECONDS, OPEN_ANGLE, CLOSE_ANGLE, ENABLE_CAMERA, PICTURE_DIR


class DispenserController:
    @staticmethod
    def dispense_food(open_angle=OPEN_ANGLE,
                      close_angle=CLOSE_ANGLE,
                      open_seconds=OPEN_SECONDS):

        servo = Servo().create(pin=11)
        servo.startup()

        print("Open")
        servo.rotate_to_angle(angle=open_angle)
        print("Waiting " + str(open_seconds) + " seconds")
        time.sleep(open_seconds)
        print("Close")
        servo.rotate_to_angle(angle=close_angle)

        servo.cleanup()

        if ENABLE_CAMERA:
            print("Trying to take a picture...")
            pic = Camera.capture()
            if pic:
                path = pic.save(path=PICTURE_DIR)
                print("Picture saved at: " + path)
