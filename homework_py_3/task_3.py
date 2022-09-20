# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19


float_list = [1.9, 1.2, 3.1, 10.01]
print(float_list)

def float_difference(lisst):
    float_part_max = float(0)
    float_part_min = float(0.1)
    result = float(0)
    for i in range(len(lisst)):
        if lisst[i] % 1 > float_part_max:
            float_part_max = lisst[i] % 1
        elif lisst[i] % 1 < float_part_min:
            float_part_min = lisst[i] % 1

    result = float_part_max - float_part_min
    return result

print(round(float_difference(float_list), 2))


