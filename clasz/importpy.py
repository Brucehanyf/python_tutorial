# 导入类
# 导入单个类
from clasz.car import Car
my_new_car = Car('bmw','X',2020)
print(my_new_car.get_descrptive_name())

# 在一个模块中存储多个类
from  clasz.electric_car import  Car,ElectricCar
elecar = ElectricCar('BYD','Q',2019)
print(elecar.get_descrptive_name())

#  导入模块中的所有类
from clasz.electric_car import *

# 在一个模块中导入另一个模块