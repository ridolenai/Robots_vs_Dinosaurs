
class Robot:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
    

    def robot_attack (self, dino):
        dino.health -= self.weapon.attack_power
        

        

        