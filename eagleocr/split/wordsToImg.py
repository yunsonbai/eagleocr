# coding=utf-8
import numpy
from eagleocr.lib import colorChange
from eagleocr.split import wordPosition
from PIL import Image


def _word_position(img_array, sf):
    position = wordPosition.get_words_position(
        img_array, sf=sf)
    return position


def _get_word(x, y, img_array):
    word_array = img_array[x[0]: x[1], y[0]: y[1]]
    return word_array


def _get_word_img(word_array, hyaline=False):
    word = Image.fromarray(word_array)
    if hyaline is True:
        word = colorChange.hyaline(word)
    return word


def words_2_img(img_2v, sf, hyaline=True):
    img_array = numpy.array(img_2v)
    position = _word_position(img_array, sf)
    wnames = {}
    for k in position.keys():
        x = position[k][0]
        y = position[k][1]
        word_array = _get_word(x, y, img_array)
        name = '{0}.png'.format(k)
        word = _get_word_img(word_array, hyaline=hyaline)
        wnames[k] = {'name': name, 'x': x, 'y': y, 'img': word}
    return wnames
