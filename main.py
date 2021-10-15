
#Class and necessary function imports
from fleet import Fleet
from herd import Herd
from battlefield import Battlefield

#Instantiates the fleet for the robots and the herd for the dinos
robot_group = Fleet()  
robot_group.create_fleet()

dino_group = Herd()
dino_group.create_herd()
#Battlefield.display_welcome()


Battlefield.display_welcome('')

Battlefield.battle('')





    


