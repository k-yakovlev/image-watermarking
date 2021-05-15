from PIL import Image
from PIL import UnidentifiedImageError


def get_path_to_file_for_watermarking():
    """Get path to the file for watermarking from user input."""
    global file
    file = input('Enter path to the file: ')


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


def get_watermark_font_name():
    """Get name of font for watermark from user input."""
    global watermark_font_name
    watermark_font_name = input('Enter the name of font for watermark: ')


def get_watermark_font_size():
    """Get size of watermark from user input."""
    global watermark_font_size
    watermark_font_size = input('Enter the size of font for watermark: ')


def get_step_of_watermarks_by_x():
    """Get step between watermarks on x-axis (horizontal interval)."""
    global watermark_step_x
    watermark_step_x = input('Enter step by x-axis for watermarks: ')


def get_step_of_watermarks_by_y():
    """Get step between watermarks on y-axis (vertical interval)."""
    global watermark_step_y
    watermark_step_y = input('Enter step by y-axis for watermarks: ')


def get_watermark_opacity_percentage():
    """Get percentage of opacity for watermark from user input"""
    global watermark_opacity_percentage
    watermark_opacity_percentage = input('Enter % of opacity for watermark: ')


def get_watermark_rotation_angle():
    """Get rotation angle for watermark."""
    global watermark_rotation_angle
    watermark_rotation_angle = input('Enter the rotation angle of watermark: ')


def add_watermark_on_image():
    """Add watermark on top of the image."""
    pass


def save_image_to_file():
    """Save edited image as a new file on disk."""
    pass


file = None
watermark_text = None
watermark_font_name = None
watermark_font_size = None
watermark_step_x = None
watermark_step_y = None
watermark_opacity_percentage = None
watermark_rotation_angle = None
image = None

if __name__ == '__main__':
    print(is_the_file_an_image())
