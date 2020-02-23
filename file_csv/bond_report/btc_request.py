import requests
import json

# w 直接写入文件
# Wb写入字节码
# json.load 和loads() 区别  load要结合with open使用  loads()是直接用的
# json.load() # 将一个存储在文件中的json对象（str）转化为相对应的python对象
# json.loads() # 将一个json对象（str）转化为相对应的python对象
# json.dump() # 将python的对象转化为对应的json对象（str),并存放在文件中
# json.dumps() # 将python的对象转化为对应的json对象（str)

json_url = "http://www.kuaidi100.com/query?type=yuantong&postid=11111111111"
req = requests.get(json_url)
print(req.text)
# 将数据写入文件
with open('express_search.json','w',encoding='utf-8') as file_object:
    file_object.write(req.text)


