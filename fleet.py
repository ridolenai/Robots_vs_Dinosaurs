
from random import choice
from robot import Robot
from weapon import Weapons
from random import randint    

#creates robot fleet
class Fleet:
    def __init__(self):
        self.fleet_list = []

    def create_fleet (self):
            weapon_choices = ('Shocky Monkey', 'Laser Cannon', 'Potato')  #allows robot to be randomly assigned a weapon
            robot_one = Robot ('James', 100, Weapons(weapon= choice(weapon_choices),attack_power=randint(5,15)))
            robot_two = Robot ('1337Z0R', 100, Weapons(weapon= choice(weapon_choices),attack_power=randint(5,15)))
            robot_three = Robot ('Cuddlefloofy', 100, Weapons(weapon= choice(weapon_choices),attack_power=randint(5,15)))
            self.fleet_list.append (robot_one)
            self.fleet_list.append (robot_two)
            self.fleet_list.append (robot_three)