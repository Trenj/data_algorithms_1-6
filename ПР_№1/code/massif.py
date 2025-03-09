import random

n = int(input("Введите колличество елементов массива: "))

pos_num = 0
last_pos_num_id = -1
sum_neg_after_pos = 0

# Задаём массив из n елементов целых случайных чисел в диапазоне от 1 до 1000
random_massif = [random.randint(-100, 100) for i in range(n)]

print(random_massif)

# Перебераем массива для поиска последнего положительного елемента
for i in range(n):
    if random_massif[i] > 0:
        pos_num = random_massif[i]
        last_pos_num_id = i

# Суммируем все отрицательные елементы после последниго положительного елемента
if last_pos_num_id != -1:
    for j in range(last_pos_num_id + 1, n):
        if random_massif[j] < 0:
            sum_neg_after_pos += random_massif[j]

print("Сумма отрицательных элементов, стоящих после последнего положительного элемента: ", sum_neg_after_pos)

'''
7.Дан одномерный целочисленный массив порядка N. Найдите сумму отрицательных элементов массива, 
стоящих после последнего положительного элемента. Если таких элементов нет, вернуть значение 0.
'''