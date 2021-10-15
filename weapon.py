

import random
from random import choice
from random import randint




#creates weapons 
class Weapons:
    def __init__(self, weapon, attack_power):
        self.name = weapon
        self.attack_power = attack_power
        weapon_choices = ('Shocky Monkey', 'Laser Cannon', 'Potato')
        weapon = choice (weapon_choices)
        
        


        

