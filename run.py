#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : run.py
# @Author: 尘昊2259
# @Date  : 2022/2/20 13:56
# @Desc  :
import os
import pytest
from common.setting import Path
from utils.allure.allure_report_data import AllureFileClean
from utils.log.loguru_utils import Logger
from utils.notify.dingtalk import DingTalkSendMsg
from utils.notify.lark import FeiShuTalkChatBot
from utils.notify.send_mail import SendEmail
from utils.notify.wechat_send import WeChatSend
from utils.other.models import NotificationType
from utils import config


def run(case_dir):
    case_path = Path.case_path + case_dir

    Logger().info(

        """
             ____ ___ .___        _____    ____ ___ ___________________    
            |    |   \|   |      /  _  \  |    |   \\__    ___/\_____  \   
            |    |   /|   |     /  /_\  \ |    |   /  |    |    /   |   \  
            |    |  / |   |    /    |    \|    |  /   |    |   /    |    \ 
            |______/  |___|    \____|__  /|______/    |____|   \_______  / 
                                       \/                              \/                                                        
        """
    )
    """
    --reruns: 失败重跑次数。
    --count: 重复执行次数
    -v: 显示错误位置以及错误的详细信息
    -s: 等价于 pytest --capture=no 可以捕获print函数的输出
    -q: 简化输出信息
    -m: 运行指定标签的测试用例
    -x: 一旦错误，则停止运行
    --maxfail: 设置最大失败次数，当超出这个阈值时，则不会在执行测试用例
    "--reruns=3", "--reruns-delay=2"
     """
    pytest.main([f'{case_path}',
                 '-s',
                 # '-n=2', #表示2个进程启动
                 '--alluredir', './report/tmp', "--clean-alluredir"
                 ]
                )

    os.system(r"allure generate ./report/tmp -o ./report/html --clean")
    allure_data = AllureFileClean().get_case_count()
    notification_mapping = {
        NotificationType.DING_TALK.value: DingTalkSendMsg(allure_data).send_ding_notification,
        NotificationType.WECHAT.value: WeChatSend(allure_data).send_wechat_notification,
        NotificationType.EMAIL.value: SendEmail(allure_data).send_main,
        NotificationType.FEI_SHU.value: FeiShuTalkChatBot(allure_data).post
    }

    if config.notification_type != NotificationType.DEFAULT.value:
        notification_mapping.get(config.notification_type)()

    # 程序运行之后，自动启动报告，如果不想启动报告，可注释这段代码
    # os.system(f"allure serve ./report/tmp -h 127.0.0.1 -p 9999")


if __name__ == '__main__':
    run("test_baidu.py")
