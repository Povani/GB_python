"""4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции."""
user_number = int(input('Введите целое положительное число: '))
biggest_number = user_number % 10
while user_number > 0:
    number = user_number % 10
    user_number = user_number // 10
    if number > biggest_number:
        biggest_number = number
print(f'Наибольшей цифрой в числе является {biggest_number}.')
