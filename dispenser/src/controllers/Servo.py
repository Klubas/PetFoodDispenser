#!/usr/bin/env python3
import time

from config.Parameters import EMULATED

if not EMULATED:
    import RPi.GPIO as GPIO


class ServoEmulated:
    @staticmethod
    def rotate_to_angle(angle):
        # duty entre 2 e 12
        print("Moving servo to " + str(angle) + " degree angle")
        time.sleep(0.2)
        time.sleep(0.2)

    @staticmethod
    def startup():
        print("Starting up...")
        time.sleep(1)

    @staticmethod
    def cleanup():
        print("Cleanup, exiting...")


class Servo:
    def __init__(self, pin):
        self.pin = pin
        self.mode = GPIO.BOARD
        self.servo = None

    def rotate_to_angle(self, angle):
        # duty entre 2 e 12
        print("Moving servo to " + str(angle) + " degree angle")
        self.servo.ChangeDutyCycle(2 + (angle / 18))
        time.sleep(0.2)
        self.servo.ChangeDutyCycle(0)
        time.sleep(0.2)

    def startup(self):
        print("Starting up...")
        GPIO.setmode(self.mode)
        GPIO.setup(self.pin, GPIO.OUT)
        self.servo = GPIO.PWM(self.pin, 50)
        self.servo.start(0)
        time.sleep(1)

    def cleanup(self):
        self.servo.stop()
        GPIO.cleanup()
        print("Cleanup, exiting...")


class ServoFactory:
    @staticmethod
    def create(pin):
        if EMULATED:
            return ServoEmulated()
        else:
            return Servo(pin=pin)


if __name__ == '__main__':
    servo = ServoFactory().create(11)
    servo.startup()
    servo.rotate_to_angle(30)
    servo.cleanup()