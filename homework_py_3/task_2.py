# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lists = [int(x) for x in input('Введите значения элементов списка:').split()]
print(lists)

result = []
def multiplication(x,y):
    temp_result = int(1)
    j = len(x) - 1
    for i in range((len(x) + 1) // 2):
        temp_result = x[i] * x[j]
        y.append(temp_result)
        j -= 1
    return y

print(multiplication(lists, result))


