from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
from robot import Robot
from weapons import Weapons


robot_group = Fleet()  
robot_group.create_fleet()

dino_one = Dinosaur ('Jaws', 100, 'bitey_mouth')
dino_two = Dinosaur ('Teeth', 100, 'bitey_mouth')
dino_three = Dinosaur('Roger', 100, 'bitey_mouth')
herd.append (dino_one)
herd.append (dino_two)
herd.append (dino_three)


print (herd)
print (robot_group)

