#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : webui_auto_python
# @File    : yaml_process.py
# @Time    : 2023-02-23 18:35:17
# @User    : cx2259
# @Author  : 大君
# @Description :
import traceback

from utils.file.yaml_utils import YamlUtils
from utils.log.loguru_utils import Logger


class YamlProcess(YamlUtils):
    def __int__(self):
        super().__init__()

    def case_data(self, filename):
        try:
            results = self.read_yaml(self.data_path + filename)

            # 存储最终数据
            all_list = {}

            # 存储最终用例的数据
            test_data = []
            for k, v in results.items():
                if k == "case_common":
                    for case_common_k, case_common_v in v.items():
                        all_list[case_common_k] = case_common_v
                else:
                    # 存储case_name
                    data = [v["case_name"]]

                    # 存储测试数据
                    data2 = []

                    for j in v["data"]:
                        data2.append(j)
                    data2.append(v["assert"]["msg"])

                    # 将测试数据和预期结果存入case_name中
                    # [用例名称,[测试数据，预期结果]]
                    data.append(data2)

                    # 存储最终的数据
                    # [[用例名称,[测试数据，预期结果]],[用例名称2,[测试数据2，预期结果2]]]
                    test_data.append(data)

            all_list["data"] = test_data
            return all_list

        except Exception as e:
            Logger().error(traceback.format_exc())


if __name__ == '__main__':
    a = YamlProcess().case_data("baidu/search.yaml")
    for i in a["data"]:
        print(i[1])
