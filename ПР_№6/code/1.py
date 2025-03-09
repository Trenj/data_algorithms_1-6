import random


def generate_random_array(size):
    """Формирует массив случайных чисел от 0 до 100."""
    return [random.randint(0, 100) for _ in range(size)]


def linear_search(arr, key):
    """Реализует последовательный (линейный) поиск заданного ключа в массиве.

    Аргументы:
    arr -- массив для поиска;
    key -- ключ для поиска.

    Возвращает:
    количество совпадений и список индексов, по которым находятся совпадения.
    """
    indices = [i for i, x in enumerate(arr) if x == key]
    return len(indices), indices


def binary_search(arr, key):
    """Реализует бинарный поиск заданного ключа в массиве. Предполагается, что массив отсортирован.

    Аргументы:
    arr -- отсортированный массив для поиска;
    key -- ключ для поиска.

    Возвращает:
    количество совпадений и список индексов, по которым находятся совпадения.
    """
    left, right = 0, len(arr) - 1
    indices = []

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            indices.append(mid)
            # Проверка влево от найденного элемента
            i = mid - 1
            while i >= 0 and arr[i] == key:
                indices.insert(0, i)
                i -= 1
            # Проверка вправо от найденного элемента
            j = mid + 1
            while j < len(arr) and arr[j] == key:
                indices.append(j)
                j += 1
            break
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return len(indices), indices


def main():
    # Запрашиваем размер массива у пользователя
    size = int(input("Введите размер массива: "))
    # Запрашиваем ключ для поиска у пользователя
    key = int(input("Введите ключ поиска: "))

    # Генерация массива случайных чисел
    array = generate_random_array(size)
    print("Сгенерированный массив:", array)

    # Линейный поиск
    count, indices = linear_search(array, key)
    print(f"Линейный поиск: найдено {count} совпадений по индексам: {indices}")

    # Подготовка к бинарному поиску: сортировка массива
    sorted_array = sorted(array)
    print("Отсортированный массив:", sorted_array)

    # Бинарный поиск
    count, indices = binary_search(sorted_array, key)
    print(f"Бинарный поиск: найдено {count} совпадений по индексам: {indices}")


if __name__ == "__main__":
    # Запуск основной функции
    main()

"""
Написать программу, которая:
1) запрашивает у пользователя размер массива и ключ поиска;
2) формирует массив случайных чисел;
3) возвращает количество совпадений и их номера.

Реализовать программу с помощью следующих алгоритмов: последовательный (линейный) поиск (для варианта 1)
и бинарный поиск (для варианта 2).
"""