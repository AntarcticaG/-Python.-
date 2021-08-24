#  Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. 
#  Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. 
#  В конце следует вывести полученную матрицу.

N, M = 4, 4
mas = []
for i in range(N):
    mas.append([])
    for j in range(M):
        mas[i].append(int(input("число ")))
    summa = 0
    for j in range(M):
      summa += mas[i][j]
    mas[i].append(summa)

for i in range(N):
  for j in range(M+1):
    print(mas[i][j], end = ' ')
  print()   
