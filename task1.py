def list_to_str(get_towns_list: list) -> str:
    return ', '.join(get_towns_list) + '.'


# towns_list = input('Введите список городов через пробел: ').split(' ')
towns_list = ['Москва', 'Санкт-Петербург', 'Воронеж']
result = list_to_str(towns_list)
print(result)

# Время выполнения задачи: 1 минута

