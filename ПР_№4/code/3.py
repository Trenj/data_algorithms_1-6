class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        hash_key = self.hash_function(key)
        self.table[hash_key].append(key)

    def search(self, key):
        hash_key = self.hash_function(key)
        for num in self.table[hash_key]:
            if num == key:
                return True
        return False

# Пример использования
file_name = input("Введите имя файла: ")
table_size = int(input("Введите размерность таблицы: "))
hash_table = HashTable(table_size)

with open(file_name, 'r', encoding='utf-8') as file:
    for line in file:
        num = int(line.strip())
        hash_table.insert(num)

search_num = int(input("Введите целое число для поиска: "))
found = hash_table.search(search_num)
if found:
    print(f"Число {search_num} найдено в таблице.")
else:
    print(f"Число {search_num} не найдено в таблице.")

"""
В текстовом файле содержатся целые числа.
Постройте хеш-таблицу для чисел из файла.
Выполните поиск введенного целого числа в хеш-таблице.
"""
