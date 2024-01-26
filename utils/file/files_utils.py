#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : files_utils.py
# @Author: 尘心2259
# @Date  : 2022/6/9 16:48
# @Desc  :
import os
import re
import traceback

from utils.log.loguru_utils import Logger


def get_all_files(file_path):
    """
    获取文件路径
    :param file_path: 目录路径
    :return:
    """

    try:
        filename = []
        # 获取所有文件下的子文件名称
        for root, dirs, files in os.walk(file_path):
            for filePath in files:
                path = os.path.join(root, filePath)
                filename.append(path)
        return filename

    except Exception:
        Logger().error(traceback.format_exc())


def get_file_name(file_path):
    """
    获取文件的名称
    :param file_path: 文件路径
    :return:
    """
    try:
        if "/" in file_path:
            return file_path.split("/")[-1]
        elif "\\" in file_path:
            return file_path.split("\\")[-1]
    except Exception:
        Logger().error(traceback.format_exc())


def creat_path(dir_name, file_name=None):
    """
    创建多级目录+文件
    :param dir_name: 目录名称
    :param file_name: 文件名称
    :return:
    """
    try:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        if file_name is not None:
            with open(dir_name + os.sep + file_name, 'w', encoding="utf-8"):
                pass
    except Exception:
        Logger().error(traceback.format_exc())


def get_test_py_name(filepath):
    """
    获取testcase目录下的test_开头或_test结尾.py文件名称
    :param filepath:
    :return:
    """
    try:
        file = get_all_files(filepath)

        files = []
        for i in file:
            split_i = str(i.split("/")[-1])
            if split_i.startswith("test_") and split_i.endswith(".py"):
                if split_i not in files:
                    files.append(split_i)
            if split_i.endswith("_test.py"):
                if split_i not in files:
                    files.append(split_i)
        return files
    except Exception:
        Logger().error(traceback.format_exc())


def get_test_py_path(filepath):
    """
    获取testcase目录下的test_开头或_test结尾的.py文件的绝对路径，用例批量跑testcase文件
    :param filepath:
    :return:
    """
    try:
        files = get_all_files(filepath)
        # print(files)
        new_files = []

        for file in files:
            # file = file.split("/")
            # test_file = file[-1:][0]
            test_file = os.path.basename(file)  # 返回path最后的文件名
            if test_file.startswith("test_") and test_file.endswith(".py"):
                # new_files.append('/'.join(file))
                if file not in new_files:
                    new_files.append(file)
            if test_file.endswith("_test.py"):
                if file not in new_files:
                    new_files.append(file)
        return new_files
    except Exception:
        Logger().error(traceback.format_exc())


def creat_init_py(file_path):
    """
    判断不同层级下的目录是否存在__init__.py文件，如果不存在则创建
    :param file_path:
    :return:
    """
    page = '''# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : __init__.py
# @Author:
# @Date  :
# @Desc  :
    '''

    try:
        for root, dirs, files in os.walk(file_path):
            creat_path_name = f"{root}{os.sep}__init__.py"
            # 文件不存在则创建
            if not os.path.isfile(creat_path_name):
                # 通过with open创建文件
                with open(creat_path_name, "w", encoding="utf-8") as f:
                    f.write(page)
    except Exception:
        Logger().error(traceback.format_exc())


def delete_all_files(file_path):
    """
    删除目录下的文件
    :param file_path:
    :return:
    """
    try:
        # 如果是文件直接删除
        if os.path.isfile(file_path):
            os.remove(file_path)
        # 递归删除目录下的文件
        elif os.path.isdir(file_path):
            for i in os.listdir(file_path):
                j = os.path.join(file_path, i)
                if os.path.isdir(j):
                    delete_all_files(j)
                else:
                    os.remove(j)
        # 删除空目录
        if os.path.isdir(file_path):
            os.removedirs(file_path)

    except Exception:
        Logger().error(traceback.format_exc())


def file_capitalize(file_path):
    """
    需求：根据文件名命名类名格式

    将文件名首字母转换为大写，并去掉后缀，最终返回名称。
    :param file_path:
    :return:
    """
    try:
        # 获取文件名
        filename = get_file_name(file_path)

        # 判断名称是否有_
        if "_" in filename:
            # 根据_切割
            spilt_name = str(filename).split("_")
            '''
            将切割后的值首字母大写，然后在拼接
            '''
            files = []  # 存储首字母转换后数据
            for i in spilt_name:
                c_i = i.capitalize()  # 将首字母转换为大写
                files.append(c_i)
            files2 = ''.join(files)  # 拼接最终转换首字母大写的数据
        else:
            files2 = filename.capitalize()

        # 返回转换后名称
        return files2.split(".")[:-1][0]

    except Exception:
        Logger().error(traceback.format_exc())


def file_strip(path):
    """
    去除文件后缀
    """
    strip_list = [".yaml", ".yml", ".json", ".csv", ".xlsx", ".xls"]

    try:
        get_suffix = "." + path.split(".")[-1]
        if get_suffix in strip_list:
            result = path.strip(get_suffix)
            return result
        else:
            Logger.warning(f"不支持该文件后缀: {path}")
            return f"不支持该文件后缀: {path}"

    except Exception:
        Logger().error(traceback.format_exc())


if __name__ == '__main__':
    a = get_test_py_name("/Users/cx2259/project/hengshi/api_auto_test/testcases/yanshi")
    print(a)
