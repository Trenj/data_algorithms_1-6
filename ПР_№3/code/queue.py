def process_queue(queue):
    if not queue:
        return []

    # Используем первый элемент в качестве текущего для сравнения
    current = queue.pop(0)
    print(current, end='\n')  # Выводим первый элемент, так как он точно останется

    # Проходим по оставшимся элементам очереди
    for _ in range(len(queue)):
        if queue and current != queue[0]:  # Если очередь не пуста и следующий элемент не равен текущему
            current = queue.pop(0)         # Берем следующий элемент как текущий
            print(current, end='\n')        # Выводим текущий элемент
        else:
            queue.pop(0)                   # Удаляем повторяющийся элемент

def main():
    n = int(input("Введите количество элементов в очереди: "))
    queue = []

    for i in range(n):
        item = input(f"Введите {i+1}-й элемент очереди: ")
        queue.append(item)

    print("Обработанная очередь:")
    process_queue(queue)

if __name__ == "__main__":
    main()



"""
7.Дана очередь символов. Преобразовать очередь, оставив в ней из группы подряд идущих одинаковых элементов только один.
"""
