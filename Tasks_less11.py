#1.Спробуйте переписати наступний код через map. Він приймає список реальних імен і замінює їх хеш-прізвищами, 
# використовуючи  більш надійний метод-хешування.
# names = ['Sam', 'Don', 'Daniel'] 
# for i in range(len(names)): 
#     names[i] = hash(names[i]) 
# print(names)


# names = ['Sam', 'Don', 'Daniel'] 
# new_names = map(hash, names)
# print(list(new_names))

#2.Вивести список кольору “red”, який найчастіше зустрічається в даному списку  
# [“red”, “green”, “black”, “red”, “brown”, “red”, “blue”, “red”, “red”, “yellow” ] 
# використовуючи функцію filter.

# colours = ['red', 'green', 'black', 'red', 'brown', 'red', 'blue', 'red', 'red', 'yellow' ]
# def filt(colours):
#     return colours.count('red')
# colour2 = filter(filt, colours)
# print(list(colour2))

#3.Всі ці числа в списку мають стрічковий тип даних, наприклад  [‘1’,’2’,’3’,’4’,’5’,’7’], 
# перетворити цей список  в список, всі числа якого мають тип даних integer:
#1)  використовуючи метод  append
#2)  використовуючи метод  map

# a = ['1', '2', '3', '4', '5', '7']
# a2 = map(int, a)
# print(list(a2))

# a = ['1', '2', '3', '4', '5', '7']
# a1 = []
# i = 0
# for a[i] in a :
#     a1.append(int(a[i]))
# print(a1)

#4. Перетворити список, який містить милі ,  в список, який містить кілометри (1 миля=1.6 кілометра)
#a) використовуючи функцію map
#b) використовуючи функцію map та lambda

mile = [1, 2, 3, 4, 5, 7]

def kilometr(m):
    m =1
    for m in mile:
        m *= 1.6 
        return m
        
km = map(kilometr, mile)
print(list(km))


#5Знайти найбільший елемент в списку  використовуючи функцію reduce
#6. Перепишіть наступний код, використовуючи map, reduce і filter. Filter приймає функцію і колекцію. 
# Повертає колекцію тих елементів, для яких функція повертає True.
people = [{'name': 'Sam', 'height': 160}, {'name': 'Alex', 'height': 80}, {'name': 'Jack'}] 
height_total = 0 
height_count = 0 
for person in people: 
    if 'height' in person: 
        height_total += person['height'] 
        height_count += 1 
print(height_total)
