from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
from robot import Robot
from weapons import Weapons


robot_group = Fleet()  
robot_group.create_fleet()

dino_group = Herd()
dino_group.create_herd()


print (dino_group)
print (robot_group)

