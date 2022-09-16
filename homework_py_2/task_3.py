# Задайте список из k чисел последовательности (1 + 1\k)^k и 
# выведите на экран их сумму.

k = int(input('Введите число: '))

listek = list(range(1, k+1))
result_list = []

for i in range(1, k+1):
    result = (1 + 1 / i)**i
    result_list.append(result)

print(result_list)


#for b in range:
 #   print(round(result_list[b]:2)) у меня непонятки с округлением постоянно, возможно ли сделать вывод списка с округлением?