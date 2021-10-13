
class Robot:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
    from weapons import Weapons

    def robot_attack (self, name_weapon, attack_power):
        self.name_weapon = name_weapon
        self.attack_power = attack_power
        pass