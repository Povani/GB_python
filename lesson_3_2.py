"""2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""


def contact(**kwargs):
    contact_list = {**kwargs}
    return list(contact_list.values())


try:
    print(contact(name=input('Введите имя: ').capitalize(),
                  surname=input('Введите фамилию: ').capitalize(),
                  b_year=int(input('Введите год рождения: ')),
                  sity=input('Введите город проживания: ').capitalize(),
                  email=input('Введите эл.почту: ').lower(),
                  phone=int(input('Введите номер телефона: '))))
except ValueError:
    print('Неправильный ввод')
