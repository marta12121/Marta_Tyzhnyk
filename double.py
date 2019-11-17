def double_char(s):
    stroka = []
    for i in s:
        stroka.append(i*2)
        new_s = ''.join(stroka)
    return new_s
print(double_char('Hello'))