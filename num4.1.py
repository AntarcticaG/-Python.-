import cProfile

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

cProfile.run('main()')
  #Возьмем для примера данный код
  #В нем вложенные циклы соответсветнно сложность O(2*m*n) т.к. два цикла в одном
  #сложность второй части будет O(m*n)
