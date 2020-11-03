"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open('lesson_5_3.txt', 'r') as text:
    workers = text.readlines()
    money_start = 0
    money_end = 20000

    for name, money in map(lambda _: _.split(), workers):
        if float(money) < float(money_end):
            print(name)

        money_start += float(money)

    print(f'Средняя зарплата = {money_start / len(workers)}')
