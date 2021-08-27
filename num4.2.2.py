# Используя алгоритм «Решето Эратосфена»

from math import sqrt

N = int(input("До какого числа"))
a = []
a.append(N)
for i in range(N):
  a.append(1)

for i in range(4, N, 2):
  a[i] = 0

i = 3
while i <= sqrt(N-1):
  while a[i] == 0:
    i+=2
  if i <= sqrt(N-1):
    j = i * i
    while j <= N-1:
      a[j] = 0
      j = j + i * 2
  i += 2

for i in range(1,N):
  if a[i] == 1:
    print(i)
