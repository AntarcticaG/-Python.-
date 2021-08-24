# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

a = []
for i in range(0,20):
  a.append(randint(0,100))
print(a)
indx_min = 0
indx_max = 0

for i in range(0,20):
  if a[indx_min] > a[i]:
    indx_min = i
  if a[indx_max] < a[i]:
    indx_max = i
a[indx_min], a[indx_max] = a[indx_max], a[indx_min]
print(a)
