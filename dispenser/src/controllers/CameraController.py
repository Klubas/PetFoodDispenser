import glob
import os
from datetime import datetime

from cv2 import VideoCapture, imshow, imwrite, waitKey, destroyWindow, CAP_V4L2
from config.Parameters import PICTURE_DIR


def get_camera():
    for dev in glob.glob("/dev/video?"):
        camera = VideoCapture(dev, CAP_V4L2)
        if camera is None or not camera.isOpened():
            continue
        else:
            return camera
    raise Exception("No available cameras found")


def date_time():
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S%ms")
    return dt_string


class Picture:
    def __init__(self, filename, image):
        self.image = image
        self.filename = filename

    def show(self):
        imshow(self.filename, self.image)
        print("Press any key to quit viewer")
        waitKey(0)
        destroyWindow(self.filename)

    def save(self, filename=None, path=None):

        path = PICTURE_DIR if path is None else path
        filename = self.filename if filename is None else filename

        try:
            os.makedirs(path, exist_ok=True)
            full_path = os.path.join(path, filename)
            imwrite(full_path, self.image)
            return full_path
        except Exception as e:
            print(e)
            return None


class CameraController:
    @staticmethod
    def capture():
        try:
            camera = get_camera()
            result, image = camera.read()

            if result:
                filename = "capture-" + date_time() + ".png"
                return Picture(filename, image)
            else:
                raise Exception("No image detected. Please! try again")

        except Exception as e:
            print(e)
