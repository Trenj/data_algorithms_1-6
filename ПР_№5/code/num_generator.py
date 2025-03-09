import random

def generate_random_sequence(length=1000):
    return [random.randint(-10000, 10000) for _ in range(length)]

def write_sequence_to_file(filename, sequence):
    with open(filename, 'w') as file:
        for number in sequence:
            file.write(f"{number}\n")

def generate_partial_sorted_sequence(length=1000, sorted_part_ratio=0.5):
    random_sequence = generate_random_sequence(length)
    sorted_length = int(length * sorted_part_ratio)
    sorted_part = sorted(random_sequence[:sorted_length])
    random_part = random_sequence[sorted_length:]
    return sorted_part + random_part

def generate_reverse_sorted_sequence(length=1000):
    random_sequence = generate_random_sequence(length)
    return sorted(random_sequence, reverse=True)

# Файл 1: последовательность из 1000 рандомных значений
sequence1 = generate_random_sequence()
write_sequence_to_file('file1.txt', sequence1)

# Файл 2: частично отсортированная последовательность
sequence2 = generate_partial_sorted_sequence()
write_sequence_to_file('file2.txt', sequence2)

# Файл 3: последовательность в обратном порядке
sequence3 = generate_reverse_sorted_sequence()
write_sequence_to_file('file3.txt', sequence3)

print("Файлы успешно созданы и записаны.")
