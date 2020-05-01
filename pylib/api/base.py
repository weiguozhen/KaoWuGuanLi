#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import json

import requests


class CommonRequests:
    def __init__(self):
        self.session = requests.Session()

    def request(self, method, url, data=None, is_json=False, **kwargs):
        """
        发送请求
        :param method: POST、GET、DELETE、PUT
        :param url: 请求路径
        :param data: 请求参数
        :param is_json: 入参是否为json格式
        :param kwargs: 请求头等其他的入参
        :return: 接口返回
        """
        method = method.upper()
        if isinstance(data, str):  # 对传入的参数进行简单处理
            try:
                data = json.loads(data)
            except Exception as e:
                print("异常为{}".format(e))
                data = eval(data)
        if method == "GET":
            response = self.session.request(method=method, url=url, params=data, **kwargs)
        elif method == "POST":
            if is_json:  # 请求参数是json格式
                response = self.session.request(method=method, url=url, json=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, data=data, **kwargs)
        elif method == "DELETE":
            response = self.session.request(method=method, url=url, data=data, **kwargs)
        elif method == "PUT":
            response = self.session.request(method=method, url=url, data=data, **kwargs)
        else:
            response = None
        return response

    def close(self):
        self.session.close()
