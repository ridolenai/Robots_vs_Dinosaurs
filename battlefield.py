

from fleet import Fleet
from herd import Herd
import time

#Instantiates the fleet for the robots and the herd for the dinos
robot_group = Fleet()  
robot_group.create_fleet()
dino_group = Herd()
dino_group.create_herd()

#forms the Battlefield class which holds the functions for the game to run.
class Battlefield:
    def __init__(self, fleet, herd):
        self.fleet = fleet 
        self.herd = herd
        
    def display_welcome(self):  #Welcomes the user to the game and introduces what it is.
        print ('I want to play a game.')
        print ('You do not have a choice.  You must also play')
        print ('Welcome to Robots vs Dinosaurs, a great new...')
        print ('Who am I kidding.  This is going to be awful, but you will do it anyway because the game plays itself. ')
        print ("I'm like WOPR's annoying, slighty less intelligent cousin.  Well, enjoy the 'game' we are playing.")
        print ("Also, just a heads up, there is probably a very small, but still non-zero, chance the world may blow up.  I'm not smart, don't ask me.")
        time.sleep(15)

    def battle(self):  #completes the epic genocidal battle between the last remaining dinosaurs and sentient robots
        while robot_group.fleet_list != [] and dino_group.herd_list != []:
            if robot_group.fleet_list[0].health <= 0:
                del robot_group.fleet_list[0]
            if robot_group.fleet_list == []: #Checks to see if there are more robots.  If not then the dinosaurs win and the game ends.
                print ('The dinosaurs have won') 
                break
            if dino_group.herd_list[0].health <= 0:
                del dino_group.herd_list[0]
                if dino_group.herd_list == []:  #Checks to see if there are more dinosaurs.  If not then the robots win and the game ends.
                    print ('The robots have won')
                    break
            if robot_group.fleet_list != []:
                dino_group.herd_list[0].dino_attack(robot_group.fleet_list[0])
                robot_group.fleet_list[0].robot_attack(dino_group.herd_list[0])
            
            print (f'You have {len(robot_group.fleet_list)} robots left')
            for robot in robot_group.fleet_list:
                print (f' {(robot.name)} has {(robot.health)} health left')
            time.sleep(1)
            print (f'You have {len(dino_group.herd_list)} dinosaurs left')
            for dino in dino_group.herd_list:
                print (f' {(dino.name)} has {(dino.health)} health left')
            time.sleep(1)