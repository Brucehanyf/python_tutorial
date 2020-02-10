### 字符串相关语法

print('hello,world')
message = "hello,message"
print(message)
message = "hello world"
print(message)

# 变量名不能以数字开头， 中间不能包含空格，其中可以包含下划线

# 字符串字母首字母大写 字符串大写 字符串小写
name = "hello bruce"
print(name.title())
print(name.upper())
print(name.lower())

# 合并字符串
first_name = "Bruce"
last_name = "Han"
full_name = first_name + " " + last_name
print(full_name.title()+"!")

# 使用制表符或者换行符来添加空白
#  制表符 \t  换行符 \n
print("language java \n\tpython js ")

# 删除空白
# rstrip() 删除右侧空格
# lstrip() 删除左侧空格
# strip() 删除两侧空格
favorite_language = " python "
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)
favorite_language = favorite_language.lstrip()
print(favorite_language)

# 使用str() 避免类型错误
age = 23
message = "hello Bruce "+ str(age) + "rd birthday!";
print(message)


















