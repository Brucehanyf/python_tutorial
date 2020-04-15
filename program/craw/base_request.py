# request模块具体使用方法
import requests
# # 开源地址：https://github.com/kennethreitz/requests
# # demo :https://www.cnblogs.com/coder-lzh/p/9843197.html
# kw = {'wd':'长城'}
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
# }
# resppnse = requests.get('http://www.baidu.com/',params=kw, headers=headers,verify=False)
# print(resppnse)
# print(resppnse.text)
# print(resppnse.content)
# print(resppnse.url)

from itertools import groupby
help(groupby())