"""1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе."""
list_type = [1, 'asad', 4.113, True, None, (1, 2, 5), {1, 4, 6}, [3, 5, 7, 7]]
for i in list_type:
    print(i, "this is", type(i))
