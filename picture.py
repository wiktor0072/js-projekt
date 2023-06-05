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


