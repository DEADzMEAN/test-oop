class Character:
    def __init__(self, name, hp, defence, speed, attack_speed, power):
        self.name = name
        self.hp = hp
        self.defence = defence
        self.speed = speed
        self.attack_speed = attack_speed
        self.power = power

    def scream(self):
        print("В акаку!")

    def should_leave(self, other) -> bool:
        return self.hp < (other.get_dpm(self) * other.attack_speed)

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
            # if self.name == 'Василий':
            #    stronghold(self)
            # if other.name == 'Василий':
            #    stronghold(other)
        return "подибил боец {}".format(other.name if self.hp <= 0 else self.name)

    def __str__(self):
        return "Character with name: " + self.name  # none эта не стринга! сделай стрингой тогда покажет метод str

    def party(self):
        print('введите трёх персонажей для пати на РБ')
        print('1 - Воин \n 2- Маг \n 3- Сапорт хиллир \n 4- Танк')
        # продолжаю обдумывать это дерьмище
