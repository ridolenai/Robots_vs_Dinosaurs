from weapon import Weapons
from robot import Robot
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self, fleet, herd):
        self.fleet = fleet 
        self.herd = herd
        
    def run_game(self):
        print ('I want to play a game.')


    def display_welcome(self):
        print ('I want to play a game.')
        print ('You do not have a choice.  You must also play')
        print ('Welcome to Robots vs Dinosaurs, a great new...')
        print ('Who am I kidding.  This is going to be awful.  ')

    def battle(self):
        pass

    def dino_turn(self,dinosaur):
        for i in Herd:
            if i.health >= (0):
                robot_attack
            pass

    def robo_turn(self,robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass
