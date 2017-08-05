# coding=utf-8
import numpy
from PIL import Image
import cv2


def denoisecolor(img):
    '''
    denoise color img
    '''
    img_array = numpy.array(img)
    dst = cv2.fastNlMeansDenoisingColored(
        img_array, None, 10, 10, 7, 21)
    return Image.fromarray(dst)


def denoisegray(img):
    '''
    denoise gray img
    '''
    img_array = numpy.array(img)
    dst = cv2.fastNlMeansDenoising(
        img_array, None, 10, 7, 21)
    return Image.fromarray(dst)
