# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input("введите число "))
b = int(input("введите число "))
c = int(input("введите число "))

if b < a < c or c < a < b:
    print("Среднее ", a)
elif a < b < c or c < b < a:
    print("Среднее ", b)
else:
    print("Среднее ", c)
