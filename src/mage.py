from src.character import Character


class Mage(Character):
    def __init__(self, name, hp, defence, speed, attack_speed, intellect, power):
        Character.__init__(self, name, hp, defence, attack_speed, speed, power)
        self.intellect = intellect

    def scream(self):
        print("...шепчет заклинания...")

    def get_dpm(self, other: Character) -> int:
        return self.intellect / other.defence
