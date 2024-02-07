import person
import reid_boss

print("тестируем ооп")

characters = [
    person.Warrior(name="Тиран", hp=200, defence=100, speed=20, power=25, attack_speed=25),
    person.Mage(name="Arhimage", hp=100, defence=50, speed=15, intellect=150, attack_speed=244, power=1),
    person.Saport(name="Bishop", hp=50, defence=15, speed=15, attack_speed=10, power=1),
    person.Tank(name='Василий', hp=500, defence=200, speed=18, attack_speed=20, power=9)
]


def checked_input(prompt: str):
    value = int(input(prompt))
    if value > 4:
        print("нет таких бойцов")
        exit(0)

    return value


for i in range(len(characters)):
    print("Боец ", i + 1, ": ", characters[i], sep='')

first = checked_input("Выбери бойца №1: ")
second = checked_input("Выбери бойца №2: ")
char1 = characters[first - 1]
char2 = characters[second - 1]

char1.scream()
char2.scream()
print("DPS first to second:", char1.get_dpm(char2))
print("DPS second to first:", char2.get_dpm(char1))
print(person.Character.fight(char1, char2))
