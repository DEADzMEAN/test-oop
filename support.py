from character import Character


class Support(Character):
    def __init__(self, name, hp, defence, speed, attack_speed, heal_power, buff, power):
        Character.__init__(self, name, hp, defence, attack_speed, speed, power)
        self.heal_power = heal_power
        self.buff = buff

    def scream(self):
        print(">>>накладываю бафы<<<")

    def heal(self, other):
        for i in range(2):
            other.hp += self.heal_power

    def baf(self, other):
        other.defence += 30
        print(f'{other.name} дарую тебе +30 к защите!')
        other.attack_speed += 10
        print(f'{other.name} сейчас бафну и будешь атаковать шустрее, а то как лох.')

    def berserk(self, other):
        print('Хочешь силу берсерка воин? - она сделает тебя сильнее но ты жертвуешь жизнью...')
        
        # ебётся с аргументом Yy d 110 строке когда ставлю проверку (надобы указать тип стринг наверно)
        bers = input('Y=1/N=0 ')  
        if bers == 1 or bers == 0:
            other.hp -= (100 - 15) * other.hp // 100  # ну такой наивный способ вычесть 15%
            print('ты лишился 15% НР')
            other.defence += (100 + 50) * other.defence // 100
            print('Получил +50% к защите')
            other.attack_speed += (100 + 15) * other.attack_speed // 100
