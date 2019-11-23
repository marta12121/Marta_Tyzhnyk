def filter_words(st):
    a = len(st)+1
    i = 1
    for i in range(1,a):
        st[i].lower()
        v = st[0].upper() + st.lower()
        c = v[0]+v[2:a]
        return (' '.join(c.split())) 
print(filter_words('This    will    not    pass '))


