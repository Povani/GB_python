"""2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()."""
len_list = int(input('введите длину списка: '))
user_list = list()
while len(user_list) < len_list:
    value = input('введите элемент списка: ')
    user_list.append(value)
el = 0
for i in range(int(len(user_list) / 2)):
    user_list[el], user_list[el + 1] = user_list[el + 1], user_list[el]
    el += 2
print(user_list)
