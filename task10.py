# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# 1 - герб, 0 - решка
# Ввод:
# 4 - число монет
# 0
# 1
# 1
# 1
# Вывод:
# 1

from random import randint
print("Введите количество монет- ", end=" ")
n = int(input()) # n-количество монеток
list = 0
count = 0
for i in range(n):
    list = randint(0, 1)
    print(list)
    if list == 0:
        count +=1
if count < n:
    print("требуется перевернуть ", count, "монет")
else:
    print("Требуется перевернуть ", n - count, "монет")