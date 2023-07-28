#4. Создайте функцию генератор чисел Фибоначчи
n = int(input('Введите число , будет кол-вом чисел фибоначчи  '))
def get_fibonacci(n):
   fibo_nums = []
   a, b = 1, 1
   for i in range(n):
       fibo_nums.append(a)
       a, b = b, a + b

   return fibo_nums
print('Список чисел фибоначчи :',get_fibonacci(n))
