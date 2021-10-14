from fleet import Fleet
from herd import Herd
from battlefield import Battlefield
from dinosaur import Dinosaur
import time


robot_group = Fleet()  
robot_group.create_fleet()

dino_group = Herd()
dino_group.create_herd()

#

# #attacked_robot = robot_group[0]

# while robot_group.fleet_list != [] and dino_group.herd_list != []:
#     if robot_group.fleet_list[0].health <= 0:
#         del robot_group.fleet_list[0]
#     if dino_group.herd_list[0].health <= 0:
#         del dino_group.herd_list[0]
#     else:
#         robot_group.fleet_list[0].health > 0 and dino_group.herd_list[0] > 0
#         dino_group.herd_list[0].dino_attack(robot_group.fleet_list[0])
#         robot_group.fleet_list[0].robot_attack(dino_group.herd_list[0])
#     print('You have '  + len(robot_group.fleet_list) + 'robots left')
for i in robot_group.fleet_list:
    print ((f'You have ') + len(dino_group.herd_list) + ('dinosaurs left'))
    print (f'You have ') + len(robot_group.herd_list) + ('robots left')
    print((robot_group.fleet_list[i]) + (robot_group.fleet_list[i].health) )
    time.sleep(5)
    print (dino_group.herd_list.name + 'has' + dino_group.herd_list.health + 'left')
    time.sleep(5)

    

# if robot_group[0].health > 0:
#     attacked_robot = robot_group[0]
#     dino_attack.robot_group[0]
    





# print (dino_group)
# print (robot_group)

