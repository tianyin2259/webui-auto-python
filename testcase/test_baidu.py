#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : webui_auto_python
# @File    : test_baidu.py
# @Time    : 2023-02-08 15:34:15
# @User    : cx2259
# @Author  : chen xin
# @Description :
import allure
import pytest
from basepage.page_baidu import PageBaidu
from utils.data_processing.yaml_process import YamlProcess

path = "baidu/search.yaml"
data = YamlProcess().case_data(path)
case_name = [i[0] for i in data["data"]]
test_data = [i[1] for i in data["data"]]



@allure.epic(data["allure_epic"])
@allure.feature(data["allure_feature"])
class TestBaidu:
    base_page_obj = PageBaidu()

    @allure.story(data["allure_story"])
    @pytest.mark.parametrize("text,er", test_data, ids=case_name)  # ids标记用例名称，增加可读性
    def test_search(self, text, er):

        try:
            self.base_page_obj.search(text, path)
            assert er == "ok"
        except Exception:
            self.base_page_obj.quit()

    # 动态标题
    # @allure.story(data["allure_story"])
    # @allure.title("百度搜索—{title}")
    # @pytest.mark.parametrize("text,er,title", [['大君', 'ok', '输入中文搜索'], ['ChatGPT', 'ok', '输入英文搜索']])
    # def test_search(self, text, er, title):
    #
    #     try:
    #         self.base_page_obj.search(text)
    #         assert er == "ok"
    #     except Exception:
    #         self.base_page_obj.quit()

    def teardown_class(self):
        self.base_page_obj.quit()


if __name__ == '__main__':
    pytest.main()
