import pymorphy2


def word_case(number_of_objects: int) -> str:
    current_word = 'компьютер'
    morph = pymorphy2.MorphAnalyzer()
    word_parse = morph.parse(current_word)[0]
    word_result = word_parse.make_agree_with_number(number_of_objects).word
    return f'{number_of_objects} {word_result}'
    # Я знаю, что также можно реализовать огромную конструкцию с if, elif, else,
    # но мне кажется более правильным использовать pymorphy


# digit_of_objects = int(input('Введите число объектов: '))

digit_of_objects = 27
result = word_case(digit_of_objects)

print(result)

# Время выполнения задачи: 5 минут
