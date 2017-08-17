# coding=utf-8
import numpy
from eagleocr.tools import arrayTool


def _check_x(rows):
    '''
    rows: list([[1, 3], [4, 6], [7, 9]])
    '''
    # 字上下距离
    word_dis = []
    # 字间距
    words_dis = []
    rows_len = len(rows)
    if rows_len <= 1:
        return rows
    for i in range(rows_len - 1):
        word_dis.append(rows[i][1] - rows[i][0])
        words_dis.append(rows[i + 1][0] - rows[i][1])
    word_dis.append(rows[i + 1][1] - rows[i + 1][0])
    word_dis_mean = arrayTool.mean_without_poles(word_dis)
    words_dis_mean = arrayTool.mean_without_poles(words_dis)
    # 字高比例判断标准
    wsd = 1.45
    # 字上下间距比例判断标准
    wssd = 1.35
    new_rows = []
    i = 0
    while i < rows_len - 1:
        if word_dis_mean / word_dis[i] < wsd or i == 0:
            new_rows.append(rows[i])
            i += 1
            continue

        # 与上一个字的距离比平均字距小的多
        if words_dis_mean / (words_dis[i - 1] + 0.00001) >= wssd:
            new_word_heigh = rows[i][1] - new_rows[-1][0]
            if new_word_heigh / word_dis_mean < wsd:
                new_rows[-1][1] = rows[i][1]
            else:
                new_rows.append(rows[i])
            i += 1
            continue

        # 与下一个字没有距离
        # 与下一个字的距离比平均字距小的多
        if words_dis_mean / (words_dis[i] + 0.00001) >= wssd:
            new_word_heigh = rows[i + 1][1] - rows[i][0]
            if new_word_heigh / word_dis_mean < wsd:
                new_rows.append(
                    [rows[i][0], rows[i + 1][1]])
                i += 1
            else:
                new_rows.append(rows[i])
            i += 1
            continue

        # 分界不明显的时候判断
        # 与上下字的间距比较
        if words_dis[i - 1] < word_dis[i]:
            new_word_heigh = rows[i][1] - new_rows[-1][0]
            if new_word_heigh / word_dis_mean < wsd:
                new_rows[-1][1] = rows[i][1]
            else:
                new_rows.append(rows[i])
        else:
            new_word_heigh = rows[i + 1][1] - rows[i][0]
            if new_word_heigh / word_dis_mean < wsd:
                new_rows.append(
                    [rows[i][0], rows[i + 1][1]])
                i += 1
            else:
                new_rows.append(rows[i])
        i += 1

    if word_dis_mean / word_dis[-1] >= wsd:
        if words_dis[-1] / words_dis_mean < wssd:
            new_rows[-1][1] = rows[-1][1]
    else:
        new_rows.append(rows[-1])
    return new_rows


def get_words_x(img_array, sf=1.0):
    '''
    img_array: numpy.array from img
    '''
    n = len(img_array)
    rows = []
    tmp_row = []
    first = True
    standard = (
        numpy.zeros(len(img_array[0])) + 255).sum()
    sums_s = img_array.sum(axis=1) / standard
    dart = 1
    s_p = 1.0 - sums_s.var() * (
        img_array.var() / standard) * sf * dart
    for row in range(n):
        d_p = img_array[row].sum() / standard
        if (first is True) and (d_p < s_p):
            if row < 1:
                tmp_row.append(row)
            else:
                tmp_row.append(row - 1)
            first = False
        elif (first is False) and (d_p >= s_p):
            tmp_row.append(row)
            rows.append(tmp_row)
            tmp_row = []
            first = True
    rows = _check_x(rows)
    return rows


def get_words_y(img_array, transposed=False, sf=1.0):
    '''
    img_array: numpy.array from img
    transposed: bool
    '''
    word_y = []
    rows_x = get_words_x(img_array, sf=sf)
    for rows in rows_x:
        tmp_arrary = img_array[rows[0]: rows[1]]
        if tmp_arrary.mean() > 230:
            continue
        word_y.append([rows[0], rows[1]])
    return word_y


def get_words_position(img_array, transpose, sf=1.0):
    '''
    img: Image
    transpose: bool
    '''
    rows_x = get_words_x(img_array, sf=sf)
    rows_y = []
    for rows in rows_x:
        row_img = img_array[rows[0]:rows[1]]
        word_y = get_words_y(
            row_img.transpose(),
            transposed=transpose, sf=sf)
        rows_y.append(word_y)

    position = {}
    lenth = len(rows_x)
    j = 0
    for i in range(lenth):
        x = rows_x[i]
        for y in rows_y[i]:
            position[j] = [[x[0], x[1]], [y[0], y[1]]]
            j += 1
    return position
