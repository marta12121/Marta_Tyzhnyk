# #example:
# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]

#     def inputSides(self):
#         self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])
    
# class Triangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self,3)  #super().__init__(3) 

#     def findArea(self):
#         a, b, c = self.sides
#         s = (a + b + c) / 2
#         area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#         print('The area of the triangle is %0.2f' %area)
# t = Triangle()
# t.inputSides()
# t.dispSides()
# t.findArea()


#1.  Створити клас машина з атрибутами name,  make, model та методами start та stop, 
# які виводять інформацію про те що автомобіль стартував чи зупинився відповідно.

# class Car:
#     def __init__(self, name, make, model):
#         self.name = name
#         self.make = make
#         self.model = model
#     def start(self):
#         print('The car {} is starting '.format(self.name))
#     def stop(self):
#         print('The car {} sttopped'.format(self.name))

# tesla = Car('Tesla', 'v8', 'n8')
# tesla.start()
# audi = Car('Audi', 'Q8', 'm8')
# audi.start()
# audi.stop()

########################################################
#2.Створити клас особа,  в якому конструктор встановлює ім’я, а метод info виводить повідомлення 
# “Hello, my name is {ім’я конкретного екземпляра класу}”, а також створити клас автомобіль,  
# в якому конструктор встановлює ім’я, а метод move виводить повідомлення {ім’я конкретного екземпляра класу}  
# moves at the speed {speed(цей параметр метод move отримує як вхідний)} km / h

# class Human:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         print('Hello, my name is {}.'.format(self.name))

# class Car2:
#     def __init__(self, model, speed):
#         self.model = model
#         self.speed = speed
#     def move(self):
#         print('{} moves at the speed {} km / h.'.format(self.model, self.speed))

# Mark = Human('Mark')
# Mark.info()
# Audi = Car2('Audi',input("Please input the speed:"))
# Audi.move()

########################################################
#3.Створити клас особа,  в якому конструктор встановлює ім’я, вік. 
# Використати в цьому класі геттери та сеттери(вичитує та встановлює), а також створити метод info, який виводить
# інформацію про ім’я та вік особи. 
# А тоді створити клас працівник,який наслідується від класу особи і містить метод details, 
# який на вхід отримує параметр про компанію,в якій працює працівник і цей метод виводить інформацію про те, 
# що працівник з таким то іменем працює в такій то компанії.
# class Human:
#     def __init__(self, name, age):
#         self.__set_name(name)
#         self.__set_age(age)

#     def __get_name(self):
#         return self.__name
   
#     def __set_name(self, name):
#         self.__name  = name

#     def __get_age(self):
#         return self.__age
   
#     def __set_age(self, age):
#         if age <= 0 :
#             print('Your age can`t be as negative number!!! Please check your inputting and enter age again:')
#         else:
#             self.__age  = age
#     name = property(__get_name, __set_name)
#     age = property(__get_age, __set_age)

#     def info2(self):
#         print('Hello! My name`s {}.'.format(self.__name))
#         print('And I`m {} years old.'.format(self.__age))


# class Employee(Human):
#     def __init__(self, name, age):
#         super().__init__(name, age)
        
#     def details(self,company) :
#         self.company = company
#         print('Employee {} works in {}.'.format(self.name, self.company))

# # Mark = Human(input('Please input your name:'), int(input('Please input your age:')))
# SoftServe.info2()
# SoftServe = Employee(input('Please input your name:', int(input('Please input your age:')))
# SoftServe.details(input('Please input company`s name:'))




########################################################
#4.Створити батьківський клас Figure з методами init: ініціалізується колір,                                                                                          get_color: повертає колір фігури,                                                                                          info: надає інформацію про фігуру та колір,  
# від якого наслідуються такі класи як Rectangle, Square, які мають інформацію про ширину, 
# висоту фігури, метод square, який знаходить площу фігури.
class Figure:
    def __init__(self, colour):
        self.colour = colour
class Rectangle(Figure):
    def __init__(self, width, height):
        # super(Figure, self).__init__()
        self.width = width
        self.height = height
class Square(Rectangle):
    def find_square(self, width, height):
        return self.width * self.height
        