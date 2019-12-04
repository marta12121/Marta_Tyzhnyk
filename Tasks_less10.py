#################################################
#1.Напишіть програму, яка пропонує користувачу ввести ціле число і визначає чи це число парне чи непарне, 
# # чи введені дані коректні.
# while True:
#     try:
#         a = int(input('Input integer number:'))
#         if a % 2 ==0:
#             print(a, ' - even number')
#         else:
#             print(a, ' - odd number')
#     except ValueError:
#         print('Please, check your entering a number and input the number again:')
    
#################################################
#2.Напишіть програму, яка пропонує користувачу ввести свій вік, 
# після чого виводить повідомлення про те чи вік є парним чи непарним числом. 
# Необхідно передбачити можливість введення від’ємного числа, в цьому випадку згенерувати власну виняткову ситуацію. 
# Головний код має викликати функцію, яка обробляє введену інформацію. 


# class SpecialError(Exception):
#     def __init__(self, data):
#         self.data = data
#     def __str__(self):
#         return repr(self.data)

# def vuznachennia_parnosti(age):
#     # age = int(input('Input your age:'))
#     if age % 2 ==0:
#         return(age, ' - even number')
#     else:
#         return(age, ' - odd number')

# while True:
#     try:
#         age = int(input('Input your age:'))
#         if age < 0:
#             raise SpecialError('Your age can`t be as negative number!')
#         elif age > 0:
#             print(vuznachennia_parnosti(age))
#     except SpecialError as error:
#         print("Please input positive number:", error.data)

# while True:
#     try:
#         age = int(input('Input your age:'))
#         if age < 0:
#             raise ValueError('Your age can`t be as negative number! Please input positive number:')
#         elif age % 2 == 0 :
#             print(age, ' - even number')
#         else:
#             print(age, ' - odd number')
#     except ValueError as error:
#         print(error)

#################################################
#3.Напишіть програму для обчислення частки двох чисел, які вводяться користувачем послідовно через кому, 
# передбачити випадок ділення на нуль, випадки синтаксичних помилок та випадки інших виняткових ситуацій. 
# Використати блоки else та finaly.

# def vuznachennia_chastku(a,b):
#     c = a / b 
#     return c
# while True:
#     try:
#         a  = int(input('Input integer number a :'))
#         b = int(input('Input integer number b :'))
#         if b == 0 :
#             raise ZeroDivisionError("U can`t divide by zero! Please input new numbers! ")
#         else:
#             print(vuznachennia_chastku(a,b))
#     except ZeroDivisionError as error:
#         print(error)

#4.  Написати  програму, яка аналізує введене число та в залежності від числа видає день тижня, 
# який відповідає цьому числу (1 це Понеділок, 2 це Вівторок і т.д.) . 
# Врахувати випадки введення чисел від 8 і більше, а також випадки введення не числових даних.

class SpecialError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)

def determine_day_of_week():
    week = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}
    return week.get(key)


while True:
    try:
        key = int(input('Please inpunt the number 1-7:'))
        if key > 7 :
            raise SpecialError('Please enter only numbers:1,2,3,4,5,6,7 : ')
        elif key == '':
            raise ValueError('Please enter only numbers:1,2,3,4,5,6,7 NO symbols: ')
        else:
            print(determine_day_of_week())
    except SpecialError as error2:
        print('Please enter only numbers:1,2,3,4,5,6,7,8! NO symbols: ', error2.data)
    except ValueError as error3:
        print(error3)