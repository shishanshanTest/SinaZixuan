# !/use/bin/env python
# -*-conding:utf-8-*-

#author:shanshan
import random

# jorder = ['all','cn','hk','us','ft','fund','wh','pid']
# random.shuffle(jorder)
# print(jorder)
# list_str = ','.join(jorder)
# print(list_str)

typelist_index = random.randint(0,6)
listype = ['cn','hk','us','ft','fund','wh']
print(listype[typelist_index])

