#Разложение числа на простые множители

m = int(input('Введите число: '))

L = [] #список простых множителей

n = 2
while m != 1: 
   if m % n == 0:
      L.append(n)
      m /= n 
   else:
      n += 1

print(L)
