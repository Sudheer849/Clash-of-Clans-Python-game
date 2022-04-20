from re import S
import numpy as np
import colorama
from colorama import Fore, Back, Style
from os import system
from input import *
import math
from time import time as current_time
from input import *
class Queen():
    def __init__(self, x, y):
        self.xcoord = x
        self.ycoord = y
        self.height = 2
        self.width = 2
        self.damage = 4
        self.xsize = 100
        self.ysize = 50
        self.range = 5
        self.bgcolor = Back.RED+' '+Style.RESET_ALL
        self.health = 20
        self.maxhealth = 20
        self.healthbar = [
            [self.bgcolor for i in range(200)] for j in range(200)]
        self.len = 30
        self.isdamage = 0
        self.speed = 1
        self.rage_spell = 0
        self.heal_spell = 0
        self.range = 5
        self.previous_move = 'W'
        self.times = np.zeros(100, dtype=np.double)
        self.time_count = 0
        self.attack_count = 0
        self.target_rows = []
        self.target_cols = []
        self.qa = np.zeros(100, dtype=int)

    def move_queen(self, char, array):
     #      print(char)
        if char == 'W' and self.ycoord > 0 and array[self.ycoord-self.speed][self.xcoord] != 1 and array[self.ycoord-self.speed][self.xcoord + self.speed] != 1:
            self.ycoord = self.ycoord - self.speed
            self.previous_move = 'W'
        elif char == 'S' and array[self.ycoord + self.height][self.xcoord] != 1 and array[self.ycoord + self.height][self.xcoord + self.speed] != 1:
            self.ycoord = self.ycoord + self.speed
            self.previous_move = 'S'
        elif char == 'A' and self.xcoord > 0 and array[self.ycoord][self.xcoord - self.speed] != 1 and array[self.ycoord + self.speed][self.xcoord - self.speed] != 1:
            self.xcoord = self.xcoord - self.speed
            self.previous_move = 'A'
        elif char == 'D' and array[self.ycoord][self.xcoord + self.width] != 1 and array[self.ycoord+1][self.xcoord + self.width] != 1:
            self.xcoord = self.xcoord + self.speed
            self.previous_move = 'D'
        elif char == 'q':
            return True