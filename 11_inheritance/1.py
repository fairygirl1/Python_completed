"""
 Добавьте на основании классов из презентации класс Magician который наследует Hero.
  Со своими методами hello и atack.
 """


class Hero():
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        print('Поприветствуйте героя ->', self.name)
        print('Уровень здоровья:', self.health)
        print('Класс брони:', self.armor)
        print('Сила удара:', self.power)
        print('Оружие:', self.weapon)


class Magician(Hero):
    def hello(self):
        super().print_info()
        print('Good luck with your hunger games')

    def attack(self, knight):
        print(self.name, 'hits', knight.name)
        knight.health -= 50
        self.armor += 100


Daemon = Magician('Daemon', 10, 10, 10, 'knife')
knight = Hero('Leopold', 50, 25, 20, 'maheta')
Daemon.hello()

Magician.attack(Daemon, knight)
print(knight.health)
print(Daemon.armor)