#################################################
#1.Роздрукувати всі парні числа менші 100 
#(написати два варіанти коду: один використовуючи цикл while, а інший з використанням циклу for).

# i = 0
# while i < 100:
#     if i % 2 == 0 :
#         print(i)
#     i= i + 1
    
# print(list(range(0,100,2)))

# for i in range (100):
#     if i % 2 == 0:
#         print(i)

################################################
#2.Роздрукувати всі непарні числа менші 100. 
#(написати два варіанти коду: один використовуючи оператор continue, а інший без цього оператора).

# i = 0 
# while i < 100:
#     if i % 2 != 0:
#         print(i)
#     i = i +1
    
# for item in range (100):
#     if item % 2 == 0 :
#         continue
#     print(item)

# print(list(range(1,100,2)))


###################################################
#3.Перевірити чи список містить непарні числа.
# (Підказка: використати оператор break)

# list = [1,3,4,6,7,9]
# for elements in list:
#     if elements % 2 != 0:
#         print("Містить:",elements)
#         break

# list = [1,3,4,6,7,9]
# for elements in list:
#     if elements % 2 != 0:
#         print("Містить:",elements)
#         continue


####################################################
#4.Створити список, який містить елементи цілочисельного типу, 
# потім за допомогою циклу перебору змінити тип даних елементів на числа з плаваючою крапкою. 
#(Підказка: використати вбудовану функцію float ()).

# my_list =[1,4,5,6,7,8,3,2]
# for element in my_list:
#     if type(element) is int:
#         print(float(element))

# my_list =[1,4,5,6,7,8,3,2]
# i = 0
# while i < len(my_list) :
#     my_list[i] = float(my_list[i])
#     i +=1
# print(my_list)

# list_number=[2,4,6,8,9,10]
# contain_odd=False
# for item in list_number:
#     if not item % 2 == 0: 
#         contain_odd=True
#         break
# if contain_odd:
#     print("There is odd number in the list")
# else: 
#     print("There is only even number in the list")


########################################################
#5.Вивести числа Фібоначі включно до введеного числа n, використовуючи цикли. 
#(Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)

# fib_1 = 0
# fib_2 = 1
# n = int(input("Input number:"))
# print(fib_1)
# print(fib_2)
# i = 2
# while i < n:
#     fib_sum = fib_2 + fib_1
#     fib_1 = fib_2
#     fib_2 = fib_sum
#     print(fib_sum)
#     i += 1 


######################################################
#6.Створити список, що складається з чотирьох елементів типу string. 
# Потім, за допомогою циклу for, вивести елементи по черзі на екран.

# my_new_list  = ['a', 'b', 'c', 'd']
# i = 0
# for my_new_list[i] in my_new_list:
#     print(my_new_list[i])
#     i +=1


########################################################
#7.  Змінити попередню програму так, щоб в кінці кожної букви елементів при виводі додавався певний символ, наприклад “#”. 
#(Підказка: цикл for може бути вкладений в інший цикл, а також  треба використати функцію print(“ ”, end=”%”)).

# my_new_list  = ['a', 'b', 'c', 'd']
# i = 0
# for my_new_list[i] in my_new_list:
#     print(my_new_list[i], end= '#\n')
#     i +=1


#######################################################
#8.Юзер вводить число з клавіатури, написати скріпт, який визначає чи це число просте чи складне.
# (DON`T WORK *CORRECT*!!!!!)

# a = int(input('Ведіть число:'))
# if a > 2 and a % 2 != 0 : 
#     y = a  
#     print(a,'- число просте!')
# elif a != y and a > 1 :
#     print(a,' - число складене!')


#######################################################
#9.Знайти максимальну цифру дійсного числа. 
#Дійсне число генеруємо випадковим чином за допомогою методу random() з модуля random
# (для цього підключаємо модуль random наступним чином from random import random)

# import random
# a = random.random()
# print(a)
# stra = str(a)
# maxa = -1
# y = len(stra)
# for i in range(y) :
#     if stra[i] == ".":
#         continue
#     elif maxa < int(stra[i]) :
#         maxa = int(stra[i])
# print(maxa)
#######################################################
#10.Визначити чи введене слово паліндром, тобто чи воно читається однаково зліва направо і навпаки.
#(DON`T WORK *CORRECT*!!!!!)

# a  = str(input('Please, input your word:'))
# n = len(a)
# i = 0
# if n == 4 and a[0] + a[1] + a[2] + a[3] == a[3] + a[2] + a[1] + a[0]:
#         print(a, 'is palindrome!')
# elif n == 5 and a[0] + a[1] + a[2] + a[3] + a[4] == a[4] + a[3] + a[2] + a[1] + a[0]:
#          print(a, 'is palindrome!')
# else:
#         print(a, "isn't palindrome!")

