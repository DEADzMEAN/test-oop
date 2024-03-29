from warrior import Warrior
from core.mage import Mage
from support import Support
from tank import Tank

import reid_boss

print("тестируем ооп")

characters = [
    Warrior(name="Тиран", hp=200, defence=100, speed=20, power=25, attack_speed=25),
    Mage(name="Arhimage", hp=100, defence=50, speed=15, intellect=150, attack_speed=244, power=1),
    Support(name="Bishop", hp=50, defence=15, speed=15, attack_speed=10, heal_power=1, buff=1, power=1),
    Tank(name='Василий', hp=500, defence=200, speed=18, attack_speed=20, aggression=1, power=9)
]

rb = [
    reid_boss.ReidBoss(name="Stone_Golem", hp=1500, defence=500, speed=1, attack_speed=15, skill_name='Power scream',
                       skill=500, power=100)
]


def checked_input(prompt: str):
    value = int(input(prompt))
    if value > 4:
        print("нет таких бойцов")
        exit(0)

    return value


for i in range(len(characters)):
    print("Боец ", i + 1, ": ", characters[i], sep='')

choice: int = int(input('1 - PvP\n2 - Going on a boss raid\nChoose your destiny: '))


def choice_pvp():
    first = checked_input("Выбери бойца №1: ")
    second = checked_input("Выбери бойца №2: ")
    char1 = characters[first - 1]
    char2 = characters[second - 1]
    return char1, char2


def choice_raid():
    print('Выбери игроков в пати\nТы можешь выбрать трёх персонажей для борьбы с коварным РБ')
    first = checked_input("Выбери бойца №1: ")
    second = checked_input("Выбери бойца №2: ")
    third = checked_input("Выбери бойца №3: ")
    char1 = characters[first - 1]
    char2 = characters[second - 1]
    char3 = characters[third - 1]
    return char1, char2, char3


if choice == 1:
    char1, char2 = choice_pvp()
    char1.scream()
    char2.scream()
    print("DPS first to second:", char1.get_dpm(char2))
    print("DPS second to first:", char2.get_dpm(char1))
    char1.fight(char2)
    exit(0)

if choice == 2:
    chars = choice_raid()
    for char in chars:
        char.scream()

    exit(0)
