"""
Camera test module
"""
from controllers.CameraController import CameraController as Camera

if __name__ == "__main__":
    pic = Camera.capture()

    if pic:
        pic.save()
        pic.show()
    
