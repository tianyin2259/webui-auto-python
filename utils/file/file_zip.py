#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : file_zip.py
# @Author: 尘心2259
# @Date  : 2022/6/10 00:15
# @Desc  :

import os
import zipfile
from common.setting import Path


def file_zip(compression_dir, storage_dir):
    """
    将目录下的所有文件压缩成.zip格式
    :param compression_dir: 要压缩的文件夹名
    :param storage_dir: 最终生成的文件名
    :return:
    """
    # 根路径
    root_path = Path.root_path

    startdir = root_path + "/" + compression_dir  # 要压缩的文件夹路径
    file_news = root_path + "/" + storage_dir + ".zip"  # 压缩后文件夹的名字

    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)  # 参数一：文件夹名
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir, '')  # 这一句很重要，不replace的话，就从根目录开始复制
        fpath = fpath and fpath + os.sep or ''  # 这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath + filename)
    z.close()


if __name__ == '__main__':
    file_zip("report", "report")
