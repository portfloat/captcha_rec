# coding=utf-8
import numpy as np
from sklearn.svm import SVC
from sklearn import cross_validation as cs
from sklearn.externals import joblib as jl
from csdn.pic2data import load_predict_pic
import os

PKL = 'modle.pkl'

def load_data():
    dataset = np.loadtxt('./datesets/train_data.txt', delimiter=',')
    return dataset


def cross_validation():
    dataset = load_data()
    raw, col = dataset.shape
    X = dataset[:, :col - 1]
    print(X.shape)
    Y = dataset[:, -1]
    print(Y.shape)
    clf = SVC()
    scores = cs.cross_val_score(clf, X, Y, cv=5)
    print(scores.mean(), scores.std() * 2)


def train():
    dataset = load_data()
    raw, col = dataset.shape
    X = dataset[:, :col - 1]
    Y = dataset[:, -1]
    clf = SVC()
    clf.fit(X, Y)
    jl.dump(clf, PKL)


def predict(img, imgname):
    clf = jl.load(PKL)
    test = load_predict_pic(img)
    value = []
    for data in test:
        data = [data]
        value.append(clf.predict(data)[0])
    predict_value = [str(int(i)) for i in value]
    predict_value = ''.join(predict_value)
    print(imgname + " 验证码：%s" % predict_value)
    open('./datesets/test_data.txt', 'w').close()
    return predict_value


if __name__ == '__main__':
    # cross_validation()
    count = 0
    success = 0
    for img in os.listdir('captchas/test'):
        if img.endswith('.png'):
            filename = 'captchas/test/' + img
            value = predict(filename, img)
            count += 1
            if value + '.png' == img:
                success += 1
    success_rate = success/count
    print("success_rate is : %.2f%%" % (success_rate*100))
