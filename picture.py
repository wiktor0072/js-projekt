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

    def update(self):
        self.history = self.history[:self.idx + 1] + self.history[-1:]
        self.idx = len(self.history) - 1
        self.saved = False


