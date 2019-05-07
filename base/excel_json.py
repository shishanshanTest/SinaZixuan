# !/use/bin/env python
# -*-conding:utf-8-*-

#author:shanshan

from base.read_excel import *
from base.get_path import *
import json


"""将excel与json文件进行关联,关联的好处在于看起来简单方便便于维护,也不用转化数据格式"""
try:
    def read_zixuanJSON_data(row):
        with open(path(mulu='data', file='zixuanJSON_data'), 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            return json_data[excel.get_data(row=row)]
except Exception as e:
    print("获取excel中data数据错误{}".format(e.args))


