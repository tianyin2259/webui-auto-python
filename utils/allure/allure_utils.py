#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : allure.py
# @Author: 尘心2259
# @Date  : 2022/6/8 23:11
# @Desc  :

import allure
from utils.file.files_utils import *
from utils.log.loguru_utils import Logger


def allure_attch_file(path):
    try:

        # 获取图片名称
        pictures_name = os.path.basename(path)
        # 将.jpg的照片添加至allure中
        if path.endswith(".jpg"):
            allure.attach.file(source=path, name=pictures_name, attachment_type=allure.attachment_type.JPG)
        elif path.endswith(".png"):
            allure.attach.file(source=path, name=pictures_name, attachment_type=allure.attachment_type.PNG)
    except Exception as e:
        Logger().error(traceback.format_exc())


def allure_attch(*result):
    """
    实际结果与预期结果不符合，追加文本
    :param reslut:
    :return:
    """
    try:
        allure.attach(f"实际结果: {result[0]}, 预期结果: {result[1]}", name='断言结果')
    except Exception as e:
        Logger().error(traceback.format_exc())


def allure_info(element=None, text=None, picture_path=None, log=None):
    """
        给allure步骤追加元素和截图
    :param element:
    :param text:
    :param picture_path:
    :param log:
    :return:
    """
    try:
        # 追加页面定位的元素
        if element is not None:
            allure.attach(f"{element}", name='页面元素')

        if text is not None:
            # 追加输入内容
            allure.attach(f"{text}", name='输入内容')
        if picture_path is not None:
            # 追加图片
            allure_attch_file(picture_path)
            # 每一步执行完将截图删除，否则allure追加附件会将之前步骤的附件进行累计追加。比如第一个步骤1张图，第二个步骤就是2张图，第三个步骤就是4张图
            delete_all_files(picture_path)
        if log is not None:
            allure.attach(f"{log}", name='报错原因')
    except Exception as e:
        Logger().error(traceback.format_exc())


def allure_step_no(step):
    """
    无附件的操作步骤
    :param step: 步骤名称
    :return:
    """
    try:
        with allure.step(step):
            pass
    except Exception as e:
        Logger().error(traceback.format_exc())
