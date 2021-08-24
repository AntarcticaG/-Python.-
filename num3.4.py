# Определить, какое число в массиве встречается чаще всего.

from random import randint

a = []
b = []
minimum = 100
maximum = 0
for i in range(0,100):
  a.append(randint(0,100))
  if a[i] > maximum:
    maximum = a[i]
  if a[i] < minimum:
    minimum = a[i]
for i in range(minimum, maximum+1):
  b.append(0)

for i in a:
  b[i]+=1
maximum = 0
for i in range(0, len(b)):
  if b[i] > maximum:
    maximum = i

print(a)
print(maximum)
