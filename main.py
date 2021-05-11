from PIL import Image
from PIL import UnidentifiedImageError


def get_file_for_watermarking():
    pass


def is_the_file_an_image():
    """Return True if the file exists & is an image.

    If True: assign the instance of PIL.Image class to global variable "image".
    Else: show error message & return None.
    """
    global image
    try:
        image = Image.open(file)
        return True
    except UnidentifiedImageError:
        print("It isn't an image.")
        return None
    except (FileNotFoundError, OSError):
        print("Can't find the file.")
        return None
    except AttributeError:
        print("Select the file.")
        return None


def get_watermark_text():
    pass


def get_watermark_size():
    pass


def get_watermark_font():
    pass


def add_watermark_on_image():
    pass


def save_image_to_file():
    pass


file = '1.jpg'
image = None

if __name__ == '__main__':
    print(is_the_file_an_image())
