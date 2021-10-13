from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
from robot import Robot
from weapons import Weapons
fleet = []
herd = []

robot_one = Robot ('Jim_Bob', 100, 'stabby_stick')
robot_two = Robot ('Bubba_Fred', 100, 'stabby_stick')
robot_three = Robot ('James', 100, "stabby_stick")

fleet.append (robot_one)
fleet.append (robot_two)
fleet.append (robot_three)

dino_one = Dinosaur ('Jaws', 100, 'bitey_mouth')
dino_two = Dinosaur ('Teeth', 100, 'bitey_mouth')
dino_three = Dinosaur('Roger', 100, 'bitey_mouth')
herd.append (dino_one)
herd.append (dino_two)
herd.append (dino_three)


print (herd)
print (fleet)

