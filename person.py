

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
            #if self.name == 'Василий':
            #    stronghold(self)
            #if other.name == 'Василий':
            #    stronghold(other)
        return "подибил боец {}".format(other.name if self.hp <= 0 else self.name)

    def __str__(self):
        return "Character with name: " + self.name  # none эта не стринга! сделай стрингой тогда покажет метод str

    def party(self):
        print('введите трёх персонажей для пати на РБ')
        print('1 - Воин \n 2- Маг \n 3- Сапорт хиллир \n 4- Танк')
        # продолжаю обдумывать это дерьмище



class Warrior(Character):
    def __init__(self, name, hp, defence, speed, power, attack_speed):
        Character.__init__(self, name, hp, defence, speed, attack_speed, power)

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
    def __init__(self, name, hp, defence, speed, attack_speed, intellect, power):
        Character.__init__(self, name, hp, defence, attack_speed, speed, power)
        self.intellect = intellect

    def scream(self):
        print("...шепчет заклинания...")

    def get_dpm(self, other: Character) -> int:
        return self.intellect / other.defence


class Saport(Character):
    def __int__(self, name, hp, defence, speed, attack_speed, hill_power, baff, power):
        Character.__init__(self, name, hp, defence, attack_speed, speed, power)
        self.hill_power = hill_power
        self.baff = baff

    def scream(self):
        print(">>>накладываю бафы<<<")

    def hill(self, other):
        for i in range(2):
            other.hp += self.hill_power

    def baf(self, other):
        other.defence += 30
        print(f'{other.name} дарую тебе +30 к защите!')
        other.attack_speed += 10
        print(f'{other.name} сейчас бафну и будешь атаковать шустрее, а то как лох.')

    def berserk(self, other):
        print('Хочешь силу берсерка воин? - она сделает тебя сильнее но ты жертвуешь жизнью...')
        bers = input('Y=1/N=0 ')                     # ебётся с аргументом Yy d 110 строке когда ставлю проверку (надобы указать тип стринг наверно)
        if bers == 1 or bers == 0:
            other.hp -= (100 - 15) * other.hp // 100  # ну такой наивный способ вычесть 15%
            print('ты лишился 15% НР')
            other.defence += (100 + 50) * other.defence // 100
            print('Получил +50% к защите')
            other.attack_speed += (100 + 15) * other.attack_speed // 100

class Tank(Character):
    def __int__(self, name, hp, defence, speed, attack_speed, power, agression):
        Character.__init__(self, name, hp, defence, attack_speed, speed, power)
        self.power = power
        self.agression = agression

    def stronghold(self):
        if self.hp <= (100 - 30) * self.hp // 100:
            self.defence += (100 + 100) * self.hp // 100
            print('Враг обломает об меня зубы! Я ТВЕРДЫНЯ!')


    def get_dpm(self, other: Character) -> int:
        return self.power / other.defence
