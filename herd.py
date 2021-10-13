
from dinosaur import Dinosaur
from weapons import Weapons
class Herd:
    def __init__(self):
        self.herd_list = []
        

    def create_herd (self):
        dino_one = Dinosaur ('Jaws', 100, Weapons('stabby_stick', 100))
        dino_two = Dinosaur ('Teeth', 100, Weapons('stabby_stick', 100))
        dino_three = Dinosaur('Roger', 100, Weapons('stabby_stick', 100))
        self.herd_list.append (dino_one)
        self.herd_list.append (dino_two)
        self.herd_list.append (dino_three)
