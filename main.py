from PIL import Image
from PIL import UnidentifiedImageError


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


file = '1.jpg'
image = None

if __name__ == '__main__':
    print(is_the_file_an_image())
