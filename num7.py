#По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

a = int(input("Длинна первого отрезка "))
b = int(input("Длинна второго отрезка "))
c = int(input("Длинна третьего отрезка "))

if a + b > c or a + c > b or b + c > a:
  if a == b == c:
    print("Равносторонний")
  elif a == b or a == c or b == c:
    print("Равнобедренный")
  else:
    print("Разносторонний")
else:
  print("Треугольника нет")
