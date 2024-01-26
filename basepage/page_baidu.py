#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : webui_auto_python
# @File    : page_baidu.py
# @Time    : 2023-02-07 14:20:18
# @User    : cx2259
# @Author  : chen xin
# @Description :
import os
from basepage.base import Base
from selenium.webdriver.common.by import By


class PageBaidu(Base):
    url = "https://www.baidu.com/"
    # 百度输入框
    send_bd = By.XPATH, '//*[@id="kw"]'
    # 点击百度一下
    click_button = By.XPATH, '//*[@id="su"]'

    def search(self, send_text, picture_path=None):
        """
        打开百度地址，搜索指定内容
        :return:
        """
        self.get_url("打开地址", self.url, picture_path=picture_path)
        self.send("输入内容", send_text, self.send_bd, picture_path=picture_path)
        self.click("点击百度一下", self.click_button, picture_path=picture_path)


if __name__ == '__main__':
    PageBaidu().search("ChatGPT")
