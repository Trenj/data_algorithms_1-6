def count_punctuation(input_string):
    # Вручную определяем строку со всеми строчными латинскими буквами
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'

    # Вручную определяем строку со всеми знаками пунктуации
    punctuation_marks = '!"#$%&\'() * +, -./:; <= > ?@[] ^ _`{ |}~'

    # Строка в нижнем регистре
    input_string_lowercase = input_string.lower()

    # Формируем множество букв
    letters_in_string = []
    for char in lowercase_letters:
        if char in input_string_lowercase and char not in letters_in_string:
            letters_in_string.append(char)

    # Подсчитываем количество знаков препинания
    punctuation_count = 0
    for char in input_string:
        if char in punctuation_marks:
            punctuation_count += 1

    return letters_in_string, punctuation_count


# Ввод строки с клавиатуры
input_string = input("Введите строку: ")

# Получаем результат
letters, punctuation = count_punctuation(input_string)

# Выводим результат
print("Буквы в строке:", letters)
print("Количество знаков препинания:", punctuation)

"""
7.Составить программу формирования множества строчных латинских букв,
входящих в строку, введенную с клавиатуры, и подсчета количества знаков препинания в ней.
"""
