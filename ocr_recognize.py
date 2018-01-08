# coding= utf-8
import pytesseract
import os
from PIL import Image
import cv2
import numpy as np


def get_code(filename):
    img = Image.open(filename)
    code = pytesseract.image_to_string(img)
    img = np.array(img)
    print(code)
    return code, img


# for file in os.listdir('temp/clear_noise'):
#     file = 'temp/clear_noise/' + file
#     code, img = get_code(file)
#     print(file)
#     if code in os.listdir('temp/features'):
#         print(file + ' is ok!')
#         cv2.imwrite('temp/features/' + code + '.png', img)
get_code('111.jpg')
