# В массиве найти максимальный отрицательный элемент. 
# Вывести на экран его значение и позицию в массиве.

from random import randint

a = []

for i in range(0,10):
  a.append(randint(-100,100))
print(a)
maximum = -100
for i in range(0,10):
  if a[i]<0 and a[i] > maximum:
    maximum = a[i]
print(maximum)
