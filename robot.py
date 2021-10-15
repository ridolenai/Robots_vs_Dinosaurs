
from random import random
from random import choice

from weapon import Weapons

#creates robots and defines their attack ability
class Robot:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
        weapon_choices = ('Shocky Monkey', 'Laser Cannon', 'Potato')
        weapon = choice (weapon_choices)
        
    

    def robot_attack (self, dino):
        dino.health -= self.weapon.attack_power
        

        

        