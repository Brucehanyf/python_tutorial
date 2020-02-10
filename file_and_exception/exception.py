# 异常处理 ZeroDivisionError: division by zero
# print(5/0)
# try except代码块
try:
    print(5 / 0)
except ZeroDivisionError:
    print('you can\'t divide by zero')


# 给定连个两个数字给出相除结果
# print("please give two number i will give you a result......\n")
# print('Q will exit......\n')
# while True:
#     first_number = input('please enter first number')
#     if first_number == 'Q':
#         break
#     second_number = input('please enter second number')
#     if second_number == 'Q':
#         break;
#     answer = int(first_number)/int(second_number)
#     print(answer)

# 处理fileNotFoundError
# filename = "write.txt"
# try:
#     with open(filename) as file_object:
#         contents = file_object.read()
# except FileNotFoundError:
#     print('sorry! the file '+filename+' does not exit!')
# else:
#     words = contents.split()
#     print(len(words))

# 使用多个文件
def count_word(filename):
    """计算一个文件大致包含多少个文件"""
    try:
        with open(filename, 'r', encoding='UTF-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print('失败时一声不吭')
        pass
        # msg = 'Sorry the file' + filename + ' is not exit'
        # print(msg)
    else:
        # 计算文件大致含有多少多少个单词
        words = contents.split()
        num_words = len(words)
        print(num_words)

file = 'write.txt'
count_word(file)

filenames = ['write.txt', 'fsfsdf.txt', 'write_message.py', 'exception.py']
for filename in filenames:
    count_word(filename)
