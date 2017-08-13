from PIL import Image
from eagleocr.split import imgDispose
from eagleocr.split import wordsToImg


base_path = '/path'
img_path = base_path + '/a17.png'
save_folder = base_path + '/word_img'

img = Image.open(img_path)
img_2v, sf = imgDispose.get_2v_img(img)
wnames = wordsToImg.words_2_img(img_2v, sf, save_folder)
print(wnames)
