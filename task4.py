from sympy import isprime


def my_isprime(number: int) -> bool:
    if number % 2 == 0:
        return number == 2

    divisor = 3

    while divisor * divisor <= number and number % divisor != 0:
        divisor += 2
    return divisor * divisor > number


def check(number: int) -> str:
    # result_bool = isprime(number)
    # Проще всего использовать эту функцию, но, видимо, в задании не это требуется
    result_bool = my_isprime(number)

    if result_bool:
        return f'Число {number} является простым'
    else:
        return f'Число {number} не является простым'


# digit = int(input('Введите число на проверку: '))
digit = 17

result = check(digit)
print(result)

# Время выполнения задачи: 10 минут