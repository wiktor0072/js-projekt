from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageFont, ImageDraw
import os


class Picture:

    def __init__(self, first_pic):
        self.history = [first_pic]
        self.idx = 0

    def __getitem__(self, item):
        return self.history[item]

    def append(self, val):
        self.history.append(val)
        self.idx = len(self.history) - 1

    def get_curr_pic(self):
        return self.history[self.idx]

    def rotate_right(self):
        self.history.append(self.history[self.idx].rotate(-90, expand=True))
        self.update()

    def rotate_left(self):
        self.history.append(self.history[self.idx].rotate(90, expand=True))
        self.update()

    def flip_vertical(self):
        self.history.append(self.history[self.idx].transpose(Image.FLIP_LEFT_RIGHT))
        self.update()

    def prev(self):
        if self.idx == 0:
            raise IndexError("Index out of bounds")
        self.idx -= 1

    def next(self):
        if self.idx >= len(self.history):
            raise IndexError("Index out of bounds")
        self.idx += 1

    def set_text(self, text, color, font, size, x_pos, y_pos):
        font_obj = self.get_font(font, size)
        im = self.get_curr_pic().copy()
        draw_text = ImageDraw.Draw(im)
        x = int((x_pos / self.get_curr_pic().width) * self.get_curr_pic().width)
        y = int((y_pos / self.get_curr_pic().height) * self.get_curr_pic().height)
        draw_text.text((x, y), text, fill=color, font=font_obj)
        self.history.append(im)
        self.update()

    def get_font(self, name, size):
        fonts_folder = 'C:\\Windows\\Fonts'
        match name:
            case 'Arial': return ImageFont.truetype(os.path.join(fonts_folder, 'Arial.ttf'), size)
            case 'Bodoni': return ImageFont.truetype(os.path.join(fonts_folder, 'BOD_R.ttf'), size)
            case 'Garamond': return ImageFont.truetype(os.path.join(fonts_folder, 'garamond.ttf'), size)
            case 'Rockwell': return ImageFont.truetype(os.path.join(fonts_folder, 'Rock.ttf'), size)
            case 'Times New Roman': return ImageFont.truetype(os.path.join(fonts_folder, 'Times.ttf'), size)
            case 'Verdana': return ImageFont.truetype(os.path.join(fonts_folder, 'verdana.ttf'), size)

    def update(self):
        self.history = self.history[:self.idx + 1] + self.history[-1:]
        self.idx = len(self.history) - 1
        self.saved = False


