#!/usr/bin/env python
# -*- coding:utf-8 -*-

import zipfile


def addzip():
    f = zipfile.ZipFile('test.zip', 'w', zipfile.ZIP_DEFLATED)
    for i in ["../img_zipper/product_1.zip", "../img_zipper/product_2.zip"]:
        file = i.split('/')[-1]
        print(file)
        f.write(i, file)  # 这个file是文件名，意思是直接把文件添加到zip没有文件夹层级， f.write(i)这种写法，则会出现上面路径的层级
        f.setpassword(b"123")
    f.close()


if __name__ == '__main__':
    addzip()
    # for i in ["../img_ziper/product_1.zip", "../img_ziper/product_2.zip"]:
    #     file = i.split('/')[-1]
    #     print(file)