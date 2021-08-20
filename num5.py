# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

first = str(input("Введите букву = "))
second = str(input("Введите букву = "))

print("Первый символ стоит на ", ord(first)-96)
print("Второй символ стоит на ", ord(second)-96)

if first > second:
  first, second = second, first

print("Между ними находится ", ord(second)-ord(first)-1)