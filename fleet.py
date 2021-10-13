
from robot import Robot
from weapons import Weapons
class Fleet:
    def __init__(self):
        self.fleet_list = []
        

    def create_fleet (self):
        robot_one = Robot ('Jim_Bob', 100, Weapons('shocky_stick', 10))
        robot_two = Robot ('Bubba_Fred', 100, Weapons('shocky_stick', 10))
        robot_three = Robot ('James', 100, Weapons('shocky_stick', 10))
        self.fleet_list.append (robot_one)
        self.fleet_list.append (robot_two)
        self.fleet_list.append (robot_three)