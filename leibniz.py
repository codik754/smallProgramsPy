#Ряд Лейбница
from fractions import Fraction

m = int(input('Сколько чисел ряда показать: '))

for n in range(m):
   n1 = (-1) ** n #Вычисляем числитель
   n2 = 2 * n + 1 #Вычисляем знаменатель
   y = Fraction(n1, n2)
   print(y, end=' ')
print()
