#Гармонический ряд
from fractions import Fraction

m = int(input('Какое количество чисел показать: '))

for n in range(1, m+1):
   y = Fraction(1, n)
   print(y, end='  ')

print('...')
