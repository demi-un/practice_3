data = input('Введите строку: ')

number_of_vowels = 0
number_of_consonant = 0

for el in data.lower():
    if el in 'аеёиоуыэюяaeiouy':
        number_of_vowels += 1
    elif el in 'бвгджзйклмнпрстфхцчшщъьbcdfghjklmnpqrstvwxz':
        number_of_consonant += 1

number_of_space = data.count(' ')
number_of_word = len(data.split())

# подсчет каждого символа
all_simbol = {}
for el in data:
    if el not in all_simbol:
        all_simbol[el] = 0
    all_simbol[el] += 1


# сортировка по убыванию количества элементов
top_3 = sorted(all_simbol, key=lambda x: int(all_simbol[x]), reverse=True)
if len(top_3) >= 3:
    top_3 = top_3[:3]


def info(vowels, consonant, space, top, word):
    print(f'Количество гласных: {vowels}')
    print(f'Количество согласных: {consonant}')
    print(f'Количество пробелов: {space}')
    print(f'Количество слов: {word}')
    print(f'Топ самых используемых символов: {top}')


info(number_of_vowels, number_of_consonant, number_of_space, top_3, number_of_word)