

from random import randint


class Weapons:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        attack_power = randint(5,10)

