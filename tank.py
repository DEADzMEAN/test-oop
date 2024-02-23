from character import Character


class Tank(Character):
    def __init__(self, name, hp, defence, speed, attack_speed, power, aggression):
        Character.__init__(self, name, hp, defence, attack_speed, speed, power)
        self.power = power
        self.aggression = aggression

    def stronghold(self):
        if self.hp <= (100 - 30) * self.hp // 100:
            self.defence += (100 + 100) * self.hp // 100
            print('Враг обломает об меня зубы! Я ТВЕРДЫНЯ!')

    def get_dpm(self, other: Character) -> int:
        return self.power / other.defence
