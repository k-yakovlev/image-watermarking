from PIL import Image, ImageFont, ImageDraw
from PIL import UnidentifiedImageError


class WaterMarker:
    """Class for watermarking images"""
    fonts = ['Pacifico']

    def __init__(self):
        self.path = self.get_path_to_file_for_watermarking()
        self.image = self.get_image_from_file()
        if self.image:
            self.new_image = self.image.convert('RGBA')
            self.dbl_max_size = max(self.image.size) * 2
            self.diagonal_size = (
                    (self.image.width ** 2 + self.image.height ** 2) ** .5
            )
            self.quarter_side_length = int(self.dbl_max_size * .25)
            self.watermark_layer = Image.new(mode='RGBA',
                                             size=(self.dbl_max_size,
                                                   self.dbl_max_size),
                                             color=(255, 255, 255, 0))
            self.text_instance = ImageDraw.Draw(self.watermark_layer)
            self.watermark_text = self.get_watermark_text()
            self.watermark_font_name = self.get_watermark_font_name()
            self.watermark_font_size = self.get_watermark_font_size()
            self.watermark_font = ImageFont.truetype(
                f'{self.watermark_font_name}.ttf',
                self.watermark_font_size,
            )
            self.watermark_step_x = self.get_step_of_watermarks_by_x()
            self.watermark_step_y = self.get_step_of_watermarks_by_y()
            self.next_line_offset_by_x = self.get_next_line_offset_by_x()
            self.watermark_opacity_value = self.get_watermark_opacity_value()
            self.watermark_rotation_angle = self.get_watermark_rotation_angle()
            self.draw_text_on_watermark_layer()
            self.rotate_watermark_layer()
            self.crop_watermark_layer()
            self.add_watermark_on_image()
            self.convert_image_to_rgb()
            self.save_image_to_file()
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
        font_size = input('Enter the size of font for watermark: ')
        try:
            self.watermark_font_size = int(font_size)
            if self.watermark_font_size > 0:
                return self.watermark_font_size
            raise ValueError
        except ValueError:
            print('Font size should be an integer > 0.')
            return self.get_watermark_font_size()

    def get_step_of_watermarks_by_x(self):
        """Get step between watermarks on x-axis (horizontal interval)."""
        step_x = input('Enter step by x-axis for watermarks (integer > 0): ')
        try:
            self.watermark_step_x = int(step_x)
            if self.watermark_step_x > 0:
                return self.watermark_step_x
            raise ValueError
        except ValueError:
            print('Horizontal step of watermarks must be an integer > 0.')
            return self.get_step_of_watermarks_by_x()

    def get_step_of_watermarks_by_y(self):
        """Get step between watermarks on y-axis (vertical interval)."""
        step_y = input('Enter step by y-axis for watermarks (integer > 0): ')
        try:
            self.watermark_step_y = int(step_y)
            if self.watermark_step_y > 0:
                return self.watermark_step_y
            raise ValueError
        except ValueError:
            print('Vertical step of watermarks must be an integer > 0.')
            return self.get_step_of_watermarks_by_y()

    def get_next_line_offset_by_x(self):
        """Get next line offset by x-axis."""
        chess_order = input('Enable chess order (y/n): ')
        if chess_order == 'y':
            self.next_line_offset_by_x = int(self.watermark_step_x * .5)
            return self.next_line_offset_by_x
        elif chess_order == 'n':
            self.next_line_offset_by_x = 0
            return self.next_line_offset_by_x
        else:
            print('Invalid input. Only "y" on "n".')
            return self.get_next_line_offset_by_x()

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

    def draw_text_on_watermark_layer(self):
        """Draw multiple text instance on watermark layer."""
        for x_coordinate in range(0,
                                  self.dbl_max_size,
                                  self.watermark_step_x):
            for y_coordinate in range(0,
                                      self.dbl_max_size,
                                      self.watermark_step_y):
                self.text_instance.text(
                    xy=(x_coordinate, y_coordinate),
                    text=self.watermark_text,
                    font=self.watermark_font,
                    fill=(255, 255, 255, self.watermark_opacity_value),
                )
                self.next_line_offset_by_x *= -1
                x_coordinate -= self.next_line_offset_by_x

    def rotate_watermark_layer(self):
        """Rotate watermark layer."""
        self.watermark_layer = (
            self.watermark_layer.rotate(self.watermark_rotation_angle)
        )

    def crop_watermark_layer(self):
        """Crop watermark layer to image size."""
        self.watermark_layer = self.watermark_layer.crop(
            (self.quarter_side_length,
             self.quarter_side_length,
             self.quarter_side_length + self.image.width,
             self.quarter_side_length + self.image.height)
        )

    def add_watermark_on_image(self):
        """Add watermark on top of the image."""
        self.new_image = Image.alpha_composite(self.new_image,
                                               self.watermark_layer)

    def convert_image_to_rgb(self):
        """Convert image from RGBA to RGB."""
        self.new_image = self.new_image.convert('RGB')

    def save_image_to_file(self):
        """Save image with watermarks as a new file on disk."""
        new_file_name = input('Enter file name to save new file: ')
        try:
            self.new_image.save(f'{new_file_name}.jpg')
        except ValueError:
            print('Invalid file name.')
            return self.save_image_to_file()


if __name__ == '__main__':
    im = WaterMarker()
