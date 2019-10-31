x = input("Input four-digit natural number :")
x = int(x)
 
d = x % 10
y = x // 10
c = y % 10
z = y // 10
b = z % 10
f = z // 10
a = f % 10
 
print("The product of the digits of a number:", d * c * b * a)
print('The number in reverse order:', str(d)+str(c)+str(b)+str(a))

p = list(map(int, str(x)))
p.sort()
print(p) 