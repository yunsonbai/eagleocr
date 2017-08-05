from eagleocr.split import wordsToImg


base_path = 'base_path'
img_path = base_path + '/a17.png'
save_folder = base_path + '/word_img'

wordsToImg.words_2_img(img_path, save_folder)
