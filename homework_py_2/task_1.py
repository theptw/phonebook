# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

# Пример:

# - 0,56 -> 11



a = (input('Введите число: '))
result = int(0)
for i in range(len(a)):
    if a[i].isdigit() == True:
        result += int(a[i])

print(result)