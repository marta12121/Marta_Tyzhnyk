arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
l = []
l1 = [0, 0]
def count_positives_sum_negatives(arr):
    count = 0
    suma = 0 
    for i in arr:
        if i > 0:
            count += 1
        else:
            suma += i

    l.append(count)
    l.append(suma)
    if arr == []:
        return l1
    elif i == 0 :
        return l1
    else:
        return l
print(count_positives_sum_negatives(arr))