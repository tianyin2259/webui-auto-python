#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : path_utils.py
# @Author: 尘昊2259
# @Date  : 2022/2/12 14:47
# @Desc  :

import os


class PathBase:
    def __init__(self):
        # 获取当前的真实路径
        self.path = os.path.abspath(__file__)

    def get_name(self, path):
        """
        根据路径获取脚本名称
        :param path: 需要获取名称的路径
        :return: 返回名称
        """
        return os.path.basename(path)

    def get_path(self, path):
        """
        根据路径，获取文件夹路径。获取的传入路径的上一级目录

        :param path: 传入路径
        :return: 返回文件路径
        """
        return os.path.dirname(path)

    def join_path(self, path, *path_str):
        """
        拼接路径
        :param path: 愿路径
        :param path_str: 待拼接的路径
        :return:
        """

        param = "/".join(i for i in path_str)
        return os.path.join(path, param)

    def path_true(self, path):
        """
        判断文件夹是否存在
        :param path:
        :return:
        """
        return os.path.exists(path)

    def create_path(self, path):
        """
        创建文件
        :param path:
        :return:
        """

        try:
            os.mkdir(path)
        except:
            return False
        else:
            return True


# if __name__ == '__main__':
#     a = PathBase()
#     print(a.get_path(a.get_path(__file__)))
