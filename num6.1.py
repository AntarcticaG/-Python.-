# Подсчитать, сколько было выделено памяти под переменные в 
# ранее разработанных программах в рамках первых трех уроков. 
# Проанализировать результат и определить программы с наиболее 
# эффективным использованием памяти.

import sys

# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint
a = []
sizeelem = 0
buf = 0
for i in range(0,10):
  buf = randint(0,100)
  sizeelem += sys.getsizeof(buf)  #Считаю размеры элементов массива
  a.append(buf)
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

sizemass = sys.getsizeof(a) #Память выделенная под массив
print(f'Память под массив {sizemass + sizeelem}')
# Индексы и суммы это просто инты 
#Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
