from re import S
import numpy as np
import colorama
from colorama import Fore, Back, Style
from os import system
from input import *
import math
from time import time as current_time


class building():
    def __init__(self, x, y, colorpoints):
        self.xcoord = x
        self.ycoord = y
        self.colorpoints = colorpoints


class Walls():
    def __init__(self, x, y, colorpoints):
        self.xcoord = x
        self.ycoord = y
        self.height = 2
        self.width = 2
        self.count = 100
        self.bgcolor = Back.BLUE+' '+Style.RESET_ALL
        self.health = 20
        self.colorpoints = colorpoints
        self.isdamage = 0
        self.isattack = 0


class Cannon():
    def __init__(self, x, y, colorpoints):
        building.__init__(self, x, y, colorpoints)
        self.height = 2
        self.width = 2
        self.bgcolor = Back.MAGENTA+' '+Style.RESET_ALL
        self.damage = 2
        self.range = 5
        self.isdamage = 0
        self.time = 0
        self.health = 20
        self.isattack = 0


class Troops():
    def __init__(self, x, y, hitpoints):
        self.xcoord = x
        self.ycoord = y
        self.height = 2
        self.width = 2
        self.bgcolor = Back.BLACK+' '+Style.RESET_ALL
        self.hitpoints = hitpoints
        self.damage = 5
        self.status = 0
        self.isdamage = 0
        self.speed = 1
        self.rage_spell = 0
        self.heal_spell = 0
        self.isattack = 0


class Town_Hall(building):
    def __init__(self, x, y, colorpoints):
        building.__init__(self, x, y, colorpoints)
        self.height = 4
        self.width = 3
        self.bgcolor = Back.GREEN+' '+Style.RESET_ALL
        self.health = colorpoints
        self.isdamage = 0
        self.isattack = 0


class Huts():
    def __init__(self, x, y, colorpoints):
        building.__init__(self, x, y, colorpoints)
        self.height = 2
        self.width = 2
        self.bgcolor = Back.GREEN+' '+Style.RESET_ALL
        self.health = colorpoints
        self.isdamage = 0
        self.isattack = 0


class Archers():
    def __init__(self, x, y, hitpoints):
        self.xcoord = x
        self.ycoord = y
        self.height = 2
        self.width = 2
        self.bgcolor = Back.LIGHTYELLOW_EX+' '+Style.RESET_ALL
        self.hitpoints = hitpoints
        self.damage = 2.5
        self.status = 0
        self.isdamage = 0
        self.speed = 1
        self.rage_spell = 0
        self.heal_spell = 0
        self.isattack = 0
        self.range = 10


class Balloons():
    def __init__(self, x, y, hitpoints):
        self.xcoord = x
        self.ycoord = y
        self.height = 2
        self.width = 2
        self.bgcolor = Back.LIGHTYELLOW_EX+' '+Style.RESET_ALL
        self.hitpoints = hitpoints
        self.damage = 10
        self.status = 0
        self.isdamage = 0
        self.speed = 1
        self.rage_spell = 0
        self.heal_spell = 0
        self.isattack = 0
        self.range = 6


class WizardTower():
    def __init__(self, x, y, colorpoints):
        building.__init__(self, x, y, colorpoints)
        self.height = 2
        self.width = 2
        self.bgcolor = Back.LIGHTBLUE_EX+' '+Style.RESET_ALL
        self.damage = 2
        self.range = 5
        self.isdamage = 0
        self.time = 0
        self.health = colorpoints
        self.isattack = 0
