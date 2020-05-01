#!/usr/bin/env python 
# -*- coding: utf-8 -*-


import yaml


class HandelYaml:
    def conf_read(self, conf_file='/Users/wgz/Desktop/考务管理系统/pylib/app/conf/locator.yaml'):
        with open(conf_file) as f:
            file = f.read()
            conf = yaml.load(file, Loader=yaml.FullLoader)
            return conf

    def get_server(self, conf_file='/Users/wgz/Desktop/考务管理系统/pylib/app/conf/mobile.yaml'):
        read = self.conf_read(conf_file)
        return read[read['server']]


if __name__ == '__main__':
    # print(conf_read())
    a = HandelYaml()
    print(a.conf_read('../conf/mobile.yaml')['wait']['wait'])
    # print(a.get_value('TeacherLogin1','password'))
    # print(a.get_server())
    # print(conf[conf['test_env']]['vcode'])
    # print(conf_read()[conf_read()['test_env']]['classUrl'])
