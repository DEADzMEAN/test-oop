class ReidBoss:
    def __init__(self, name, power, hp, defence, speed, attack_speed, skill_name, skill):
        self.name = name
        self.power = power
        self.hp = hp
        self.defence = defence
        self.speed = speed
        self.attack_speed = attack_speed
        self.skill = skill
        self.skill_name = skill_name

    def monolog(self):
        print('Вы чё ахуели, зачем припёрлись ко мне?! Проблемы ищите? Здоровья вагон?! - ну сейчас я мигом разгужу...')

    def fight_skill(self, other):
        if self.hp < 100:
            other.hp -= self.skill / other.defence
            print('Предсмертный рёв!... - Вокруг всё начинает вибрировать и гудеть как будто наши герои оказалисьж')
            print(' в трансформаторной будке. Кажется сейчас  что то произойдёт')
            print('5 \n 4 \n 3 \n 2 \n 1 \n _____БУУУУМ____')


rb = (
    ReidBoss(name="Stone_Golem", hp=1500, defence=500, speed=1, attack_speed=15, skill_name='Power scream', skill=500, power=100)

)