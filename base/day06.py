# 用户输入和While 循环 提示超过一行用变量拼接 pro = '123' pro += '456'
# name = input("please enter your name:")
# print ('hello '+ name + "!")

# 如何输入非法字符怎么处理 空怎么处理
# count = 3
# while(count >= 0):
#     height = input("please tell me how old you are")
#     height = int(height)
#     # count -= 1
#     if height >= 18 and height <= 60:
#         print ('you are an audlt!')
#     elif height > 60:
#         print ('you are an older!')
#     else:
#         print ('you are a child')

# order = ''
# while(order != 'exit'):
#     order = input('请输入指令,按 exit退出！')
#     print (order)

# 使用break退出循环 开关方式退出循环
# while(True):
#     order = input('请输入指令，按exit 退出！')
#     print (order)
#     if order == 'exit':
#         break;

# 使用continue放弃本次continue后边执行的代码
current_number = 0
while(current_number <10):
    current_number += 1
    if(current_number % 2 == 0):
        continue
    print (current_number)

# 在列表红移动元素

unconfirm_users = ['alice','brian','candace']
confirm_users = []
while unconfirm_users:
    current_user = unconfirm_users.pop()
    print ('verifying user.............'+ current_user.title())
    confirm_users.append(current_user)
print ("The follwing users have been confirmed:")
for user in confirm_users:
    print (user)

# 循环删除列表中的重复数据

pets = ['dog','dog','cat','fish','rabbit','goldfish']
print ('pets: before: ' + str(pets))
while 'cat' in pets:
    pets.remove('cat')
print ('pets: after: '+ str(pets))
