"""
Camera test module
"""
import os
import glob
from datetime import datetime
from base64 import b64decode, b64encode
from subprocess import run, CalledProcessError

from config.Parameters import PICTURE_DIR, CAMERA_DEVICE_PATH, DEBUG


class Picture:
    def __init__(self, filename, base64string):
        self.base64string = base64string
        self.filename = filename

    def save(self, filename=None, path=None):
        path = PICTURE_DIR if path is None else path
        filename = self.filename if filename is None else filename

        try:
            os.makedirs(path, exist_ok=True)
            full_path = os.path.join(path, filename)

            print("Converting base64 to binary")
            with open(full_path, "wb") as image:
                print("Writing file to " + str(full_path))
                image.write(b64decode(self.base64string))

            return full_path
        except Exception as e:
            print(e)
            return None


class CameraController:
    def __init__(self):
        self.ffmpeg_path = "ffmpeg"
        self.frame = 1
        self.show_error = DEBUG

    @staticmethod
    def __timestamp_():
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S%ms")
        return dt_string

    def __ffmpeg_capture__(self, device, filename='capture.jpeg', filepath='/tmp'):
        """
        ffmpeg -f video4linux2 -i /dev/v4l/by-id/usb-*  -vframes 1 -video_size 640x480 test%3d.jpeg
        """
        ffmpeg_args = (" -f " + "video4linux2"
                       + " -i " + device
                       + " -vframes " + str(self.frame)
                       + " -video_size " + "640x480"
                       + "-update " + filename
                       + " -y")

        cmd = self.ffmpeg_path + ffmpeg_args
        print(cmd)
        cmd = cmd.split(' ')

        out = run(cmd, encoding='UTF-8', cwd=filepath, stderr=self.show_error)
        print(out)
        out.check_returncode()

        file = os.path.join(filepath, filename)
        print("Converting binary to base64")
        with open(file, 'rb') as image_file:
            base64string = b64encode(image_file.read()).decode('ascii')

        try:
            print("Deleting file " + file)
            os.remove(file)
        except (FileNotFoundError, Exception) as fnf:
            print("ERROR: File " + file + " not deleted")
            print(fnf)

        return base64string

    def get_camera(self):

        if CAMERA_DEVICE_PATH:
            return CAMERA_DEVICE_PATH

        for dev in glob.glob("/dev/v4l/by-id/usb-*"):
            try:
                self.__ffmpeg_capture__(dev)
                return dev
            except CalledProcessError as e:
                print(e)
                continue
        raise Exception("No available cameras found")

    def capture(self):
        filename = "capture-" + self.__timestamp_() + ".jpeg"
        camera = self.get_camera()

        try:
            base64string = self.__ffmpeg_capture__(camera)
            if base64string:
                return Picture(filename=filename, base64string=base64string)
            else:
                raise Exception("No image detected. Please! try again")
        except Exception as e:
            print("Error capturing pictures with device " + camera)
            print(e)


if __name__ == "__main__":
    cam = CameraController()
    pic = cam.capture()

    if pic:
        pic.save()
