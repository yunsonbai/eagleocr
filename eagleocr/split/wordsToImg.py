# coding=utf-8
import numpy
from eagleocr.lib import colorChange
from eagleocr.split import wordPosition
from eagleocr.split import imgDispose
from PIL import Image


def _get_2v_img(img_path):
    img = Image.open(img_path)
    img_2v, sf = imgDispose.get_2v_img(img)
    return img_2v, sf


def _word_position(img_array, sf, transpose=False):
    position = wordPosition.get_words_position(
        img_array, transpose, sf=sf)
    return position


def _get_word(x, y, img_array, transpose):
    word_array = img_array[x[0]: x[1], y[0]: y[1]]
    if transpose is True:
        word_array = word_array.transpose()
    return word_array


def _save_word_img(word_array, img_name, hyaline=False):
    word = Image.fromarray(word_array)
    if hyaline is True:
        word = colorChange.hyaline(word)
    word.save(img_name)


def words_2_img(img_path, save_folder, trans=True, hyaline=True):
    img_2v, sf = _get_2v_img(img_path)
    img_array = numpy.array(img_2v)
    if trans is True:
        img_array = img_array.transpose()
    position = _word_position(img_array, sf, transpose=trans)
    for k in position.keys():
        x = position[k][0]
        y = position[k][1]
        word_array = _get_word(x, y, img_array, trans)
        img_name = '{0}/{1}.png'.format(save_folder, k)
        _save_word_img(word_array, img_name, hyaline=True)
