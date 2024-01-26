#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : requirements_utils.py
# @Author: 尘心2259
# @Date  : 2022/7/14 21:42
# @Desc  : 导出和安装python使用的第三方库
import os

from common.setting import Path

root_path = Path.root_path
path = Path.root_path + os.sep + "requirements.txt"


def freeze():
    """
    导出当前环境所有依赖库
    :return:
    """
    os.system(f"pip3 freeze > {path}")


def pipreqs():
    """
    导出当前项目的依赖库，有可能导出的不全，需要手动添加下
    :return:
    """
    pip_list = os.popen("pip3 list")
    result = pip_list.read()

    if "pipreqs" in result:
        os.system(f"pipreqs {root_path} --encoding=utf-8 --force")
    else:
        os.system(f"pip3 install pipreqs -i https://mirrors.aliyun.com/pypi/simple/")
        os.system(f"pipreqs {root_path} --encoding=utf-8 --force")


def install():
    """
    豆瓣 https://pypi.doubanio.com/simple/
    网易 https://mirrors.163.com/pypi/simple/
    阿里云 https://mirrors.aliyun.com/pypi/simple/
    腾讯云 https://mirrors.cloud.tencent.com/pypi/simple
    清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
    :return:
    """

    if os.path.isfile(path):
        os.system(f"pip3 install -r {path} -i https://mirrors.aliyun.com/pypi/simple/")
    else:
        freeze()
        os.system(f"pip3 install -r {path} -i https://mirrors.aliyun.com/pypi/simple/")


if __name__ == '__main__':
    # freeze()
    pipreqs()
    # install()
