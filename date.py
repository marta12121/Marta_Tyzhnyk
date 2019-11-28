def shorten_to_date(long_date):
    a  = long_date.split()
    s = a[2][0] 
    s2 = a[2][1] 
    if s2 == ',':
        short = ' '.join(a[0:2]) + ' ' + s 
    elif int(a[2][0]+a[2][1])>9:
        short = ' '.join(a[0:2]) + ' ' + s + s2
    return short 
print(shorten_to_date("Monday February 29, 8pm"))
