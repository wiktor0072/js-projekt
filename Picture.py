from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageFont, ImageDraw
import os


class Picture:

    def __init__(self, path):
        self.history = [Image.open(path)]   # history of edition
        self.saved = True                   # informs if image bounded with current idx was saved
        self.idx = 0                        # index of current image
        self.unfiltered = None              # picture that wasn't affected by any filters
        self.filter_counter = 0

    def __getitem__(self, item):
        return self.history[item]

    def append(self, val):
        self.history.append(val)
        self.idx = len(self.history) - 1

    def get_curr_pic(self):
        return self.history[self.idx]

    def rotate_right(self):
        self.history.append(self.get_curr_pic().rotate(-90, expand=True))
        self.update()

    def rotate_left(self):
        self.history.append(self.get_curr_pic().rotate(90, expand=True))
        self.update()

    def flip_vertical(self):
        self.history.append(self.get_curr_pic().transpose(Image.FLIP_LEFT_RIGHT))
        self.update()

    def prev(self):
        if self.idx == 0:
            raise IndexError("Index out of bounds")
        self.idx -= 1
        if self.idx == 0:
            self.saved = True

    def next(self):
        if self.idx >= len(self.history):
            raise IndexError("Index out of bounds")
        self.idx += 1

    def is_last(self):
        if self.idx == len(self.history) - 1:
            return True
        return False

    def is_first(self):
        if self.idx == 0:
            return True
        return False

    def set_brightness(self, value):
        return ImageEnhance.Brightness(self.get_curr_pic()).enhance(value/50)

    def set_contrast(self, value):
        return ImageEnhance.Contrast(self.get_curr_pic()).enhance(value/50)

    def get_unfiltered(self):
        self.history.append(self.unfiltered)
        self.filter_counter = 0
        self.idx = len(self.history) - 1

    def set_black_white_filter(self):
        self.history.append(self.get_curr_pic().convert('L'))
        self.idx = len(self.history) - 1

    def set_sepia_tone_filter(self):
        self.history.append(ImageEnhance.Color(self.get_curr_pic()).enhance(0.5))
        self.update()

    def set_inverted_colors(self):
        self.history.append(ImageOps.invert(self.get_curr_pic()))
        self.update()

    def sharpen_edges(self):
        self.history.append(self.get_curr_pic().filter(ImageFilter.SHARPEN))
        self.update()

    def change_filter(self, filter):
        # if counter is set to 0, it means the image hasn't been filtered yet, and we can assign it to unfiltered
        # variable which would be unfiltered one
        if self.filter_counter == 0:
            self.unfiltered = self.get_curr_pic().copy()
        self.filter_counter += 1
        match filter:
            case 'Normal': self.get_unfiltered()
            case 'Black-white': self.set_black_white_filter()
            case 'Sepia tone': self.set_sepia_tone_filter()
            case 'Inverted': self.set_inverted_colors()
            case 'Sharpen': self.sharpen_edges()

    def set_text(self, text, color, font, size, x_pos, y_pos):
        font_obj = self.get_font(font, size)
        im = self.get_curr_pic().copy()
        draw_text = ImageDraw.Draw(im)
        # rescaling coordinates in order to be accurate to real size of the image
        x = int((x_pos / self.get_curr_pic().width) * self.get_curr_pic().width)
        y = int((y_pos / self.get_curr_pic().height) * self.get_curr_pic().height)
        draw_text.text((x, y), text, fill=color, font=font_obj)
        self.history.append(im)
        self.update()

    def get_font(self, name, size):
        # returns a font object depending on string
        fonts_folder = 'C:\\Windows\\Fonts'
        match name:
            case 'Arial': return ImageFont.truetype(os.path.join(fonts_folder, 'Arial.ttf'), size)
            case 'Bodoni': return ImageFont.truetype(os.path.join(fonts_folder, 'BOD_R.ttf'), size)
            case 'Garamond': return ImageFont.truetype(os.path.join(fonts_folder, 'garamond.ttf'), size)
            case 'Rockwell': return ImageFont.truetype(os.path.join(fonts_folder, 'Rock.ttf'), size)
            case 'Times New Roman': return ImageFont.truetype(os.path.join(fonts_folder, 'Times.ttf'), size)
            case 'Verdana': return ImageFont.truetype(os.path.join(fonts_folder, 'verdana.ttf'), size)

    def crop_image(self, parameters):
        parameters = [int(num) for num in parameters]
        self.check_coordinates(parameters, 0, 2)
        self.check_coordinates(parameters, 1, 3)
        self.history.append(self.get_curr_pic().crop(tuple(parameters)))
        self.update()

    def check_coordinates(self, coords, idx1, idx2):
        # checks if starting coordinate is bigger than second one, if so the indexes are switched
        if coords[idx1] > coords[idx2]:
            temp = coords[idx1]
            coords[idx1] = coords[idx2]
            coords[idx2] = temp

    def resize_image(self, parameters):
        # parameters variable contains tuple of new width and size of an image
        parameters = tuple(int(num) for num in parameters)
        self.history.append(self.get_curr_pic().resize(parameters))
        self.update()

    def add_picture(self, path, width, height, x_pos, y_pos):
        img_to_add = Image.open(path).resize((int(width), int(height))).convert('RGBA')
        copy = self.get_curr_pic().copy()
        copy.paste(img_to_add, (int(x_pos), int(y_pos)), img_to_add)
        self.history.append(copy)
        self.update()

    def update(self):
        # deletes objects of images in bounds between previous view picture and just created one
        self.history = self.history[:self.idx + 1] + self.history[-1:]
        self.idx = len(self.history) - 1
        self.saved = False

    def save(self, path):
        self.get_curr_pic().save(path)
        self.saved = True


