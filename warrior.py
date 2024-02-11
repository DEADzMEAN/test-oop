from character import Character


class Warrior(Character):
    def __init__(self, name, hp, defence, speed, power, attack_speed):
        Character.__init__(self, name, hp, defence, speed, attack_speed, power)

    def scream(self):
        if self.power > 10:
            print("Нагибаем!")
        else:
            Character.scream(self)

    def get_dpm(self, other: Character) -> int:
        return self.power / other.defence

    def __str__(self):
        return "Warrior with name: " + self.name
