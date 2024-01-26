#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : api_auto_test
# @File    : codes_utils.py
# @Time    : 2023-01-31 11:55:36
# @User    : cx2259
# @Author  : chen xin
# @Description :
import base64


def b64_encode(text):
    """
    对文本使用base64编码
    :param text:
    :return:
    """
    encoded_data = base64.b64encode(bytes(text, "utf-8"))  # bytes将str转换为字节
    return encoded_data


def b64_decode(text):
    """
    对文本使用base64解码
    :param text:
    :return:
    """
    decoded_data = base64.b64decode(text)
    return decoded_data


if __name__ == '__main__':
    a = b64_encode("test")
    b = b64_decode("dGVzdA==")
    print(a)
    print(b)
