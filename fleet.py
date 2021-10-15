
from random import choice
from robot import Robot
from weapon import Weapons
from random import randint    
class Fleet:
    def __init__(self):
        self.fleet_list = []
        fleet_list = []

    def create_fleet (self):
            weapon_choices = ('Shocky Monkey', 'Laser Cannon', 'Potato')
            robot_one = Robot ('James', 100, Weapons(weapon= choice(weapon_choices),attack_power=randint(1,10)))
            robot_two = Robot ('1337Z0R', 100, Weapons(weapon= choice(weapon_choices),attack_power=randint(1,10)))
            robot_three = Robot ('Cuddlefloofy', 100, Weapons(weapon= choice(weapon_choices),attack_power=randint(1,10)))
            self.fleet_list.append (robot_one)
            self.fleet_list.append (robot_two)
            self.fleet_list.append (robot_three)