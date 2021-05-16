from PIL import Image
from PIL import UnidentifiedImageError


class WaterMarker:
    """Class for watermarking images"""

    def __init__(self):
        self.fonts = ['Pacifico']
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
        """Get PIL.Image object from self.path & return it to self.image.

        If image file exist --> return PIL.Image object.
        Otherwise --> show error message, return self.image = None
        """
        self.image = None
        try:
            self.image = Image.open(self.path)
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
        return self.image

    def get_watermark_text(self):
        """Get text for watermark from user input."""
        watermark_text = input('Enter text for the watermark: ')
        if watermark_text:
            self.watermark_text = watermark_text
            return self.watermark_text
        else:
            print('The watermark text is not specified.')
            return self.get_watermark_text()

    def get_watermark_font_name(self):
        """Get name of font for watermark from user input."""
        font_name = input('Enter the name of font for watermark: ')
        if font_name in self.fonts:
            self.watermark_font_name = font_name
            return self.watermark_font_name
        else:
            print('Unknown font name.')
            return self.get_watermark_font_name()

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

        Each of RGBA value should be an integer in range 0-255.
        But % is more user-friendly format for input.
        0% opacity is absolutely transparent image. In case of watermark it
        doesn't make sense. Because of it valid input starts from 1.

        If user input is correct then opacity value in RGBA format will be
        returned in self.watermark_opacity_value.
        Otherwise function raise ValueError & call themself again.
        """
        watermark_opacity = input('Enter % of opacity for watermark (1-100): ')
        try:
            opacity_percentage = int(watermark_opacity)
            if 1 <= opacity_percentage <= 100:
                self.watermark_opacity_value = int(opacity_percentage * 2.55)
                return self.watermark_opacity_value
            else:
                raise ValueError
        except ValueError:
            print('Invalid input. Opacity should be an integer from 1 to 100.')
            return self.get_watermark_opacity_value()

    def get_watermark_rotation_angle(self):
        """Get rotation angle for watermark."""
        rotation_angle = input('Enter the rotation angle of watermark: ')
        try:
            self.watermark_rotation_angle = int(rotation_angle)
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
