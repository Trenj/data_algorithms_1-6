class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_key = self.hash_function(key)
        for pair in self.table[hash_key]:
            if pair[0] == key:
                pair[1] += value
                return
        self.table[hash_key].append([key, value])

    def search(self, key):
        hash_key = self.hash_function(key)
        for pair in self.table[hash_key]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete_by_prefix(self, prefix):
        for bucket in self.table:
            for pair in bucket:
                if pair[0].startswith(prefix):
                    bucket.remove(pair)

    def print_table(self):
        for bucket in self.table:
            for pair in bucket:
                print(f"Слово '{pair[0]}': {pair[1]} раз(а)")

# Пример использования
file_name = input("Введите имя файла: ")
table_size = int(input("Введите размерность таблицы: "))
hash_table = HashTable(table_size)

with open(file_name, 'r', encoding='utf-8') as file:
    for line in file:
        words = line.split()
        for word in words:
            count = hash_table.search(word)
            if count is None:
                hash_table.insert(word, 1)
            else:
                hash_table.insert(word, count + 1)

hash_table.print_table()

search_word = input("Введите слово для поиска: ")
count = hash_table.search(search_word)
if count is not None:
    print(f"Слово '{search_word}' найдено в таблице. Количество вхождений: {count}")
else:
    print(f"Слово '{search_word}' не найдено в таблице.")

delete_prefix = input("Введите букву для удаления слов, начинающихся на нее: ")
hash_table.delete_by_prefix(delete_prefix)
hash_table.print_table()

"""
Постройте хеш-таблицу из слов произвольного текстового файла, задав ее размерность с экрана.
Выведите построенную таблицу слов на экран.
Осуществите поиск введенного слова.
Выполните программу для различных размерностей таблицы и сравните количество сравнений.
Удалите все слова, начинающиеся на указанную букву, выведите таблицу.
"""