import time
from config.Parameters import OPEN_SECONDS, OPEN_ANGLE, CLOSE_ANGLE, EMULATED

@staticmethod
def __dispense_food_test__(open_angle=OPEN_ANGLE
                        , close_angle=CLOSE_ANGLE
                        , open_seconds=OPEN_SECONDS):
    print("RUNNING IN EMULATED MODE")
    print("Open")
    print("Waiting " + str(open_seconds) + " seconds")
    time.sleep(open_seconds)
    print("Close")

@staticmethod
def __dispense_food__(open_angle=OPEN_ANGLE
                    , close_angle=CLOSE_ANGLE
                    , open_seconds=OPEN_SECONDS):

    from controllers.ServoController import ServoController as Servo

    servo = Servo(pin=11)
    servo.startup()

    print("Open")
    servo.rotate_to_angle(angle=open_angle)
    print("Waiting " + str(open_seconds) + " seconds")
    time.sleep(open_seconds)
    print("Close")
    servo.rotate_to_angle(angle=close_angle)

    servo.cleanup()

class DispenserController:
    @staticmethod
    def dispense_food(open_angle=OPEN_ANGLE
                    , close_angle=CLOSE_ANGLE
                    , open_seconds=OPEN_SECONDS):

        if EMULATED:
            __dispense_food_test__(open_angle=open_angle
                                 , close_angle=close_angle
                                 , open_seconds=open_seconds)

        else:
            __dispense_food__(open_angle=open_angle
                            , close_angle=close_angle
                            , open_seconds=open_seconds)