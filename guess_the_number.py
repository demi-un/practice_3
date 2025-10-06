import random

min_value, max_value = map(int, input('Введите диапазон чисел через пробел (например: 1 50): ').split())
hidden_number = random.randint(min_value, max_value)

for attempt in range(3):
    number = int(input('Введите число: '))
    if number == hidden_number:
        print('Вы угадали число')
        break
    elif number > hidden_number:
        print('Загаданное число меньше')
    else:
        print('Загаданное число больше')
    if attempt == 2:
        print('Загаданное число четное') if hidden_number % 2 == 0 else print('Загаданное число нечетное')
    print('<------------------------------------->')



