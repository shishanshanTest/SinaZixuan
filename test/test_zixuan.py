# !/use/bin/env python
# -*-conding:utf-8-*-

#author:shanshan

import requests,unittest,random
from base.excel_json import *
from base.get_path import *
from base.read_excel import *

# class zixuan(unittest.TestCase):
#     yincang_type = 'us'
#
#     def setUp(self):
#         pass
#
#     def tearDown(self):
#         pass
#
#     def assert_code(self,r):
#         self.assertEqual(r.status_code, 200)
#         self.assertEqual(r.json()['result']['status']['code'], 0)
#
#
#     def test_001_chakanzixuanfenzu(self):
#         """查看自选分组接口"""
#         r = requests.get(url=excel.get_url(1),
#                          params=read_zixuanJSON_data(1),
#                          headers=zixuan_header())
#         self.assert_code(r)
#
#     def test_002_chuangjianzixuanfenzu(self):
#         """创建自选分组接口"""
#         r = requests.get(url=excel.get_url(2),
#                          params=read_zixuanJSON_data(2),
#                          headers=zixuan_header())
#         global pid, order
#         pid = r.json()['result']['data']['pid']
#         order = r.json()['result']['data']['order']
#         print(pid)
#         self.assert_code(r)
#
#     def test_003_xiugaizixuanname(self):
#         """更改自选分组名称接口"""
#         params = read_zixuanJSON_data(3)
#         params['pid'] = pid#动态参数pid
#         r = requests.get(url=excel.get_url(3),
#                          params=params,
#                          headers=zixuan_header())
#         self.assert_code(r)

    #
    # def test_004_tiaozhengzixuanfenzushuxun(self):
    #     """随即调整自选分组顺序接口"""
    #     jorder = ['all','cn','hk','us','ft','fund','wh',pid]#放在一个列表中
    #     random.shuffle(jorder)#使用random.shuffle生成随机的列表
    #     list_str = ','.join(jorder)#再将列表转化为字符串
    #     params = read_zixuanJSON_data(4)
    #     params['jorder'] = list_str
    #     r = requests.get(url=excel.get_url(4),
    #                      params=params,
    #                      headers=zixuan_header())
    #     self.assert_code(r)
    #
    #
    #
    # def test_005_yincangzixuanfenzu(self):
    #     """隐藏自选股分组接口"""
    #     params = read_zixuanJSON_data(5)
    #     #typelist_index = random.randint(0,5)
    #     #listype = ['cn','hk','us','ft','fund','wh']
    #     params['type'] =self.yincang_type
    #     r = requests.get(url=excel.get_url(5),
    #                      params=params,
    #                      headers=zixuan_header())
    #     self.assert_code(r)
    #
    # def test_006_yincanggongnengyanzheng(self):
    #     """验证隐藏功能是否成功"""
    #     r = requests.get(url=excel.get_url(1),
    #                      params=read_zixuanJSON_data(1),
    #                      headers=zixuan_header())
    #     for i in range(0,7):
    #         if r.json()['result']['data'][i]['type'] == self.yincang_type:
    #             self.assertEqual(r.json()['result']['data'][i]['status'],1)
    #
    #
    # def test_007_shanchuzixuanfenzu(self):
    #     """删除自选分组接口"""
    #     params = read_zixuanJSON_data(6)
    #     params['pid'] = pid
    #     r = requests.get(url=excel.get_url(6),
    #                      params=params,
    #                      headers=zixuan_header())
    #     self.assert_code(r)




# if __name__ == '__main__':
#     unittest.main(verbosity=2)

r = requests.get(url=excel.get_url(2),
                params=read_zixuanJSON_data(2),
                headers=zixuan_header())

pid = r.json()['result']['data']['pid']
print(json.dumps(r.json(),indent=4,ensure_ascii=False))

params = read_zixuanJSON_data(3)
params['pid'] = pid#动态参数pid
r = requests.get(url=excel.get_url(3),
                params=params,
                headers=zixuan_header())
print(json.dumps(r.json(),indent=4,ensure_ascii=False))
