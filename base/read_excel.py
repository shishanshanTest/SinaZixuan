# !/use/bin/env python
# -*-conding:utf-8-*-

#author:shanshan

import xlrd
from base.get_path import *
from data.variable import *

class excel(object):
    "对应excel表格中的表头"
    ID = 0
    title = 1
    request_path = 2
    data = 3


    def get_sheet(self):
        "获取sheet实例"
        excel = xlrd.open_workbook(path('data','zixuanData.xls'))
        sheet = excel.sheet_by_index(0)
        return sheet

    def get_nrows(self):
        '''获取excel中有效的行数'''
        return self.get_sheet().nrows

    def get_ID(self,row):
        """
        获取excel中每一行的ID值
        :param row: 行的值
        :return:
        """
        return self.get_sheet().cell_value(rowx=row,colx=0)

    def get_title(self,row):
        return self.get_sheet().cell_value(rowx=row,colx=1)

    def get_url(self,row):
        return zixuan_IP()+self.get_sheet().cell_value(rowx=row,colx=2)

    def get_data(self,row):
        return self.get_sheet().cell_value(rowx=row,colx=3)

excel = excel()
