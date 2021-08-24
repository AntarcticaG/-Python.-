# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint
a = []
for i in range(0,10):
  a.append(randint(0,100))
print(a)
indx_max = 0
indx_min = 0
for i in range(0,10):
  if a[indx_max]<a[i]:
    indx_max = i
  if a[indx_min]>a[i]:
    indx_min = i
if indx_min > indx_max:
  indx_max, indx_min = indx_min, indx_max
summa = 0
for i in range(indx_min+1, indx_max):
  summa += a[i]
print(summa)
