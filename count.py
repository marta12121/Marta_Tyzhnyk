arr = [0,0,0,0,0,0,0,0,0]
def count_positives_sum_negatives(arr):
  count = 0
  suma = 0
  for i in arr:
    if i > 0:
      count += 1
    else:
      suma += i
  l1 = [0, 0]
  l = []
  l.append(count)
  l.append(suma)
  if i == 0:
      return l1
  else:
      return l
print(count_positives_sum_negatives(arr))