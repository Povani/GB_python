"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""


from sys import argv

_, param_hours, param_rate, param_bonus = argv


def salary(hours, rate, bonus):
    """ Простой расчет зарплаты
    :param hours:
    :param rate:
    :param bonus:
    :return:
    """
    return hours * rate + bonus


print('Зарплата сотрудника: ', salary(float(param_hours), float(param_rate), float(param_bonus)))
