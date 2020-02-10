# 写入空文件
filename = 'write.txt'
with open(filename,'w') as file_object:
    file_object.write("I love python!\n")
    file_object.write("I love java!\n")
    file_object.write("I love Go!\n")

# 附加到指定指定文件
with open(filename,'a') as file_object:
    file_object.write('because coding is interesting')