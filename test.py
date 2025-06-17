import random


# Список уровней сложности
x = [
    {'value':10, 'attempt': 5},
    {'value':50, 'attempt': 7},
    {'value':100, 'attempt': 10},
]

count = {'wins': 0, 'losses': 0}

def save_result():
    with open('stats.txt', 'w') as f:
        f.write(str(count))

def game_num():

    while True:
        # Выбор уровня сложности
        while True:
            try:
                difficult = int(input('Выберите уровень сложности (Легкий(1),Средний(2),Сложный(3)): '))-1
                break
            except ValueError:
                print('Введите число!')

        num = random.randint(1,x[difficult]['value'])  # Генерация загаданного числа
        attempts = x[difficult]['attempt'] # Попытки

        # Цикл игры
        while attempts > 0:

            # Выбор числа
            while True:
                try:
                    choice_num = int(input(f'Выберите число от 1 до {x[difficult]['value']}'))
                    break
                except ValueError:
                    print("Введите число!")

            if choice_num == num:
                print('Поздравляю вы угадали!')
                count['wins'] += 1
                break
            elif choice_num < num:
                print('Загаданное число больше!')
                attempts -= 1
            elif choice_num > num:
                print('Загаданное число меньше!')
                attempts -= 1
            else:
                pass
            print('Осталось попыток', attempts)

        if attempts == 0:
            count['losses'] += 1
            print('Вы проиграли! Загаданное число:', num)

        print('Побед:', count['wins'], 'Поражений:', count['losses'])
        save_result()
        play_again = input('Сыграть еще раз? (да/нет): ').lower()
        if play_again == 'да':
            continue
        elif play_again == 'нет':
            break

game_num()
