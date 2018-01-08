# coding= utf-8
import os
import random
import cv2
from PIL import Image
import numpy as np


def sum_9_region(img, x, y):
    cur_pixel = img.getpixel((x, y))  # 当前像素点的值
    width = img.width
    height = img.height

    if cur_pixel == 255:  # 如果当前点为白色区域,则不统计邻域值
        return 10

    if y == 0:  # 第一行
        if x == 0:  # 左上顶点,4邻域
            # 中心点旁边3个点
            sum = cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))
            return 4 - sum / 255
        elif x == width - 1:  # 右上顶点
            sum = cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1))

            return 4 - sum / 255
        else:  # 最上非顶点,6邻域
            sum = img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1)) \
                  + cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))
            return 6 - sum / 255
    elif y == height - 1:  # 最下面一行
        if x == 0:  # 左下顶点
            # 中心点旁边3个点
            sum = cur_pixel \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y - 1)) \
                  + img.getpixel((x, y - 1))
            return 4 - sum / 255
        elif x == width - 1:  # 右下顶点
            sum = cur_pixel \
                  + img.getpixel((x, y - 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y - 1))

            return 4 - sum / 255
        else:  # 最下非顶点,6邻域
            sum = cur_pixel \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x, y - 1)) \
                  + img.getpixel((x - 1, y - 1)) \
                  + img.getpixel((x + 1, y - 1))
            return 6 - sum / 255
    else:  # y不在边界
        if x == 0:  # 左边非顶点
            sum = img.getpixel((x, y - 1)) \
                  + cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y - 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))

            return 6 - sum / 255
        elif x == width - 1:  # 右边非顶点
            # print('%s,%s' % (x, y))
            sum = img.getpixel((x, y - 1)) \
                  + cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x - 1, y - 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1))

            return 6 - sum / 255
        else:  # 具备9领域条件的
            sum = img.getpixel((x - 1, y - 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1)) \
                  + img.getpixel((x, y - 1)) \
                  + cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y - 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))
            return 9 - sum / 255

# 灰度处理
def split_image(image_name, col_range):
    filename = './temp/gray/' + str(random.random()) + '.png'
    image = cv2.imread(image_name, 0)
    ret, image = cv2.threshold(image, 180, 255, 1)
    height, width = image.shape
    new_image = image[0:height, col_range[0]:col_range[1]]
    cv2.imwrite(filename, new_image)
    img = Image.open(filename)
    return img


def split_before(img, xy):
    img = split_image(img, xy)
    img = clear_noise(img)
    return img

# 切割成4个图片
def split(image_name):
    img1 = split_before(image_name, (5, 5 + 8))
    img2 = split_before(image_name, (14, 14 + 8))
    img3 = split_before(image_name, (23, 23 + 8))
    img4 = split_before(image_name, (32, 32 + 8))
    return img1, img2, img3, img4

# 去除噪点
def clear_noise(img):
    filename = './temp/clear_noise/' + str(random.random()) + '.png'
    x, y = img.width, img.height
    for i in range(x):
        for j in range(y):
            if sum_9_region(img, i, j) < 2:
                # print(img.getpixel((i,j)))
                img.putpixel((i, j), 255)
    img = np.array(img)

    cv2.imwrite(filename, img)
    img = Image.open(filename)
    return img


def main():
    for filename in os.listdir('captchas/train'):
        current_file = 'captchas/train' + filename
        if os.path.isfile(current_file):
            split(current_file)
            print('split file:%s' % current_file)


#
# def main():
#     split('csdn1.png')

if __name__ == '__main__':
    # main()
    # print('done...')
    split_before('6561.png', (0,40))
