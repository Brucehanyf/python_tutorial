# 模拟掷骰子
from random import randint
class Die():
    def __init__(self, num_sides = 6):
        """ 骰子默认6面 """
        self.num_sides = num_sides

    def roll(self):
        """ 返回一个介于1和骰子面数之间的随机数"""
        return randint(1,self.num_sides)