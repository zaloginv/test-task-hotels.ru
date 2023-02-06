def lists_to_compare(first_list: list, second_list: list) -> list:
    result_list = []

    for element in first_list:
        if first_list.count(element) > 1 and second_list.count(element) > 1 and \
                element not in result_list:
            result_list.append(element)

    return result_list


list_1 = [7, 17, 1, 9, 1, 17, 56, 56, 23]
list_2 = [56, 17, 17, 1, 23, 34, 23, 1, 8, 1]

result = lists_to_compare(list_1, list_2)
print(result)

# Время выполнения задачи: 15 минут