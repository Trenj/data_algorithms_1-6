class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_key = self.hash_function(key)
        key_exists = False
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

    def search(self, key):
        hash_key = self.hash_function(key)
        bucket = self.table[hash_key]
        for kv in bucket:
            k, v = kv
            if key == k:
                return v
        return None

    def print_table(self):
        for bucket in self.table:
            if bucket:
                for kv in bucket:
                    print(f"Буква '{kv[0]}': {kv[1]} раз(а)")

# Пример использования
input_string = input("Введите строку: ")
hash_table = HashTable()

for char in input_string:
    count = hash_table.search(char)
    if count is None:
        hash_table.insert(char, 1)
    else:
        hash_table.insert(char, count + 1)

hash_table.print_table()

search_char = input("Введите букву для поиска: ")
count = hash_table.search(search_char)
if count is not None:
    print(f"Буква '{search_char}' найдена в хеш-таблице. Количество вхождений: {count}")
else:
    print(f"Буква '{search_char}' не найдена в хеш-таблице.")


"""
Составьте хеш-таблицу, содержащую буквы и количество их вхождений во введенной строке.
Вывести таблицу на экран.
Осуществить поиск введенной буквы в хеш-таблице.
"""