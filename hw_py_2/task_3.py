# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int

my_list = input('Введите элементы списка через пробел: ').split()

temp = 0

for i in range(len(my_list)):
    temp = my_list[i]
    my_list[i] = my_list[i-2]
    my_list[i-2] = temp

print(my_list)