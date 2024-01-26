#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : driver_factory.py
# @Author: 尘昊2259
# @Date  : 2022/2/12 14:01
# @Desc  :

from selenium import webdriver
from selenium.webdriver.common.by import By

from common.setting import Path
from utils.file.path_utils import PathBase


class DriverFactory:
    driver = None

    @classmethod
    def get_driver(cls, driver_path, browser, flag):
        """

        :param driver_path:
        :param browser:
        :param flag:
        :return:
        """
        if cls.driver is None:
            if browser.lower() == "chrome":
                options = webdriver.ChromeOptions()  # 绕过https安全隐私
                options.add_argument('--ignore-ssl-errors=yes')
                options.add_argument('--ignore-certificate-errors')
                cls.driver = webdriver.Chrome(Path.driver_path + driver_path,
                                              chrome_options=options)  # options=options也行

            cls.driver.maximize_window()
            cls.driver.implicitly_wait(30)

        if flag:
            cls.login("admin", 123456)

        return cls.driver

    @classmethod
    def login(cls, user, passwd):
        """
        默认登录
        :param user:
        :param passwd:
        :return:
        """
        pass


if __name__ == '__main__':
    DriverFactory().get_driver("macm1/chromedriver", "chrome", False)
