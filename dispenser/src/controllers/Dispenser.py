import time

from config.Parameters import (OPEN_SECONDS,
                               OPEN_ANGLE,
                               CLOSE_ANGLE,
                               ENABLE_CAMERA,
                               PICTURE_DIR,
                               TELEGRAM_ENABLE)
from controllers.Camera import Camera
from controllers.Servo import ServoFactory as Servo
from controllers.Telegram import TelegramBot


class Dispenser:
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

        base64string = None
        if ENABLE_CAMERA:
            print("Trying to take a picture...")
            pic = Camera().capture()
            if pic:
                path = pic.save(path=PICTURE_DIR)
                base64string = pic.base64string
                print("Picture saved at: " + path)

        if TELEGRAM_ENABLE:
            print("Sending pic to telegram chat")
            bot = TelegramBot()
            if pic:
                bot.send_picture(picture=open(path, 'rb'),
                                 caption='Hora de comer!')
            else:
                bot.send_text(message='Hora de comer!')

        return True, base64string


if __name__ == '__main__':
    dispenser = Dispenser()
    dispenser.dispense_food()
