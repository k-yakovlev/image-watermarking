from PIL import Image
from PIL import UnidentifiedImageError


class WaterMarker:
    """Class for watermarking images"""

    def __init__(self):
        self.path = self.get_path_to_file_for_watermarking()
        self.image = self.get_image_from_file()
        if self.image:
            self.watermark_text = self.get_watermark_text()
            self.watermark_font_name = self.get_watermark_font_name()
            self.watermark_font_size = self.get_watermark_font_size()
            self.watermark_step_x = self.get_step_of_watermarks_by_x()
            self.watermark_step_y = self.get_step_of_watermarks_by_y()
            self.watermark_opacity_value = self.get_watermark_opacity_value()
            self.watermark_rotation_angle = self.get_watermark_rotation_angle()
        else:
            self.__init__()

    def get_path_to_file_for_watermarking(self):
        """Get path to the file for watermarking from user input."""
        self.path = input('Enter path to the file: ')
        return self.path

    def get_image_from_file(self):
        """Return True if the file exists & is an image.

        If True: assign the instance of PIL.Image class to global variable "image".
        Else: show error message & return None.
        """
        try:
            self.image = Image.open(self.path)
            return self.image
        except UnidentifiedImageError:
            print("This isn't an image file.")
        except (FileNotFoundError, OSError):
            print("File not found.")
        except AttributeError:
            print("File path not specified.")
        except ValueError:
            print("'mode' should be 'r'. 'fp' can't be a StringIO instance.")
        except TypeError:
            print('"format" value type should be one of: None, list, tuple.')
        self.image = None
        return self.image

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

    def get_watermark_opacity_value(self):
        """Get % of opacity for watermark from user input & convert it to RGBA.

        RGBA value should be integer in range 0-255, but % is more user-friendly.
        """
        user_input = input('Enter % of opacity for watermark (1-100): ')
        try:
            watermark_opacity_percentage = int(user_input)
            if 1 <= watermark_opacity_percentage <= 100:
                self.watermark_opacity_value = int(watermark_opacity_percentage * 2.55)
                return self.watermark_opacity_value
            else:
                raise ValueError
        except ValueError:
            print('Invalid input. Opacity should be integer from 1 to 100.')
            return self.get_watermark_opacity_value()

    def get_watermark_rotation_angle(self):
        """Get rotation angle for watermark."""
        user_input = input('Enter the rotation angle of watermark: ')
        try:
            self.watermark_rotation_angle = int(user_input)
            return self.watermark_rotation_angle
        except ValueError:
            print('Invalid input. Angle should be an integer.')
            return self.get_watermark_rotation_angle()

    def add_watermark_on_image(self):
        """Add watermark on top of the image."""
        pass

    def save_image_to_file(self):
        """Save edited image as a new file on disk."""
        pass


if __name__ == '__main__':
    im = WaterMarker()
