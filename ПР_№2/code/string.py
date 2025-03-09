from datetime import datetime

# Класс для хранения всех характеристик компьютера
class Computer:
    def __init__(self, code, brand, processor_type, processor_speed, ram, hard_drive, release_date, price, quantity):
        self.code = code
        self.brand = brand
        self.processor_type = processor_type
        self.processor_speed = processor_speed
        self.ram = ram
        self.hard_drive = hard_drive
        self.release_date = datetime.strptime(release_date, '%Y-%m-%d')
        self.price = price
        self.quantity = quantity

# Класс, представляющий узел в связном списке
class Node:
    def __init__(self, data=None):
        self.data = data                                                        # Хранящийся данные
        self.next = None                                                        # Ссылка на следующую ноду

# Класс, представляющий связный список
class LinkedList:
    def __init__(self):
        self.head = None

    # Метод для добавления компьютера в конец списка
    def append(self, data):
        if not self.head:                                                       # Условие если нет первого элемента
            self.head = Node(data)                                              # Записываем данные в ноду
        else:
            current = self.head                                                 # текущая нода (current)
            while current.next:
                current = current.next
            current.next = Node(data)

    # Метод для поиска компьютера по критериям
    def search(self, processor_type=None, ram=None, release_date=None):
        current = self.head
        while current:
            if (processor_type and current.data.processor_type == processor_type) or \
               (ram and current.data.ram == ram) or \
               (release_date and current.data.release_date == datetime.strptime(release_date, '%Y-%m-%d')):
                return current.data
            current = current.next
        return None


    # Метод для сортировки компьютеров по критерию
    def sort(self, by='processor_type'):
        if not self.head:  # Проверка наличия элементов в списке
            return

        swapped = True
        while swapped:                                                                  # Проверка отсортированности списка
            swapped = False
            current = self.head

            while current and current.next:                                             # Пробегаем по списку и сравниваем все елементы с критерием
                if getattr(current.data, by) > getattr(current.next.data, by):
                    # Меняем местами данные компьютеров
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next


    # Вспомогательный метод для вставки данных компьютера в отсортированный список
    def _sorted_insert(self, sorted_list, new_node, by):
        if not sorted_list or getattr(sorted_list.data, by) <= getattr(new_node, by):   # Проверка, существует ли отсортированный список или он пустой
            new_node.next = sorted_list
            sorted_list = Node(new_node)
        else:                                                                           # Вставка узла в начало или конец списка
            current = sorted_list
            while current.next and getattr(current.next.data, by) < getattr(new_node, by):
                current = current.next
            new_node.next = current.next
            current.next = Node(new_node)
        return sorted_list                                                              # Возвращаем ссылку на отсортированный список

    # Метод для печати списка компьютеров
    def print_list(self):
        current = self.head
        while current:
            print(current.data.__dict__)
            current = current.next

# Пример использования
linked_list = LinkedList()

computer1 = Computer('001', 'Dell', 'Intel Core i7', 3.6, 16, 1000, '2020-01-01', 1200, 10)
linked_list.append(computer1)

computer2 = Computer('002', 'HP', 'AMD Ryzen 5', 3.8, 8, 500, '2019-05-01', 800, 5)
linked_list.append(computer2)

computer3 = Computer('003', 'Lenovo', 'Intel Core i5', 3.2, 12, 750, '2021-02-15', 1000, 8)
linked_list.append(computer3)

computer4 = Computer('004', 'Acer', 'AMD Ryzen 7', 3.5, 16, 512, '2018-09-10', 1100, 6)
linked_list.append(computer4)

computer5 = Computer('005', 'Asus', 'Intel Core i9', 4.0, 32, 2000, '2022-07-20', 2000, 12)
linked_list.append(computer5)

computer6 = Computer('006', 'MSI', 'AMD Ryzen 9', 3.9, 24, 1000, '2023-04-05', 1500, 15)
linked_list.append(computer6)

computer7 = Computer('007', 'Apple', 'M1', 3.2, 16, 512, '2020-11-12', 1800, 7)
linked_list.append(computer7)

# Поиск компьютера по типу процессора
found_computer = linked_list.search(processor_type='Intel Core i5')
print("Found computer:", found_computer.__dict__ if found_computer else "Not found")

# Сортировка по типу процессора
linked_list.sort(by='processor_type')
print("Sorted list:")
linked_list.print_list()

"""
7.Модель компьютера характеризуется:

- кодом и маркой компьютера, 
- типом процессора (может содержать цифры и буквы),
- частотой работы процессора, 
- объемом оперативной памяти, 
- объемом жесткого диска, 
- датой выпуска на рынок,
- стоимостью компьютера в рублях 
- и количеством экземпляров, имеющихся в наличии.

Поиск и сортировка — по:
типу процессора,
объему ОЗУ, 
дате выпуска компьютера на рынок.
"""
