from fleet import Fleet
from herd import Herd
from battlefield import Battlefield
from dinosaur import Dinosaur



robot_group = Fleet()  
robot_group.create_fleet()

dino_group = Herd()
dino_group.create_herd()

dino_group.herd_list[0].dino_attack(robot_group.fleet_list[0])


for i in robot_group:
    if robot_group[0].health > (0):




print (dino_group)
print (robot_group)

