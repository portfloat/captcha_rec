# coding=utf-8
from PIL import Image
import numpy as np
import os
from csdn.split import split
import cv2


# 二值化
def get_binary_pix(img):
    # img = np.array(img)
    #
    # rows, clos = img.shape
    # for i in range(rows):
    #     for j in range(clos):
    #         if img[i, j] <= 128:
    #             img[i, j] = 0
    #         else:
    #             img[i, j] = 1
    img = cv2.imread(img, 0)
    img = cv2.threshold(img, 180, 1, 1)
    pix = np.ravel(img)
    return pix




def get_files(dirs):
    f = os.listdir(dirs)
    fs = []
    for name in f:
        fr = dirs + "/" + name
        fs.append(fr)
    return fs


def write_train_file(content):
    with open("train_data.txt", "a+") as f:
        f.write(content)
        f.write('\n')


def write_predict_file(content):
    with open("test_data.txt", "a+") as f:
        f.write(content)
        f.write('\n')


def load_predict_pic(img):
    for im in split(img):
        # print(im)
        pixs = get_binary_pix(im).tolist()
        pixs = [str(i) for i in pixs]
        content = ",".join(pixs)
        write_predict_file(content)
    test_data = np.loadtxt('test_data.txt', delimiter=',')
    return test_data


# if __name__ == '__main__':
#     for i in range(10):
#         for file in os.listdir('temp/features/' + str(i)):
#             file = 'temp/features/' + str(i) + "/" + file
#             img = Image.open(file)
#             pixs = get_binary_pix(img).tolist()
#             pixs.append(i)
#             pixs = [str(i) for i in pixs]
#             content = ",".join(pixs)
#             write_train_file(content)
# load_predict_pic('csdn1.png')
