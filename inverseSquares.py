#Ряд обратных квадратов
from fractions import Fraction

m = int(input('Сколько чисел ряда показать: '))

for n in range(1, m+1):
   y = Fraction(1, n**2)
   print(y, end='  ')
print()
