#Ряд обратных простых чисел
from fractions import Fraction
import random

def isPrimeNumber(n):
   """Функция, проверяющая простотуш числа"""
   if n == 1: return True
   if (random.randint(1, n - 1) ** (n - 1)) % n == 1: return True
   return  False

def isOtherPrime(n):
   """Еще одна проверка"""
   if n % 2 == 0 and n != 2: return False
   elif n % 3 == 0 and n != 3: return False
   elif n % 4 == 0 and n != 4: return False
   elif n % 5 == 0 and n != 5: return False
   elif n % 6 == 0 and n != 6: return False
   elif n % 7 == 0 and n != 7: return False
   elif n % 8 == 0 and n != 8: return False
   elif n % 9 == 0 and n != 9: return False
   return True

m = int(input('Сколько чисел показать: '))

i = 0
j = 2
while i < m:
   if isPrimeNumber(j):
      if isOtherPrime(j):
         y = Fraction(1, j)
         print(y, end='  ')
         i += 1
   j += 1

print()
