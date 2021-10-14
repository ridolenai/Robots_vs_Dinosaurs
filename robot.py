
from fleet import Fleet
from herd import Herd
from weapon import Weapons

class Robot:
    def __init__(self, name, health, weapon, attack_power):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.attack_power = attack_power
    

    def robot_attack (self,robot):
        self.robot = robot
        