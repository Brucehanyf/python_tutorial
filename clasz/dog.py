class Dog():
    ''' 小狗实体类  两侧双下划线 '''
    def __init__ (self,name, age):
        self.name = name
        self.age = range

    def sit (self):
        ''' 模拟小狗坐下动作'''
        print(self.name.title() + ' is now setting')

    def roll_over(self):
        ''' 模拟小狗打滚 '''
        print(self.name.title() + ' rolled over!')


dog = Dog('haha',6)
print("my dog's name is "+dog.name+" his age is " + str(dog.name))
dog.sit()
dog.roll_over()

erha = Dog('hashiqi',10)
erha.sit()
