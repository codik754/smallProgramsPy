#Ряд Фибоначи
m = 0
try:
   m = int(input("Сколько чисел показать:"))
except Exception as s:
   print('Произошла ошибка!\n', s)
n1 = 0 #первое число в последовательности
n2 = 1 #второе число в последовательности
for i in range(m):
   print(n2, end=' ')
   temp = n2
   n2 += n1
   n1 = temp
print()
