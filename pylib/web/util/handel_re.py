#!/usr/bin/env python 
# -*- coding: utf-8 -*-


import re


def remove_count(text):
    pattern = '(.*班).*?'
    return re.findall(pattern, text)[0]


if __name__ == '__main__':
    print(remove_count('九年级3班2fdf'))
