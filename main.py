from fleet import Fleet
from herd import Herd
from battlefield import Battlefield
from dinosaur import Dinosaur
import time


robot_group = Fleet()  
robot_group.create_fleet()

dino_group = Herd()
dino_group.create_herd()



while robot_group.fleet_list != [] and dino_group.herd_list != []:
    if robot_group.fleet_list[0].health <= 0:
        del robot_group.fleet_list[0]
    if dino_group.herd_list[0].health <= 0:
        del dino_group.herd_list[0]
    else:
        dino_group.herd_list[0].dino_attack(robot_group.fleet_list[0])
        if robot_group.fleet_list == []:
            print ('The dinosaurs have won.')
            break
        else:
            robot_group.fleet_list[0].robot_attack(dino_group.herd_list[0])
            if dino_group.herd_list == []:
                print ('The robots have won')
                break
    print (f'You have {len(robot_group.fleet_list)} robots left')
    for robot in robot_group.fleet_list:
        print (f' {(robot.name)} has {(robot.health)} health left')
        #time.sleep(5)
    print (f'You have {len(dino_group.herd_list)} dinosaurs left')
    for dino in dino_group.herd_list:
        print (f' {(dino.name)} has {(dino.health)} health left')

    


