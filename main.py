from PIL import Image
from PIL import UnidentifiedImageError


class WaterMarker:
    """Class for watermarking images"""

    def __init__(self):
        self.path = self.get_path_to_file_for_watermarking()
        self.image = self.is_the_file_an_image()
        self.watermark_text = self.get_watermark_text()
        self.watermark_font_name = self.get_watermark_font_name()
        self.watermark_font_size = self.get_watermark_font_size()
        self.watermark_step_x = self.get_step_of_watermarks_by_x()
        self.watermark_step_y = self.get_step_of_watermarks_by_y()
        self.watermark_opacity_percentage = self.get_watermark_opacity_percentage()
        self.watermark_rotation_angle = self.get_watermark_rotation_angle()

    def get_path_to_file_for_watermarking(self):
        """Get path to the file for watermarking from user input."""
        self.path = input('Enter path to the file: ')
        return self.path

    def is_the_file_an_image(self):
        """Return True if the file exists & is an image.

        If True: assign the instance of PIL.Image class to global variable "image".
        Else: show error message & return None.
        """
        try:
            self.image = Image.open(self.path)
            return self.image
        except UnidentifiedImageError:
            print("It isn't an image.")
            return None
        except (FileNotFoundError, OSError):
            print("Can't find the file.")
            return None
        except AttributeError:
            print("Select the file.")
            return None

    def get_watermark_text(self):
        """Get text for watermark from user input."""
        self.watermark_text = input('Enter text for watermark: ')
        return self.watermark_text

    def get_watermark_font_name(self):
        """Get name of font for watermark from user input."""
        self.watermark_font_name = input('Enter the name of font for watermark: ')
        return self.watermark_font_name

    def get_watermark_font_size(self):
        """Get size of watermark from user input."""
        self.watermark_font_size = input('Enter the size of font for watermark: ')
        return self.watermark_font_size

    def get_step_of_watermarks_by_x(self):
        """Get step between watermarks on x-axis (horizontal interval)."""
        self.watermark_step_x = input('Enter step by x-axis for watermarks: ')
        return self.watermark_step_x

    def get_step_of_watermarks_by_y(self):
        """Get step between watermarks on y-axis (vertical interval)."""
        self.watermark_step_y = input('Enter step by y-axis for watermarks: ')
        return self.watermark_step_y

    def get_watermark_opacity_percentage(self):
        """Get percentage of opacity for watermark from user input"""
        self.watermark_opacity_percentage = input('Enter % of opacity for watermark: ')
        return self.watermark_opacity_percentage

    def get_watermark_rotation_angle(self):
        """Get rotation angle for watermark."""
        self.watermark_rotation_angle = input('Enter the rotation angle of watermark: ')
        return self.watermark_rotation_angle

    def add_watermark_on_image(self):
        """Add watermark on top of the image."""
        pass

    def save_image_to_file(self):
        """Save edited image as a new file on disk."""
        pass


if __name__ == '__main__':
    im = WaterMarker()
