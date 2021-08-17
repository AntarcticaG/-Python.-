# Написать программу, которая генерирует в указанных пользователем границах:
from random import randint, random


#     случайное целое число;
#     случайное вещественное число;
#     случайный символ.

flag = int(input("Что ввести: \n1.целое число \n2.вещественное число \n3.символ\n"))
if flag == 1:
  Min = int(input("минимальное число = "))
  Max = int(input("максимальное число = "))
  print(randint(Min, Max))
if flag == 2:
  Min = float(input("минимальное число = "))
  Max = float(input("максимальное число = "))
  print(random() * (Max - Min) + Min)
if flag == 3:
  Min = ord(str(input("минимальный символ = ")))
  Max = ord(str(input("максимальный символ = ")))
  print(chr(randint(Min, Max)))
  