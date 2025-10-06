import random

player_victories = 0
bot_victories = 0


while player_victories < 3 and bot_victories < 3:
    bot_move = random.choice(['камень', 'ножницы', 'бумага'])
    player_move = input('Сделайте ход (камень/ножницы/бумага): ')

    print(f'{player_move} -> {bot_move}')
    if bot_move == player_move:
        print('ничья')
    elif (bot_move == 'камень' and player_move == 'ножницы') or (bot_move == 'бумага' and player_move == 'камень') or (
            bot_move == 'ножницы' and player_move == 'бумага'):
        print('раунд проигран')
        bot_victories += 1
    elif (player_move == 'камень' and bot_move == 'ножницы') or (player_move == 'бумага' and bot_move == 'камень') or (
            player_move == 'ножницы' and bot_move == 'бумага'):
        print('раунд выигран')
        player_victories += 1

    print(f'Счет: player: {player_victories} - bot: {bot_victories}')


print('Вы победили') if player_victories > bot_victories else print('Вы проиграли')
