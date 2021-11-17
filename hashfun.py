#Хеш-функции
import hashlib

#print(hashlib.algorithms_guaranteed) #Список алгоритмов модуля
fhash = input("""Выбери хеш-функцию:
1.md5
2.sha256
3.sha512
Введите число: """)

text = input('Введите текст: ')

bit = True
if fhash == '1':
   hashObj = hashlib.md5(text.encode())
elif fhash == '2':
   hashObj = hashlib.sha256(text.encode())
elif fhash == '3':
   hashObj = hashlib.sha512(text.encode())
else:
   bit = False

if bit:
   print('Результат: ', hashObj.hexdigest())
