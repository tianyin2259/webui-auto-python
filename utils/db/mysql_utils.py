#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : mysql_utils.py
# @Author: 尘昊2259
# @Date  : 2022/2/15 21:07
# @Desc  : mysql操作
import traceback

import pymysql

from common.setting import Path
from utils.file.yaml_utils import YamlUtils
from utils.log.loguru_utils import Logger

db_info = YamlUtils().read_yaml(Path.common_path + "config.yaml")


class MysqlUtil:
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=db_info['mysql_db']['host'],
            user=db_info['mysql_db']['user'],
            password=db_info['mysql_db']['password'],
            database=db_info['mysql_db']['database'],
            port=db_info['mysql_db']['port'],
            charset='utf8'
        )
        # 创建游标
        self.cursor = self.connect.cursor()

    def select_all(self, execute_sql):
        """

        :param execute_sql:
        :return:
        """
        try:
            # 执行的sql语句
            sql = f'''{execute_sql}'''
            # 执行sql
            self.cursor.execute(sql)
            # 提交事务
            self.connect.commit()
            # 关闭连接
            self.connect.close()
            return self.cursor.fetchall()
        except Exception as e:
            Logger().error(traceback.format_exc())

    def select_one(self, execute_sql):
        """

        :param execute_sql:
        :return:
        """
        try:
            # 执行的sql语句
            sql = f'''{execute_sql}'''
            # 执行sql
            self.cursor.execute(sql)
            # 提交事务
            self.connect.commit()
            # 关闭连接
            self.connect.close()
            return self.cursor.fetchone()
        except Exception as e:
            Logger().error(traceback.format_exc())

    def delete(self, table, contins):
        """

        :param table:
        :param contins:
        :return:
        """
        try:
            # 执行的sql语句
            sql = f'''delete from {table} where {contins}'''
            # 执行sql
            self.cursor.execute(sql)
            # 提交事务
            self.connect.commit()
            # 关闭连接
            self.connect.close()
        except Exception as e:
            Logger().error(traceback.format_exc())


if __name__ == '__main__':
    obj = MysqlUtil()
    # obj.delete("tb_incident", "description like '%api_auto%'")
    a = obj.select_all("select description from tb_incident where description like '%api_auto%' ")
    # print(a)
