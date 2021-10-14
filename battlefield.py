from weapon import Weapons
from robot import Robot
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
import time
class Battlefield:
    def __init__(self, fleet, herd):
        self.fleet = fleet 
        self.herd = herd
        
    def run_game(self):
        print ('I want to play a game.')
        time.sleep(2)
        

    def display_welcome(self):
        print ('I want to play a game.')
        print ('You do not have a choice.  You must also play')
        print ('Welcome to Robots vs Dinosaurs, a great new...')
        print ('Who am I kidding.  This is going to be awful.  ')
        time.sleep(5)

    def battle(self):
        pass

    def dino_turn(self,dinosaur):
        pass        

    def robo_turn(self,robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass
