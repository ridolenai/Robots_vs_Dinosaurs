
class Robot:
    def __init__(self, name, health, weapon, attack_power):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.attack_power = attack_power
    from weapons import Weapons

    def robot_attack (self,dinosaur):
        self.dinosaur = dinosaur
        