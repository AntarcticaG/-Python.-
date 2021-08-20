# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. 
# Вывести на экран это число и сумму его цифр.
maximum = 0
while True:
  summa = 0
  a = abs(int(input("Введите число ")))
  if a == 0:
    break
  while a:
    summa += a%10
    a //= 10
  if maximum < summa:
    maximum = summa
print(maximum)
