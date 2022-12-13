# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# not (x or y or z) == not x and not y and not z

xyz = ["X", "Y", "Z"]
my_list = []
for i in range(3):
    my_list.append(input(f'Введите значение переменной {xyz[i]}: '))

left = not (my_list[0] or my_list[1] or my_list[2])
right = not my_list[0] and not my_list[1] and not my_list[2]

if left == right:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')