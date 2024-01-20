"""
Camera test module
"""
import glob
import os
from base64 import b64encode
from datetime import datetime
from subprocess import run, CalledProcessError

from controllers.Picture import Picture
from config.Parameters import CAMERA_DEVICE_PATH, DEBUG


class Camera:
    def __init__(self):
        self.ffmpeg_path = "ffmpeg"
        self.frame = 1
        self.show_error = DEBUG

    @staticmethod
    def __timestamp__():
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S%ms")
        return dt_string

    """
    @staticmethod
    def __v4l2_capture__(self):
        from PIL import Image
        import select, v4l2capture
        
        video = v4l2capture.Video_device(Camera.video_source)
        size_x = 640
        size_y = 480
        size_x, size_y = video.set_format(size_x, size_y)
        video.create_buffers(1)
        video.queue_all_buffers()
        video.start()
        bio = io.BytesIO()
        try:
            while True:
                select.select((video,), (), ())  # Wait for the device to fill the buffer.
                image_data = video.read_and_queue()
                image = Image.frombytes("RGB", (size_x, size_y), image_data)
                image.save(bio, format="jpeg")
                yield bio.getvalue()
                bio.seek(0)
                bio.truncate()
        finally:
            video.close()
    """

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

        for dev in glob.glob("/dev/video?"):
            try:
                self.__ffmpeg_capture__(dev)
                return dev
            except CalledProcessError as e:
                print(e)
                continue
        raise Exception("No available cameras found")

    def capture(self):
        filename = "capture-" + self.__timestamp__() + ".jpeg"
        try:
            camera = self.get_camera()
        except Exception as e:
            print(e)
            return False

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
    cam = Camera()
    pic = cam.capture()

    if pic:
        pic.save()
