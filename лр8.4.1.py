import random

answers = ['Нормально', 'Лучше всех :)', 'Ну так себе', 'Отличненько!', 'Ничего, жить буду']

def how_are_you():
    return random.choice(answers)

print(how_are_you())
