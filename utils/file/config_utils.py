#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : config_utils.py
# @Author: 尘昊2259
# @Date  : 2022/2/20 15:39
# @Desc  :

import configparser
from common.setting import Path


class ConfigUtils:
    # 实例化
    config = configparser.ConfigParser()

    def __init__(self):

        self.data_path = Path().common_path
        self.path = ".ini"

    def read(self, filename):
        """
        :param filename: 文件名
        :return:
        """
        self.config.read(f"{self.data_path}{filename}{self.path}", encoding="utf-8-sig")
        return self

    def get(self, section, option):
        try:
            # 方法一：调用方法
            value = self.config.get(section=section, option=option)

            # 方法而：索引
            # value = self.config[section][option]

        except Exception as e:
            print("没有获取到值")
            value = None
        return value

    def get_options_key_value(self, section):
        """
       以列表(name,value)的形式返回section中的每个值
         :param _section: 某个section
         :return: list[tuple(key,value)]
        """

        return self.config.items(section)

    def get_all_section(self):
        """
        获取所有section
        """
        return self.config.sections()

    def get_options_by_section(self, section):
        """
        获取section下所有可用options
        :param section:
        :return:
        """

        # # 方式一
        # keys = []
        # for options in self.config[section]:
        #     keys.append(options)

        # 方式二
        keys = self.config.options(section)
        return keys

    def assert_section_in_config(self, section):

        """
         判断section是否存在
         :param _section: 需要判断的section
         """
        return section in self.config

    def assert_options_in_section(self, section, options):

        """
             判断options是否存在某个section中
             :param _section: 某个section
             :param _options: 需要判断的options的key值
             """

        return options in self.config[section]

    def get_hosts(self):
        r = self.read("config")
        return r.get("hosts", "hosts")


if __name__ == '__main__':
    a = ConfigUtils().get_hosts()
    print(a)
