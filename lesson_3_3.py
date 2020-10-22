"""3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""


def my_func():
    try:
        arg_1 = float(input('введите первое число: '))
        arg_2 = float(input('введите второе число: '))
        arg_3 = float(input('введите третье число: '))
    except ValueError:
        return "Неправильный ввод"
    if arg_3 <= arg_2 and arg_3 <= arg_1:
        sum_max = arg_1 + arg_2
    elif arg_2 <= arg_3 and arg_2 <= arg_1:
        sum_max = arg_3 + arg_1
    else:
        sum_max = arg_3 + arg_2
    # sum_1 = arg_1 + arg_2 + arg_3 - min(arg_1, arg_2, arg_3)
    # return sum_1 если не использовать if
    return sum_max


print(my_func())
