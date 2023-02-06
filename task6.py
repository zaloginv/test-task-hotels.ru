import pandas as pd


def multiplication_table(number: int) -> pd.DataFrame:
    list_of_lists = []
    for x in range(1, number + 1):
        list_of_multiply = []
        for y in range(1, number + 1):
            list_of_multiply.append(x * y)
        list_of_lists.append(list_of_multiply)

    df = pd.DataFrame(
        list_of_lists,
        columns=list_of_lists[0],
        index=list_of_lists[0]
    )

    return df


# digit = int(input('Введите число для создания таблицы умножения: '))
digit = 5
result = multiplication_table(digit)
print(result)

# Время выполнения задачи: 10 минут