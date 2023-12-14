import os
from base64 import b64decode

from config.Parameters import PICTURE_DIR


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
