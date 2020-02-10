# 姓名测试类
def get_format_name(first, last,middle=''):
    """ 获取全名 """
    if middle:
        full_name = first +' '+ middle +' '+last
    else:
        full_name = first +' '+ last
    return full_name.title()