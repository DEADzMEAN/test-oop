import person
import reid_boss

print("тестируем ооп")

characters = [
    person.Warrior(name="Тиран", hp=200, defence=100, speed=20, power=25, attack_speed=25),
    person.Mage(name="Arhimage", hp=100, defence=50, speed=15, intellect=150, attack_speed=244, power=1),
    person.Saport(name="Bishop", hp=50, defence=15, speed=15, attack_speed=10, power=1),
    person.Tank(name='Василий', hp=500, defence=200, speed=18, attack_speed=20, power=9)
]

rb = [
    reid_boss.ReidBoss(name="Stone_Golem", hp=1500, defence=500, speed=1, attack_speed=15, skill_name='Power scream', skill=500, power=100)
]

def checked_input(prompt: str):
    value = int(input(prompt))
    if value > 4:
        print("нет таких бойцов")
        exit(0)

    return value


for i in range(len(characters)):
    print("Боец ", i + 1, ": ", characters[i], sep='')

choice = input('1 - pwp \n 2 - Going on a boss raid \n input - ')

def choice_pvp(choice):
    if choice == 1:
        first = checked_input("Выбери бойца №1: ")
        second = checked_input("Выбери бойца №2: ")
        char1 = characters[first - 1]
        char2 = characters[second - 1]
        return char1, char2
    if choice == 2:
        print('Выбери игроков в пати \n Ты можешь выдрать трёх персонажей для борьбы с коварным РБ')
        first = checked_input("Выбери бойца №1: ")
        second = checked_input("Выбери бойца №2: ")
        third = checked_input("Выбери бойца №3: ")
        char1 = characters[first - 1]
        char2 = characters[second - 1]
        char3 = characters[third - 1]
        return char1, char2, char3

def

choice_pvp(choice).char1.scream()    # да хуй его маму знает. по наитию думаю что так...
char2.scream()
print("DPS first to second:", char1.get_dpm(char2))
print("DPS second to first:", char2.get_dpm(char1))
print(choice_pvp(choice), person.Character.fight(char1, char2))
