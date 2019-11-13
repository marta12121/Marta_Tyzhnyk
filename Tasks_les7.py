import random
import math
a = random.randint(1,100)
print(a)
x = int(input('Спробуйте вгадати згенероване число: '))
while x !=a:
    x = int(input('Спробуйте ще: '))
    if x >a:
        print('Спробуйте число менше :')
    elif x< a:
        print('Спробуйте число більше:')

print('Вітаю!')

##############################
numb = random.randint(1,100)
while True:
    x = int(input('Спробуйте вгадати згенероване число: ')) 
    i = int(x)
    if i == x :
        print('Вітаю!')
        break
    elif i < x:
        print('Спробуйте число більше:')
    elif i > a:
        print('Спробуйте число менше :')

##############################

a = int(input('Сторона а ='))
b = int(input('Сторона b ='))
h = int(input('Сторона h ='))
r = int(input('Сторона r ='))
s1 = math.pow(a,b)
s2 = 0.5 * math.pow(h,a)
s3 = math.pi * math.pow(r,2)
print('Площа прямокутника', s1)
print('Площа трикутника', s2)
print('Площа кола', s3)