# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число: '))

fibo_list = [0, 1, 1]

i = 3
while i < n + 1:
    fib_sum = fibo_list[i-1] + fibo_list[i-2]
    fibo_list.append(fib_sum)
    i += 1

i = -1
k = -1
while i > -n - 1:
    fib_razn = fibo_list[k+2] - fibo_list[k+1]
    fibo_list = [fib_razn] + fibo_list 
    i -= 1


print(fibo_list)
