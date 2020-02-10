# name_function_test测试类创建
# 导入unittest
# 创建测试类
# 编写测试方法
# 断言判断结果
import unittest
from test.name_function import get_format_name

# 断言的方法
## assertEqual(a,b) 核实a==b
## assertNotEqual(a,b) 核实a!=b
## assertTrue(x) 核实x为True
## assertFalse(x) 核实x为False
## assertIn(item,list) 核实item在list中
## assertNotIn(item,list)核实item不在list中

class NamesTestCase(unittest.TestCase):
    ''' 测试 name_function.py '''

    def test_first_last_name(self):
        ''' 测试 Bruce Han这样的用户名么 '''
        format_name = get_format_name('bruce','han')
        self.assertEqual(format_name,'Bruce Han')


    def test_first_middle_last_name(self):
        ''' 测试 Bruce Han这样的用户名么 '''
        format_name = get_format_name('bruce','han','middle')
        self.assertEqual(format_name,'Bruce Middle Han')
