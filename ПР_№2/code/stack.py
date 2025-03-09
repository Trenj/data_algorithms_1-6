import random

class stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Ошибка: Стек пуст"

    def sum_first_k_elements(self, k):
        if len(self.stack) < k:
            return "Ошибка: Стек содержит меньше элементов, чем запрошено для сложения"
        else:
            temp_stack = []
            for i in range(len(self.stack)):
                temp_stack.append(self.stack.pop())

            total = 0
            for _ in range(k):
                total += temp_stack.pop()

            while temp_stack:
                self.stack.append(temp_stack.pop())

            self.stack.append(total)
            return total
    def clear_stack(self):
        while len(self.stack) != 0:
            self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

# Ввод колличества позиций в стеке
n = int(input("Введите колличество елементов стека: "))
stack = stack()

# Генерация наполнения стека
while n > 0:
    stack.push(random.randint(1,100))
    n -= 1
print("Содержание стека:", stack.stack)

# Ввод элементов для сложения
k = int(input("Введите количество первых элементов для сложения: "))
k = stack.sum_first_k_elements(k)
print(k)

# Очистка стека
stack.clear_stack()

# Добавление суммы первых k элементов и вывод содержания стека
stack.push(k)
print("Содержание стека:", stack.stack)

"""
7.Сформировать стек из N чисел. Найти сумму первых K чисел. Результат поместить в стек.
"""
