# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint
N, M = 4, 4
mas = []
for i in range(N):
    mas.append([])
    for j in range(M):
        mas[i].append(randint(0,10))
for i in range(N):
  for j in range(M):
    print(mas[i][j], end = ' ')
  print()   

buf = -1
for i in range(N):
  maxmin = 10
  for j in range(M):
    if maxmin > mas[j][i]:
      maxmin = mas[j][i]
  if buf < maxmin:
    buf = maxmin

print(buf)
    

