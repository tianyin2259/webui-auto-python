## 框架介绍

本框架主要是基于 Python + Selenium + Pytest + Allure + log + YAML + 钉钉通知 + Jenkins 实现的Web UI自动化框架。


## 技术栈
* Python3.9
* Selenium3

## 目录结构

    ├── basepage                               // 基类
        ├── base.py                            // selenium二次封装
        └── page_baidu.py                      // 页面元素对象、操作封装
    ├── common                                 // 配置
        └── config.yaml                        // 公共配置
        ├── driver_factory.py                  // driver的封装
        └── setting.py                         // 环境路径存放区域
    ├── data                                   // 测试用例数据
    ├── driver                                 // 存放driver驱动
    ├── logs                                   // 日志层
    ├── picture                                // 存放截图，用于给allure追加附件
    ├── report                                 // 测试报告
    ├── testcase                               // 测试用例代码
    └── utils                                  // 工具类
        ├── allure                             // allure工具类
            ├── allure_report_data.py          // allure报告数据清洗
            └── allure_utils.py                // allure报告追加附件
        ├── data_processing                    // 数据处理
            └── yaml_process.py                // 对读取yaml的数据清洗
        ├── db                                 // 数据库工具类
            └── mysql_utils.py                 // mysql基本操作
        ├── file                               // 文件工具类
            ├── config_utils.py                // .ini文件读取
            ├── excel_utils.py                 // excel文件读取
            ├── file_zip.py                    // 文件压缩
            ├── files_utils.py                 // 文件的处理
            ├── path_utils.py                  // 路径封装
            └── yaml_utils.py                  // yaml文件读写
        ├── log                                // 日志工具类
            ├── loguru_utils.py                // 日志封装
        ├── notify
            ├── dingtalk.py                    // 钉钉通知
            ├── lark.py                        // 飞书通知
            └── send_mail.py                   // 邮件通知
            ├── wechat_send.py                 // 企业微信通知
        ├── other                              // 其他
            ├── codes_utils.py                 // 加密解密
            ├── exceptions.py                  // 异常封装
            ├── get_local_ip.py                // 获取本机ip
            ├── models.py                      // 枚举
        ├── times                              // 时间封装
            └── time_control.py                // 时间工具类
        └── requirements_utils.py              // 批量安装第三方库
    ├── .gitignore                             // git push不上传的目录、文件
    ├── README.md                              // 帮助文档
    ├── requirements.txt                       // 存储项目所用的第三方库
    ├── run.py                                 // 程序运行入口