# coding=utf-8
from PIL import ImageEnhance
from PIL import ImageFilter


def tow_value(img):
    new_img = img.filter(ImageFilter.EDGE_ENHANCE)
    return new_img.convert("1")


def gray(img):
    new_img = img.filter(ImageFilter.EDGE_ENHANCE)
    return new_img.convert("L")


def bright_strong(img, p=2.0):
    brightness = ImageEnhance.Brightness(img)
    return brightness.enhance(p)


def sharpen(img, p=5.0):
    sharpness = ImageEnhance.Sharpness(img)
    return sharpness.enhance(p)


def contrast(img, p=2):
    contrast = ImageEnhance.Contrast(img)
    return contrast.enhance(p)
