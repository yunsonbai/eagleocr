# coding=utf-8
import os
from setuptools import setup


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]

setup(
    name="eagleocr",
    version="0.1.1",
    packages=get_packages('eagleocr'),
    author="yunsonbai",
    author_email='1942893504@qq.com',
    url="http://www.yunsonbai.top",
    description='Image text recognition',
    install_requires=[
        'Pillow==3.2.0', 'opencv-python==3.2.0.7', 'numpy==1.13.1',
        'tesserocr==2.2.2'],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
