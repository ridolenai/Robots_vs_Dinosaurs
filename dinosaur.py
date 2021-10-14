
class Dinosaur:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon

    def dino_attack(self, robot):
        robot.health -= self.weapon.attack_power
        
