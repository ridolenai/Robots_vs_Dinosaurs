

from random import randint


class Weapons:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power

    # def arm_yourself_robots(self, name_weapon, dmg_points):
    #     import random
    #     self.name_weapon = name_weapon
    #     self.dmg_points = int(dmg_points)
    #     print ('A weapon will now be randomly chosen:  ')
    #     weapon_choice = randint(1, 100)
    #     if weapon_choice <= 20:
    #         print ('You are unlucky.  You have to slap them.')
    #         print ('Slapping them only does 5 damage.  Good luck.')
    #         name_weapon ('slap', 5)
    #     elif weapon_choice <= 85:
    #         print ('I suppose I will give you a laser sword... this time')
    #         print ('Laser swords do 10 damage per hit.  You may be okay.')
    #         name_weapon ('laser sword', 10)
    #     else:
    #         print ('Dalek mode activated.  Exterminate, exterminate!')
    #         print ('Unless you are fighting the doctor, you will be fine.  25 damage per hit.')
    #         name_weapon ('Dalek mode', 25)
    #     input ('Press enter key when you are ready to proceed.')
