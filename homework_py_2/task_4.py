# Задайте список из N элементов, заполненных 
# числами из промежутка [-N, N].
#Найдите произведение элементов на указанных пользователем 
# через пробел позициях.

n = int(input('Введите число: '))

lists = []
temp = -n

for i in range(n + 1):
    if temp >= n:
        break
    lists.append(temp)
    temp += 2
    
print(lists)


index_num = [int(x) for x in input('Введите номера позиций элементов:').split()]

print(f"Произведение элементов списка с индексами {index_num}: ")

result = int(1)

for i in range(len(index_num)):
    result *= lists[index_num[i]]
    

print(result)