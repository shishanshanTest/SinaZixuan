# !/use/bin/env python
# -*-conding:utf-8-*-

#author:shanshan

import os

def path(mulu,file):
    """
    获取该项目下的文件具体路径
    :param mulu: 该项目下的目录名称
    :param file: 目录下的文件名称
    :return:
    """
    PM_PATH = os.path.dirname(os.path.dirname(__file__))#该项目的路径
    return os.path.join(PM_PATH,mulu,file)


