import os
import glob
from datetime import datetime
from cv2 import VideoCapture, imshow, imwrite, waitKey, destroyWindow

def get_camera():
    for dev in reversed(glob.glob("/dev/video?")):
        camera = VideoCapture(dev)
        source = dev
        break
    
    if camera is None or not camera.isOpened():
        raise Exception('Warning: unable to open video source: ' + source)
    else:
        return camera
    
    raise Exception("No cameras found")

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
        waitKey(0) 
        destroyWindow(self.filename) 
    
    def save(self, filename=None, path=None):
        
        path        = '.'           if path     is None else path
        filename    = self.filename if filename is None else filename
        
        try:
            full_path = os.path.join(self.path, self.filename)
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

