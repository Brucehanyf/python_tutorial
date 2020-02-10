class Car():
    '''  汽车类 '''
    def __init__(self, make, model, year):
        '''初始化汽车属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descrptive_name (self):
        local_name = str(self.year) + ' ' + self.make +' '+ self.model
        return local_name.title()
    def read_odometer_reading(self):
        '''打印汽车里程'''
        print("This car has " + str(self.odometer_reading) + " miles on it ")
    def update_odometer_reading(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(" you can't roll back an oldmeter")

# my_car = Car('auDi', 'AudiA6',2029)
# print(my_car.get_descrptive_name())

# 给属性指定默认值 初始化函数则无需传递设置
# 修改属性值
# my_car.year = 2020
# print(my_car.get_descrptive_name())
# my_car.update_odometer_reading(10)
# print(my_car.get_descrptive_name())
# my_car.update_odometer_reading(9)
# print(my_car.get_descrptive_name())

