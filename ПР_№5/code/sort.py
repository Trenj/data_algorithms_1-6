import time

def bubble_sort_positive(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # Пропускаем сравнение, если элемент отрицательный или уже отсортирован
            if arr[j] <= 0 or arr[j+1] <= 0:
                continue
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def comb_sort_positive(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True

        i = 0
        while i + gap < n:
            # Пропускаем сравнение, если элемент отрицательный или уже отсортирован
            if arr[i] <= 0 or arr[i+gap] <= 0:
                i += 1
                continue
            if arr[i] > arr[i+gap]:
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
                sorted = False
            i += 1

    return arr

# Пример использования
array = []

# Ввод имени файла пользователем
filename = input("Введите имя файла: ")

with open(filename, "r") as file:
    for line in file:
        array.append(int(line.strip()))  # Преобразуем каждую строку в число

print("Исходный массив:", array)

# Время выполнения пузырьковой сортировки
start_time = time.time()
sorted_array_bubble = bubble_sort_positive(array.copy())
bubble_sort_time = time.time() - start_time
print("Отсортированный массив (пузырьковая сортировка):", sorted_array_bubble)
print(f"Время выполнения пузырьковой сортировки: {bubble_sort_time:.6f} секунд")

# Время выполнения сортировки расческой
start_time = time.time()
sorted_array_comb = comb_sort_positive(array.copy())
comb_sort_time = time.time() - start_time
print("Отсортированный массив (расческа-сортировка):", sorted_array_comb)
print(f"Время выполнения сортировки расческой: {comb_sort_time:.6f} секунд")

# Сравнение времени выполнения сортировок
if bubble_sort_time < comb_sort_time:
    faster_sort = "пузырьковая сортировка"
    slower_sort_time = comb_sort_time
    faster_sort_time = bubble_sort_time
else:
    faster_sort = "сортировка расческой"
    slower_sort_time = bubble_sort_time
    faster_sort_time = comb_sort_time

ratio = slower_sort_time / faster_sort_time

print(f"{faster_sort} быстрее в {ratio:.2f} раз")

"""
7.Отсортировать положительные элементы одномерного массива, отрицательные оставить на местах.
Сортировки: пузырьковая и расческой.
"""
