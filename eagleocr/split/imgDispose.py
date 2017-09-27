# coding=utf-8
import numpy
from PIL import Image
from eagleocr.lib import imgCorrect
from eagleocr.lib import imgDenoise


def get_2v_img(source_img, sf=1.0):
    '''
    img: Image
    return:
        2v_img and sf(本次处理依据全局参数)
    '''
    w, h = source_img.size
    var_s = 5000
    noiseimg = imgDenoise.denoisecolor(source_img)
    # img = imgCorrect.contrast(noiseimg, p=5.0)
    img = imgCorrect.contrast(noiseimg, p=2.0)
    img = img.convert("L")
    img_array = numpy.array(img)
    sf = img_array.var() / var_s
    mean = img_array.mean() - 80 * (1 - sf)

    img_array = img_array * 1.15
    tmp_array = img_array - mean
    tmp_array = numpy.maximum(tmp_array, 0)
    tmp_array = numpy.minimum(tmp_array, 1)
    tmp_array = tmp_array * 255
    tmp_array = tmp_array.astype(numpy.uint8)
    img = Image.fromarray(tmp_array)

    return img, sf


def rgba_get_2v_img(img):
    '''
    rgba img to 2v img
    '''
    x, y = img.size
    p = Image.new('RGBA', img.size, (255, 255, 255))
    p.paste(img, (0, 0, x, y), img)
    return p
