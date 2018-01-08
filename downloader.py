# coding=utf-8
import requests
import random
from PIL import Image
import os


# 下载csdn图片验证码
def download_pic(url, pic_dir):
    resp = requests.get(url)
    filename = pic_dir + str(random.random()) + ".png"
    with open(filename, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
        f.close()
    im = Image.open(filename)
    if im.size != (48, 20):
        os.remove(filename)
    else:
        print(filename)


if __name__ == '__main__':
    url = 'http://download.csdn.net/index.php/rest/tools/validcode/source_ip_validate'
    train_dir = 'captchas/train/'
    test_dir = 'captchas/test/'
    # for i in range(200):
    #     download_pic(url, train_dir)
    for i in range(50):
        download_pic(url, test_dir)
