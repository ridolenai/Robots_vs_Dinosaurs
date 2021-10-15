import random
from random import choice
from random import randint





class Weapons:
    def __init__(self, weapon, attack_power):
        self.name = weapon
        self.attack_power = attack_power
        weapon_choices = ('Shocky Monkey', 'Laser Cannon', 'Potato')
        #attack_power = randint (1,10)
        weapon = choice (weapon_choices)
        
        


        

