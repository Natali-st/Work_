#дз

#1

"""
a = int(input("введите цифру от 1 до 7: "))

if a == 1:
  print("понедельник")
elif a == 2:
  print("вторник")
elif a == 3:
  print("среда")
elif a == 4:
  print("четверг")
elif a == 5:
  print("пятница")
elif a == 6:
  print("суббота")
elif a == 7:
  print("воскресение")
else:
  print("ошибка, попробуйте снова")
"""


#2

"""
a = int(input("введите цифру от 1 до 12: "))

if a == 1:
  print("январь")
elif a == 2:
  print("февраль")
elif a == 3:
  print("март")
elif a == 4:
  print("апрель")
elif a == 5:
  print("май")
elif a == 6:
  print("июнь")
elif a == 7:
  print("июль")
elif a == 8:
  print("август")
elif a == 9:
  print("сентябрь")
elif a == 10:
  print("октябрь")
elif a == 11:
  print("ноябрь")
elif a == 12:
  print("декабрь")
else:
  print("ошибка, попробуйте снова")
"""

#3

"""
a = int(input("введите любое число: "))

if a > 0:
  print("Number is positive")
elif a < 0:
  print("Number is negative")
else:
  print("Number is equal to zero")
"""


#4
"""
a = int(input("введите любое число: "))
b = int(input("введите любое число: "))

if a == b:
  print("числа равны")
elif a < b:
  print(f" получаем: {a} {b}") #f - префикс(для упрощения буду его использовать). 
else:
  print(f" получаем: {b} {a}")
"""


дз0.1

#1

"""
a = int(input("введите любое число: "))
b = int(input("введите любое число: "))
c = int(input("введите любое число: "))

you = input("сумма чисел (1) или произведение (2)? ")

if you == "1":
   print(a + b + c)
else:
   print(a * b * c)
"""

2#

"""
a = int(input("введите любое число: "))
b = int(input("введите любое число: "))
c = int(input("введите любое число: "))

you = input("максимальное число (1), минимальное (2) или среднее арифметическое (3)? ")

if you == "1":
  print(max(a, b, c))
elif you == "2":
  print(min(a, b, c))
else:
  print((a + b + c) / 3 ))
"""




#3

"""
a = int(input("введите любое кол-во метров: "))

you = input("мили(1), дюймы (2) или ярды (3)? ")

if you == "1":
  print(a * 0.000621371, "мили")
elif you == "2":
  print(a * 39.3701, "дюймы")
else:
  print(a * 1.09361, "ярды")
"""
