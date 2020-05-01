#!/usr/bin/env python 
# -*- coding: utf-8 -*-


import re


def handel_re(data):
    print(data)
    pattern = '(.*?功).*?(\d{1,10}).*?(\d{1,15})'
    return re.findall(pattern, data, re.S)[0]


def handel_teacher_re(data):
    print(data)
    pattern = '(.*?功).*?(\d{1,10})'
    print(re.findall(pattern, data, re.S))
    return re.findall(pattern, data, re.S)[0]


if __name__ == '__main__':
    print(handel_re('添加成功 班级ID为：387848 班级邀请码为：3878488250966'))
