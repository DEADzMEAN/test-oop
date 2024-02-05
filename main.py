print("тестируем ооп")


class Character:
    def __init__(self, name, hp, defence, speed, attack_speed, dick=None):
        self.name = name
        self.hp = hp
        self.defence = defence
        self.speed = speed
        self.attack_speed = attack_speed
        self.dick = dick

    def _scream(self):
        print("В акаку!")

    def should_leave(self, other) -> bool:
        return self.hp < (other.get_dpm(self) * other.speed)

    def can_leave(self, other) -> bool:
        return self.speed >= other.speed

    def get_dpm(self, other) -> int:
        return 0

    def __eq__(self, other):
        if self.name == other.name:
            print("В топку клонов!")
            return True
        if self.hp == other.hp and self.defence == other.defence and self.speed == other.speed:
            print("Теорема Эскобара")
            return True
        return False

    def fight(self, other):
        if self.should_leave(other):
            print(self.name, "пытается трусливо свалить поджав хвост ибо зассал")
            if self.can_leave(other):
                print(self.name, "пятки мелькают вдалеке, это ссыкло уже не догнать")
            else:
                print(self.name, "зассал, пытался бежать, но даже это не смог сделать нормально ибо лох")
            return

        while self.hp > 0 and other.hp > 0:
            self.hp -= other.get_dpm(self) * other.attack_speed
            print(f"Боец {other.name} ебашит по щщам и у {self.name} остаётся {self.hp} HP")
            other.hp -= self.get_dpm(other) * self.attack_speed
            print(self.name, " кидает в ответ плюху и осталось y", other.name, other.hp, " HP")

        return "подибил боец {}".format(other.name if self.hp <= 0 else self.name)

    def __str__(self):
        return "Character with name: " + self.name + ", dick: " + str(self.dick) #none эта не стринга! сделай стрингой тогда покажет метод str


class Warrior(Character):
    def __init__(self, name, hp, defence, speed, power, attack_speed, dick):
        Character.__init__(self, name, hp, defence, speed, attack_speed, dick)
        self.power = power
        self.dick = dick

    def scream(self):
        if self.power > 10:
            print("Нагибаем!")
        else:
            Character._scream(self)

    def get_dpm(self, other: Character) -> int:
        return self.power / other.defence

    def __str__(self):
        return "Warrior with name: " + self.name


class Mage(Character):
    def __init__(self, name, hp, defence, speed, attack_speed, intellect):
        Character.__init__(self, name, hp, defence, attack_speed, speed)
        self.intellect = intellect

    def scream(self):
        print("...шепчет заклинания...")

    def get_dpm(self, other: Character) -> int:
        return self.intellect / other.defence


def checked_input(prompt: str):
    value = int(input(prompt))
    if value > 2:
        print("нет таких бойцов")
        exit(0)

    return value


characters = (
    Warrior(name="Гнида из 10 квартиры", hp=100, defence=50, speed=20, power=9, attack_speed=50, dick=11),
    Mage(name="Arhimage", hp=100, defence=50, speed=15, intellect=100, attack_speed=20),
)

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
print(Character.fight(char1, char2))
