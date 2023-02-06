def round_up_to_five(number: float) -> int:
    if number % 10 > 5:
        number = number // 10 * 10 + 5
    else:
        number = number // 10
    return int(number)


# digit = float(input('Введите число типа float: '))
digit = 27.8
result = round_up_to_five(digit)
print(result)

# Время выполнения задачи: 2 минуты