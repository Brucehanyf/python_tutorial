# 读取圆周率
# 读取整个文件
# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents)

# file_path = 'pi_digits.txt';
# \f要转义
# 按行读取
file_path = "D:\PycharmProjects\practise\\file_and_exception\pi_digits.txt";
# with open(file_path) as file_object:
#     for line in file_object:
#         print(line)

# file_object.readlines()
# with open(file_path) as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line)

# 使用文件中的内容
with open(file_path) as file_object:
    lines = file_object.readlines()
result = '';
for line in lines:
    result += line.strip()
print(result)
print(result[:10]+'......')
print(len(result))
birthday = input('请输入您的生日')
if birthday in result:
    print("your birthday appears in pai digits")
else:
    print("your birthday does not appears in pai digits")



