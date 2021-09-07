# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). 
#Выведите на экран исходный и отсортированный массивы.
from random import randint

def merge_sort(a):
    n = len(a)
    if n < 2:
        return a
    l = merge_sort(a[:n//2])
    r = merge_sort(a[n//2:n])
    i = j = 0
    res = []
    while i < len(l) or j < len(r):
        if not i < len(l):
            res.append(r[j])
            j += 1
        elif not j < len(r):
            res.append(l[i])
            i += 1
        elif l[i] < r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
    return res


a = []
for i in range(25):
    a.append(randint(0,50))
print(a)
print(merge_sort(a))
