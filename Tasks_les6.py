#################################################
#1.Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел. 
def find_arithmetic_mean( *args):
    """ This function can find 
    arithmetic_mean."""
    sum = 0
    for value in args:
        sum += value
    return sum/len(args)
    
print("ARITHMETIC MEAN : ", find_arithmetic_mean(3,5,9,4,5))

#################################################
# 2.Написати функцію, яка повертає абсолютне значення числа
import math
def find_absolute_value(x):
    """ This function can find absolute_value 
    of the number."""
    return math.fabs(x)

print('ABSOLUTE VALUE OF NUMBER:', find_absolute_value(-2))

#################################################
#3.Написати функцію, яка знаходить максимальне число з двох чисел, а також в функції 
# використати рядки документації DocStrings.
def find_max_numb(x,y):
    """ This function can find max number 
    of two numbers."""
    if x > y:
        print(x, " - is max number.")
        return x 
    else:
        print(y, " - is max number.")
        return y
print('MAX NUMBER OF TWO NUMBERS: ', find_max_numb(3,4))
#################################################
#4. Написати програму, яка обчислює площу прямокутника, трикутника та кола 
#(написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)
import math

def find_square_pr(a,b):
    """ This function can find square
    of priamokutnuk"""
    return a * b
print("SQUARE OF PRIAMOKUTNUK: ", find_square_pr(2,6))

def find_square_tric(a, b, c):
    """ This function can find square
    of tricutnuk"""
    p = (a+b+c)/2
    s = math.sqrt(p * (p-a)*(p-b)*(p-c))
    return s
print("SQUARE OF TRICUTNUK: ", find_square_tric(3,4,5))

def find_square_kolo(r):
    """ This function can find square
    of kolo"""
    s = math.pi * r **2
    return s 
print("SQUARE OF KOLO: ", find_square_kolo(5))

#################################################
#5.Написати функцію, яка обчислює суму цифр введеного числа.

x = int(input("Please input your numeric: "))
my_list = list(map(int, str(x)))
print(my_list)
def find_sum( *my_list):
    """ This function can find sum 
    of numeric"""
    # a = len(my_list)- 2
    # i  = 0
    # suma=0
    # for i in my_list  :
    #     suma  +=  my_list[i]
    #     i+=1
    # return suma
    return sum(my_list)
print("SUM NUMBERS OF NUMERIC:", sum(my_list))

#################################################
#6.Написати програму калькулятор, яка складається з наступних функцій: 
# ÷головної, яка пропонує вибрати дію 
# ÷ додаткових, які реалізовують вибрані дії, 
# ÷калькулятор працює доти, поки ми не виберемо дію вийти з калькулятора, 
# ÷після виходу, користувач отримує повідомлення з подякою за вибір нашого програмного продукту!!!
import math
print("CALCULATOR")
a = float(input('First number : '))
x = str(input('''Choose action : 
÷ "+" - сума
÷ "-" - різниця
÷ "*" - добуток
÷ "/" - частка
÷ "%" - остача від частки 
÷ "^" - піднесення до степеня
÷ "!" - знаходження факторіалу
÷ "&" - знаходження кореня від числа
Action: '''))
b = int(input('Second number : '))

def choose_action():
    """ This function realize 
    calculator"""

    def find_suma(a,b):
        return a+b

    def find_rizn(a,b):
        return a - b 
    
    def find_ostacha(a,b):
        return a % b

    def find_stepin(a,b):
        return a ** b
        
    def find_sqrt(a):
        return math.sqrt(a)
    
    def find_factorial(a):
        return math.factorial(a) 

    def find_dobutok(a,b):
        
        return a * b
    
    def find_chastku(a,b):
        if b == 0 :
            print('Dilennia na "0" nemozluve!')
        else:
            return a/b
    
    if x == '+':
        res = find_suma(a,b)
        return res
    
    elif x == '-':
        res = find_rizn(a,b)
        return res

    elif x == '*':
        res = find_dobutok(a,b)
        return res

    elif x == '/':
        res = find_chastku(a,b)
        return res

    elif x == '%':
        res = find_ostacha(a,b)
        return res

    elif x == '&':
        res = find_sqrt(a)
        return res

    elif x == '!':
        res = find_factorial(a)
        return res

    elif x == '^':
        res = find_stepin(a,b)
        return res
print('RESULT: ', choose_action())


#################################################
#7.Побудувати рекурсивну функцію обчислення чисел Фібоначі до числа введеного користувачем.
def find_fib_sum(a):
    if a<3 :
        return 1
    else:
        return find_fib_sum(a-1) + find_fib_sum(a-2)
print('SUMA FIBONACHI: ', find_fib_sum(8))