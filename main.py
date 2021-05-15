from PIL import Image
from PIL import UnidentifiedImageError


def get_path_to_file_for_watermarking():
    """Get path to the file for watermarking from user input."""
    global file
    file = input('Enter path to the file: ')
    return file


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
    """Get text for watermark from user input."""
    global watermark_text
    watermark_text = input('Enter text for watermark: ')


def get_watermark_size():
    """Get size of watermark from user input."""
    pass


def get_watermark_font():
    """Get font of watermark from user input."""
    pass


def get_watermark_opacity():
    """Get opacity of watermark from user input"""
    pass


def add_watermark_on_image():
    """Add watermark on top of the image."""
    pass


def save_image_to_file():
    """Save edited image as a new file on disk."""
    pass


file = None
watermark_text = None
image = None

if __name__ == '__main__':
    print(is_the_file_an_image())
