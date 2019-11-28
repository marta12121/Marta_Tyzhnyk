#######################################################
#1.Створити список цілих чисел, які вводяться з терміналу та визначити 
# серед них максимальне та мінімальне число.

# count_my_list = input("Input count of my_list : ")
# my_list = []
# for elements in range(int(count_my_list)):
#     my_list.append(int(input("Enter numbers: ")))
# print("my_list:", my_list)    
# print("MAXIMUM NUMBER OF my_list: ", max(my_list))
# print("MINIMUM NUMBER OF my_list: ", min(my_list))

# count_my_list = int(input("Input count of my_list : "))
# my_list = [input("Enter numbers: ") for elements in range(count_my_list)]
# print("my_list:", my_list)    
# print("MAXIMUM NUMBER OF my_list: ", max(my_list))
# print("MINIMUM NUMBER OF my_list: ", min(my_list))


#######################################################
# 2.  В інтервалі від 1 до 10 визначити числа 
# •  парні, які діляться на 2,
# •  непарні, які діляться на 3, 
# •  числа, які не діляться на 2 та 3.

# list_x = list(range(1,11))
# print(list_x)
# list_y = []
# i = 0
# for list_x[i] in list_x :
#     if list_x[i] % 2 == 0 :
#         list_y.append(list_x[i])
#         i = i+1
# print('ПАРНІ ЧИСЛА , ЯКІ ДІЛЯТЬСЯ НА 2:', list_y)

# list_x = list(range(1,11))
# i = 0
# list_y = [list_x for list_x[i] in list_x if list_x[i]% 2 == 0 ] 
# print(list_y)

# list_z = list(range(1,11))
# list_w = []
# i = 0
# for list_z[i] in list_z :
#     if list_z[i] % 3 == 0 :
#         list_w.append(list_z[i])
#         i = i+1
# print('НЕПАРНІ ЧИСЛА , ЯКІ ДІЛЯТЬСЯ НА 3: ', list_w)

# list_a = list(range(1,11))
# list_b = []
# i = 0
# for list_a[i] in list_a :
#     if list_a[i] % 2 != 0 :
#         list_b.append(list_a[i])
#     elif list_a[i] % 3 != 0 :
#         list_b.append(list_a[i])
#         i = i+1
# print('ЧИСЛА, ЯКІ НЕ ДІЛЯТЬСЯ НА 2 ТА 3: ',list_b)
    
#######################################################
#3.Написати програму, яка обчислює факторіал числа, яке користувач вводить.
# (не використовувати рекурсивного виклику функції)
# n = int(input("ВВЕДІТЬ ЧИСЛО ДЛЯ ВИЗНАЧЕННЯ ФАКТОРІАЛУ:"))
# factorial = 1
# for i in range(2, n+1):
#     factorial *=i
# print(factorial)
#######################################################

#4.Напишіть скрипт, який перевіряє логін, який вводить користувач. 
# Якщо логін вірний (First), то привітайте користувача. 
# Якщо ні, то виведіть повідомлення про помилку.(використайте цикл while)

# login = str(input("Please input login: "))
# while login != str("First"):
#     print("PLEASE CHECK YOUR LOGIN!")
#     login = str(input("Please input login again: "))
# if login == str("First"):
#     print("CONGRATULATION!")

#######################################################
# 5.Перший випадок. 
# Написати програму, яка буде зчитувати числа поки не зустріне від’ємне число. 
# При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).

# new_list= []
# i = 1
# while i > 0 :
#     i = int(input("Ведіть число:"))
#     new_list.append(i)
#     if (i == 0) or (i < 0):
#         break
#     print(new_list)


#######################################################
# 6.Другий випадок.На початку на вхід подається кількість елементів послідовності, а потім самі елементи.
# При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).

# count_new_list = int(input('Введіть кількість елементів послідовності : '))

# new_list = []
# for i in range(int(count_new_list)):
#     i = int(input("Ведіть число:"))
#     new_list.append(i)
#     if (i == 0) or (i < 0):
#         break
#     print(new_list)

    


#######################################################
# 7.  Знайти прості числа від 10 до 30, а всі решта чисел представити у вигляді добутку чисел 
# (Hаприклад:         10 equals 2 * 5
#                     11 is a prime number
#                     12 equals 2 * 6
#                     13 is a prime number
#                     14 equals 2 * 7
#                      ………………….)
 
for number in range(10, 31):
    for i in (2, number):
        if number % i == 0:
            num = int(number/i)
            print(number, 'equals',num, '*',i )
        else:
            print(number, '- is a prime number.')
#######################################################
# 8.  Відсортувати слова в реченні в порядку їх довжини (використати List Comprehensions)
# x = "In python you seldom need to convert a string to a list because strings and lists are very similar"
# y = x.split()
# print(' '.join(sorted (y, key = len)))


