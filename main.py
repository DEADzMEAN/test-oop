import person
import reid_boss


print("тестируем ооп")





def checked_input(prompt: str):
    value = int(input(prompt))
    if value > 2:
        print("нет таких бойцов")
        exit(0)

    return value




for i in range(len(person.characters)):
    print("Боец ", i + 1, ": ", person.characters[i], sep='')

first = checked_input("Выбери бойца №1: ")
second = checked_input("Выбери бойца №2: ")
char1 = person.characters[first - 1]
char2 = person.characters[second - 1]

char1.scream()
char2.scream()
print("DPS first to second:", char1.get_dpm(char2))
print("DPS second to first:", char2.get_dpm(char1))
print(person.Character.fight(char1, char2))
