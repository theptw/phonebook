# Реализуйте алгоритм перемешивания списка.


from random import random, shuffle 


a = [int(x) for x in input('Введите значения списка через пробел: ').split()]
print(a)
temp = int(0)

for i in range(len(a) + 1): 
    if i >= len(a) - 1: 
        break # без break постоянно выходит за пределы диапозона, не понимаю как без него сделать
    temp = a[i]
    a[i] = a[i+1]
    a[i+1] = temp

print(a)
    
    
# shuffle не работает, тоже не могу понять почему, выдаёт ошибку: AttributeError: 'builtin_function_or_method' object has no attribute 'shuffle'