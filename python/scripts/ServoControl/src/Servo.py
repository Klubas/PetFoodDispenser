#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO

class Servo:
   def __init__(self, pin, mode=GPIO.BOARD):
      self.pin = pin
      self.mode = mode
      self.servo = None

   def rotate_to_angle(self, angle):
      # duty entre 2 e 12
      print("Moving servo to " + str(angle) + " degree angle")
      self.servo.ChangeDutyCycle(2+(angle/18))
      time.sleep(0.5)
      self.servo.ChangeDutyCycle(0)
      time.sleep(0.5)

   def startup(self):
      print("Starting up...")
      GPIO.setmode(self.mode)
      GPIO.setup(self.pin,GPIO.OUT)
      self.servo = GPIO.PWM(self.pin, 50)
      self.servo.start(0)
      time.sleep(1)

   def cleanup(self):
      self.servo.stop()
      GPIO.cleanup()
      print("Cleanup, exiting...")