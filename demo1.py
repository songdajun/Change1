import requests #导入请求包
from dbtools1 import query #跟dbtools文件连接，导入query
url = "http://127.0.0.1:8080/morning/getAllGoods" #获取所有结果
# requests的get方法
# 1.构造请求
res = requests.get(url) 
# print(res.text)  #.text所有的响应值
# 2.判断http状态码 res.status_code
assert res.status_code == 200
print("断言通过！")
# 3.判断接口返回的信息：获取到success，判断是不是true
a = res.json()
print(type(a)) #判断接口的类型  dict字典
assert res.json()["success"] == True  #条件为True
#4.连接查询数据库 (可选)
sql = "select * from tb_goods"
b = query(sql)
assert len(b) != 0
print(b)
print("接口测试通过！")