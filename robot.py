
from random import random
from random import choice

from weapon import Weapons


class Robot:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
        weapon_choices = ('Shocky Monkey', 'Laser Cannon', 'Potato')
        weapon = choice (weapon_choices)
        # weapon = Weapons()
    

    def robot_attack (self, dino):
        dino.health -= self.weapon.attack_power
        

        

        