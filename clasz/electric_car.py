# 形参是可选的 没有值默认给70
class Battery():
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size
    def describe_battery(self):
        return str(self.battery_size)

'''  汽车类继承类 '''
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
    def fill_gas_tank(self):
        print('my car is filling gas')

class ElectricCar(Car):
    ''' 继承类 '''
    def __init__(self, make, model, year):
        '''初始化父类属性'''
        super().__init__(make, model, year)
        # self.battery = 70
        self.battery = Battery()
    def describe_battery(self):
         print('This car has a '+str(self.battery.describe_battery())+'-kWh battery')
    '''重写父类方法'''
    def fill_gas_tank(self):
         print('electricCar do not need gas !!!')

my_electricCar = ElectricCar('Audi','A6',2020)
print(my_electricCar.get_descrptive_name())
print(my_electricCar.describe_battery())
my_electricCar.fill_gas_tank()

# 调用super().__init__(make, model, year)方法 无需传递self参数
# 参数上下一定要对齐

print(my_electricCar.describe_battery())
