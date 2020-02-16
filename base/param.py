# 参数相关语法
def param (param="123456"):
    print("123123")

# 函数的收集参数和分配参数用法（‘*’ 和 ‘**’）
# arg传递的是实参， kvargs传递的是带key值的参数
# 函数参数带*的话，将会收集非关键字的参数到一个元组中；
# 函数参数带**的话，将会收集关键字参数到一个字典中；
# 参数arg、*args、必须位于**kwargs之前
# 指定参数不会分配和收集参数

def param_check(*args,value = 'param', **kvargs):
    print(value)
    print(args)
    print("args--------start")
    for arg in args:
        print(arg)
    print("args--------end")

    print(kvargs)
    print("kvargs--------start")
    for k, v in kvargs.items():
        print("key: " + str(k) + " value:" + str(v))
    print("kvargs--------end")


# **参数需要指定key值
param_check(1, 2, 3,value="1024",k=5,v=6,a=7,b=8)
