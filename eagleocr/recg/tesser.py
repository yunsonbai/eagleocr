import tesserocr


def get_word_txt(img, lang, psm):
    txt = tesserocr.image_to_text(img, lang=lang, psm=psm)
    if txt:
        return txt
    return ''
