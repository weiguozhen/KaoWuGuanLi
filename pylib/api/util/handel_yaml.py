#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import yaml


def conf_read(conf_file='/Users/wgz/Desktop/考务管理系统/pylib/api/conf/conf.yaml'):
    with open(conf_file) as f:
        file = f.read()
        conf = yaml.load(file, Loader=yaml.FullLoader)
        return conf


if __name__ == '__main__':
    # print(conf_read())
    conf = conf_read()
    print(conf[conf['test_env']]['vcode'])
    # print(conf_read()[conf_read()['test_env']]['classUrl'])
