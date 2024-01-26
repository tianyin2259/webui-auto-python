#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : base.py
# @Author: 尘昊2259
# @Date  : 2022/2/12 22:46
# @Desc  : selenium的公共操作封装在这里
from selenium.webdriver.common.keys import Keys
from common.driver_factory import DriverFactory
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from utils.allure.allure_utils import *
from utils.file.files_utils import file_strip
from utils.file.yaml_utils import YamlUtils
from common.setting import Path
from utils.log.loguru_utils import Logger

driver = YamlUtils().read_yaml(Path.common_path + "config.yaml")


class Base:

    def __init__(self, flag=True):
        # 获取driver
        self.driver = DriverFactory().get_driver(driver['driver']['path'], driver['driver']['browser'], flag)

    def screenshot(self, path, name):
        """
        截图
        :param path:截图存储路径
        :param name: 截图名称
        :return:
        """
        try:
            new_picture_path = f'{Path.picture_path}{file_strip(path) + os.sep}'

            # 如果该路径不存在就新建
            if not os.path.exists(new_picture_path):
                # 创建目录
                os.makedirs(new_picture_path)

            """截图"""
            # 获取现在的时间格式，2021-02-24-20-59-21
            # current_time = datetime.datetime.now().strf_time('%Y-%m-%d-%H-%M-%S')
            # 生成的截图格式
            file_name = f'{name}.png'
            # 合并截图路径和图片名称
            file_path = os.path.join(new_picture_path, file_name)
            # 截图
            self.driver.get_screenshot_as_file(file_path)
            Logger.debug(f"截图: {file_name}")
            return file_path

        except Exception as e:
            Logger().error(traceback.format_exc())

    def wait_element(self, by, page_element, step_name):
        """
        元素显示等待。
        :param step_name:
        :param by: 传入的是八大元素定位方式
        :param page_element: 页面的元素
        :return: 返回单个对象
        """
        try:

            element = WebDriverWait(self.driver, timeout=10).until(
                ec.presence_of_element_located(
                    (by, page_element)
                )
            )
            Logger.debug(f"元素定位成功：{page_element}")
            return element

        except Exception as e:
            allure_info(log=f"{step_name}元素可能未找到, 报错原因: {traceback.format_exc()}")
            Logger().error(traceback.format_exc())

    def wait_elements(self, by, page_element, step_name):
        """

        :param page_element:
        :param step_name:
        :param by:
        :return: 返回多个对象
        """
        try:
            element = WebDriverWait(self.driver, timeout=10).until(
                ec.presence_of_all_elements_located(
                    (by, page_element)
                )
            )
            Logger.debug(f"元素定位成功：{page_element}")
            return element
        except Exception as e:
            allure_info(log=f"{step_name}元素可能未找到, 报错原因: {traceback.format_exc()}")
            Logger().error(traceback.format_exc())

    def find_element(self, by, page_element, step_name):
        """
        用于查找元素
        :param page_element:
        :param by:
        :param step_name:
        :return:
        """
        try:

            r = self.driver.find_element(by, page_element)
            Logger.debug(f"元素定位成功：{page_element}")
            return r
        except Exception as e:
            allure_info(log=f"{step_name}元素可能未找到, 报错原因: {traceback.format_exc()}")
            Logger().error(traceback.format_exc())

    def get_url(self, step_name, url, picture_path=None):
        """

        :param step_name:
        :param url:
        :param picture_path:
        :return:
        """
        try:
            with allure.step(step_name):
                self.driver.get(url)
                if picture_path is not None:
                    allure_info(element=url, picture_path=self.screenshot(picture_path, step_name)
                                )
                else:
                    allure_info(url)
        except Exception as e:
            Logger().error(traceback.format_exc())

    def send(self, step_name, text, *loc, picture_path=None):
        """
        输入文本内容
        :param step_name:
        :param text: 输入的具体内容
        :param loc:
        :param picture_path:
        :return:
        """
        try:
            with allure.step(step_name):
                for i in loc:
                    r = self.wait_element(i[0], i[1], step_name)
                    r.send_keys(text)
                    if picture_path is not None:
                        self.screenshot(picture_path, step_name)
                        allure_info(element=i[1], text=text, picture_path=self.screenshot(picture_path, step_name))
                    else:
                        allure_info(element=i[1], text=text)
                    Logger.debug(f"成功输入: {text}")
        except Exception as e:
            Logger().error(traceback.format_exc())

    def click(self, step_name, *loc, picture_path=None):
        """
        单击
        :param step_name:
        :param loc:
        :param picture_path:
        :return:
        """
        try:
            with allure.step(step_name):
                for i in loc:
                    r = self.wait_element(i[0], i[1], step_name)
                    r.click()
                    if picture_path is not None:
                        self.screenshot(picture_path, step_name)
                        allure_info(element=i[1], picture_path=self.screenshot(picture_path, step_name))
                    else:
                        allure_info(element=i[1])
                    Logger.debug(f"点击按钮成功")
        except Exception as e:
            Logger().error(traceback.format_exc())

    def clear(self, step_name, *loc, picture_path=None):
        """
        清除文本内容
        :param step_name:
        :param loc:
        :param picture_path:
        :return:
        """
        try:
            with allure.step(step_name):
                for i in loc:
                    r = self.wait_element(i[0], i[1], step_name)
                    r.clear()
                    if picture_path is not None:
                        self.screenshot(picture_path, step_name)
                        allure_info(element=i[1], picture_path=self.screenshot(picture_path, step_name))
                    else:
                        allure_info(element=i[1])
                    Logger.debug(f"清除内容成功")
        except Exception as e:
            Logger().error(traceback.format_exc())

    def get_text(self, step_name, *loc, picture_path=None):
        """
        返回文本信息
        :return:
        """
        try:
            # return self.driver.find_element(*loc).text
            with allure.step(step_name):
                for i in loc:
                    r = self.wait_element(i[0], i[1], step_name)
                    # 元素定位到了，但没有获取到，可以考虑是否隐藏元素，使用此方法，但是IE不支持
                    text = r.get_attribute("textContent")
                    if picture_path is not None:
                        allure_info(element=i[1], picture_path=self.screenshot(picture_path, step_name))
                    else:
                        allure_info(element=i[1])
                    Logger.debug(f"成功获取文本: {text}")
                    return text
        except Exception as e:
            Logger().error(traceback.format_exc())

    def get_title(self):
        """

        :return: 返回标题
        """
        try:
            t = self.driver.title
            Logger.debug(f"成功获取标题: {t}")
            return t
        except Exception as e:
            Logger().error(traceback.format_exc())

    def select_option(self, element_name, text_name):
        """
            下拉框选择方法
        :param element_name:
        :param text_name:
        :return:
        """
        try:
            s1 = Select(element_name)
            s1.select_by_visible_text(text_name)
            Logger.debug("成功选择: {text_name}")
        except Exception as e:
            Logger().error(traceback.format_exc())

    def switch_win(self, index):
        """
            # 窗口切换方法
            # index为0代表第一个窗口，1代表第二个窗口
        :param index:
        :return:
        """
        try:
            # 获取所有窗口
            all_window = self.driver.window_handles
            # 切换窗口
            self.driver.switch_to_window(all_window[index])
            Logger.debug("切换窗口成功")
        except Exception as e:
            Logger().error(traceback.format_exc())

    '''====================================iframe处理===================================='''

    def switch_to_frame_page(self, *loc):
        """
        通过定位的元素进入frame
        :param driver:
        :param loc:
        :return:
        """

        try:
            self.driver.switch_to_frame(self.wait_element(*loc))
            Logger.debug("成功进入iframe")
        except Exception as e:
            Logger().error(traceback.format_exc())

    def switch_to_frame_index(self, index):
        """
        通过索引进入frame
        :param index: 0表示第一个frame
        :return:
        """
        try:
            self.driver.switch_to_frame(index)
            Logger.debug("成功进入iframe")
        except Exception as e:
            Logger().error(traceback.format_exc())

    def switch_to_frame_id(self, id):
        """
        通过id进入frame
        :param id:
        :return:
        """
        try:
            self.driver.switch_to_frame(id)
            Logger.debug("成功进入iframe")
        except Exception as e:
            Logger().error(traceback.format_exc())

    def switch_to_frame_name(self, name):
        """
        通过name进入frame
        :param name:
        :return:
        """
        try:
            self.driver.switch_to_frame(name)
            Logger.debug("成功进入iframe")
        except Exception as e:
            Logger().error(traceback.format_exc())

    def switch_to_default_content(self):
        """
        跳出最外层的页面
        :return:
        """
        try:
            self.driver.switch_to_default_content()
            Logger.debug("跳出最外层iframe")
        except Exception as e:
            Logger().error(traceback.format_exc())

    def switch_to_parent_frame(self):
        """
        跳出上一级
        :return:
        """
        try:
            self.driver.switch_to.parent_frame()
            Logger.debug("跳出上一级iframe")
        except Exception as e:
            Logger().error(traceback.format_exc())

    def back(self):
        """
        浏览器后退
        :return:
        """
        self.driver.back()
        Logger.debug("浏览器后退")

    def forward(self):
        """
        浏览器前进
        :return:
        """
        self.driver.forward()
        Logger.debug("浏览器前进")

    def refresh(self):
        """
        浏览器刷新
        :return:
        """
        self.driver.refresh()
        Logger.debug(f"浏览器刷新")

    def close(self):
        """
        有多个窗口的时候只是关闭当前的Windows窗口
        :return:
        """
        self.driver.close()
        Logger.debug("关闭当前窗口")

    def quit(self):
        """
        关闭浏览器，无论有多少个窗口都可以关闭
        :return:
        """
        self.driver.quit()
        Logger.debug("关闭浏览器")

    '''====================================键盘操作===================================='''

    def keyboard_operation(self, name, step_name, *loc):
        """

        :param driver:
        :param name: 具体的操作
        :param loc:
        :return:
        """
        try:
            for i in loc:
                serach = self.wait_element(i[0], i[1], step_name)

                if name == "删除":
                    serach.send_keys(Keys.BACK_SPACE)
                    Logger.debug("删除")
                elif name == "空格":
                    serach.send_keys(Keys.SPACE)
                    Logger.debug("输入空格")
                elif name == "回退":
                    serach.send_keys(Keys.ESCAPE)
                    Logger.debug("后退")
                elif name == "回车":
                    serach.send_keys(Keys.ENTER)
                    Logger.debug("回车")
                elif name == "全选":
                    serach.send_keys(Keys.CONTROL, 'a')
                    Logger.debug("全选")
                elif name == "复制":
                    serach.send_keys(Keys.CONTROL, 'c')
                    Logger.debug("复制")
                elif name == "剪贴":
                    serach.send_keys(Keys.CONTROL, 'x')
                    Logger.debug("剪贴")
                elif name == "粘贴":
                    serach.send_keys(Keys.CONTROL, 'v')
                    Logger.debug("粘贴")
        except Exception as e:
            Logger().error(traceback.format_exc())

    def js_querySelector(self, loc, value):
        """
        使用场景比如下拉框选择不是select标签，可以通过js强制注入内容。
        js接受css选择器定位的
        :param loc:
        :param value:
        :return:
        """
        try:
            js = f'document.querySelector("{loc}").value="{value}"'
            r = self.driver.execute_script(js)
            Logger.debug("下拉框强制注入内容成功")
            return r
        except Exception as e:
            Logger().error(traceback.format_exc())


if __name__ == '__main__':
    BasePage()
