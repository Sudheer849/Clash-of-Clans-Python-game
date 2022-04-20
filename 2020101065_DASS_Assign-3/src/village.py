from re import S
import numpy as np
import colorama
from colorama import Fore, Back, Style
from os import system
from input import *
import math
from time import time as current_time
from building import *
from king import *
from input import *
from queen import *


class Village():
    def __init__(self):
        self.rows = 50
        self.cols = 100
        self.background = Back.BLACK+' '+Style.RESET_ALL
        self.walls = np.zeros(200, dtype=Walls)
        self.king = King(75, 25)
        self.queen = Queen(75, 25)
        self.town_hall = Town_Hall(48, 24, 50)
        self.huts = np.zeros(5, dtype=Huts)
        self.huts[0] = Huts(10, 10, 20)
        self.huts[1] = Huts(94, 40, 20)
        self.huts[2] = Huts(30, 30, 20)
        self.huts[3] = Huts(6, 7, 20)
        self.huts[4] = Huts(15, 18, 20)
        self.cannons = np.zeros(2, dtype=Cannon)
        self.cannons[0] = Cannon(20, 20, 20)
        self.cannons[1] = Cannon(82, 35, 20)
        # build a np matrix
        self.troops = np.zeros((3, 2), dtype=Troops)
        self.troops[0] = np.zeros(2, dtype=Troops)
        self.troops[1] = np.zeros(2, dtype=Troops)
        self.troops[2] = np.zeros(2, dtype=Troops)
        self.archers = np.zeros((3, 1), dtype=Archers)
        self.archers[0] = np.zeros(1, dtype=Archers)
        self.archers[1] = np.zeros(1, dtype=Archers)
        self.archers[2] = np.zeros(1, dtype=Archers)
        self.balloons = np.zeros((3, 2), dtype=Balloons)
        self.balloons[0] = np.zeros(2, dtype=Balloons)
        self.balloons[1] = np.zeros(2, dtype=Balloons)
        self.balloons[2] = np.zeros(2, dtype=Balloons)
        self.troops_count = np.zeros(3, dtype=int)
        self.archers_count = np.zeros(3, dtype=int)
        self.balloons_count = np.zeros(3, dtype=int)
        self.wizardtowers = np.zeros(2, dtype=WizardTower)
        self.wizardtowers[0] = WizardTower(42, 32, 20)
        self.wizardtowers[1] = WizardTower(68, 20, 20)
        self.level = 0
        self.gameover = 0
        self.time = 0
        self.archertime = 0
        self.balloontime = 0
        self.variable = 'q'
        self.inputchar = 'v'

        self.status = np.zeros((50, 100), dtype=int)
        self.wallstatus = np.zeros((50, 100), dtype=int)
        self.defensivestatus = np.zeros((50, 100), dtype=int)

    def build_troops(self):
        for i in range(2):
            self.troops[0][i] = Troops(11, 14, 20)
            self.troops[1][i] = Troops(60, 45, 20)
            self.troops[2][i] = Troops(65, 28, 20)
        for i in range(3):
            self.troops_count[i] = 0

    def build_archers(self):
        for i in range(1):
            self.archers[0][i] = Archers(17, 25, 10)
            self.archers[1][i] = Archers(65, 35, 10)
            self.archers[2][i] = Archers(85, 25, 10)
        for i in range(3):
            self.archers_count[i] = 0

    def build_balloons(self):
        for i in range(2):
            self.balloons[0][i] = Balloons(10, 10, 20)
            self.balloons[1][i] = Balloons(90, 40, 20)
            self.balloons[2][i] = Balloons(30, 30, 10)
        for i in range(3):
            self.balloons_count[i] = 0

    def build_walls(self):
        xcoordinate = 0
        ycoordinate = 0
        for num in range(50):
            self.walls[num] = Walls(xcoordinate, ycoordinate, 20)
            xcoordinate = xcoordinate + self.walls[num].width
        xcoordinate = 0
        for num in range(25):
            self.walls[num+50] = Walls(xcoordinate, ycoordinate, 20)
            ycoordinate = ycoordinate + self.walls[num + 50].height
        xcoordinate = 98
        ycoordinate = 0
        for num in range(25):
            self.walls[num + 75] = Walls(xcoordinate, ycoordinate, 20)
            ycoordinate = ycoordinate + self.walls[num + 75].height
        ycoordinate = 48
        xcoordinate = 0
        for num in range(50):
            self.walls[num + 100] = Walls(xcoordinate, ycoordinate, 20)
            xcoordinate = xcoordinate + self.walls[num + 100].width
        xcoordinate = 25
        ycoordinate = 0
        for num in range(25):
            self.walls[num+150] = Walls(xcoordinate, ycoordinate, 20)
            ycoordinate = ycoordinate + self.walls[num + 25].width

    def print(self):
        system('clear')
        self.board = [[self.background for i in range(
            self.cols)] for j in range(self.rows+5)]
        # print walls
        for p in range(175):
            if self.walls[p].isdamage == 0:
                for row in range(self.walls[p].ycoord, self.walls[p].ycoord+self.walls[p].height):
                    for col in range(self.walls[p].xcoord, self.walls[p].xcoord+self.walls[p].width):
                        self.board[row][col] = self.walls[p].bgcolor
                        self.status[row][col] = 1
                        self.wallstatus[row][col] = 1
            else:
                for row in range(self.walls[p].ycoord, self.walls[p].ycoord+self.walls[p].height):
                    for col in range(self.walls[p].xcoord, self.walls[p].xcoord+self.walls[p].width):
                        self.board[row][col] = self.walls[p].bgcolor
                        self.status[row][col] = 0
                        self.wallstatus[row][col] = 0
        # print king
        if(self.variable == 'k'):
            if self.king.isdamage == 0:
                for row in range(self.king.ycoord, self.king.ycoord+self.king.height):
                    for col in range(self.king.xcoord, self.king.xcoord+self.king.width):
                        self.board[row][col] = self.king.bgcolor
            else:
                for row in range(self.king.ycoord, self.king.ycoord+self.king.height):
                    for col in range(self.king.xcoord, self.king.xcoord+self.king.width):
                        self.status[row][col] = 0
        if(self.variable == 'q'):
            if self.queen.isdamage == 0:
                for row in range(self.queen.ycoord, self.queen.ycoord+self.queen.height):
                    for col in range(self.queen.xcoord, self.queen.xcoord+self.queen.width):
                        self.board[row][col] = self.queen.bgcolor
            else:
                for row in range(self.queen.ycoord, self.queen.ycoord+self.queen.height):
                    for col in range(self.queen.xcoord, self.queen.xcoord+self.queen.width):
                        self.status[row][col] = 0
        # print health bar
        if self.variable == 'k':
            for row in range(51, 52):
                for col in range(10, 10+int(self.king.len)):
                    self.board[row][col] = self.king.bgcolor
            for row in range(51, 52):
                for col in range(10+int(self.king.len), 40):
                    self.board[row][col] = Back.WHITE + ' ' + Style.RESET_ALL
        elif(self.variable == 'q'):
            for row in range(51, 52):
                for col in range(10, 10+int(self.queen.len)):
                    self.board[row][col] = self.queen.bgcolor
            for row in range(51, 52):
                for col in range(10+int(self.queen.len), 40):
                    self.board[row][col] = Back.WHITE + ' ' + Style.RESET_ALL
        # print town hall
        if self.town_hall.isdamage == 0:
            for row in range(self.town_hall.ycoord, self.town_hall.ycoord+self.town_hall.height):
                for col in range(self.town_hall.xcoord, self.town_hall.xcoord+self.town_hall.width):
                    self.board[row][col] = self.town_hall.bgcolor
                    self.status[row][col] = 1
        else:
            for row in range(self.town_hall.ycoord, self.town_hall.ycoord+self.town_hall.height):
                for col in range(self.town_hall.xcoord, self.town_hall.xcoord+self.town_hall.width):
                    self.status[row][col] = 0

        # print huts
        for p in range(5):
            if self.huts[p].isdamage == 0:
                for row in range(self.huts[p].ycoord, self.huts[p].ycoord+self.huts[p].height):
                    for col in range(self.huts[p].xcoord, self.huts[p].xcoord+self.huts[p].width):
                        self.board[row][col] = self.huts[p].bgcolor
                        self.status[row][col] = 1
            else:
                for row in range(self.huts[p].ycoord, self.huts[p].ycoord+self.huts[p].height):
                    for col in range(self.huts[p].xcoord, self.huts[p].xcoord+self.huts[p].width):
                        self.status[row][col] = 0
        # print cannons
        for p in range(2):
            if self.cannons[p].isdamage == 0:
                for row in range(self.cannons[p].ycoord, self.cannons[p].ycoord+self.cannons[p].height):
                    for col in range(self.cannons[p].xcoord, self.cannons[p].xcoord+self.cannons[p].width):
                        self.board[row][col] = self.cannons[p].bgcolor
                        self.status[row][col] = 1
                        self.defensivestatus[row][col] = 1
            else:
                for row in range(self.cannons[p].ycoord, self.cannons[p].ycoord+self.cannons[p].height):
                    for col in range(self.cannons[p].xcoord, self.cannons[p].xcoord+self.cannons[p].width):
                        self.status[row][col] = 0
        # print wizard towers
        for p in range(2):
            if self.wizardtowers[p].isdamage == 0:
                for row in range(self.wizardtowers[p].ycoord, self.wizardtowers[p].ycoord+self.wizardtowers[p].height):
                    for col in range(self.wizardtowers[p].xcoord, self.wizardtowers[p].xcoord+self.wizardtowers[p].width):
                        self.board[row][col] = self.wizardtowers[p].bgcolor
                        self.status[row][col] = 1
                        self.defensivestatus[row][col] = 1
            else:
                for row in range(self.wizardtowers[p].ycoord, self.wizardtowers[p].ycoord+self.wizardtowers[p].height):
                    for col in range(self.wizardtowers[p].xcoord, self.wizardtowers[p].xcoord+self.wizardtowers[p].width):
                        self.status[row][col] = 0

        # barberians movement
        if(current_time() - self.time > 0.1):
            for num in range(3):
                var = 0
                for p in range(2):
                    min = -1
                    distance = -1
                    min_index = -1
                    flag = 0
                    if self.troops[num][p].status == 1:
                        if self.troops[num][p].isdamage == 0:
                            touch_row = -1
                            touch_col = -1

                            for row in range(self.troops[num][p].ycoord-1, self.troops[num][p].ycoord+self.troops[num][p].height + 1):
                                for col in range(self.troops[num][p].xcoord-1, self.troops[num][p].xcoord+self.troops[num][p].width+1):
                                    if self.wallstatus[row][col] == 1:
                                        touch_row = row
                                        touch_col = col
                                        flag = 1
                                        break
                                if flag == 1:
                                    break
                            if flag == 1:
                                flag = 0
                                for w in range(175):
                                    for row in range(self.walls[w].ycoord, self.walls[w].ycoord+self.walls[w].height):
                                        for col in range(self.walls[w].xcoord, self.walls[w].xcoord+self.walls[w].width):
                                            if row == touch_row and col == touch_col:
                                                self.walls[w].colorpoints = self.walls[w].colorpoints - \
                                                    self.troops[num][p].damage
                                                if self.walls[w].colorpoints <= 0:
                                                    self.walls[w].colorpoints = 0
                                                    self.walls[w].isdamage = 1
                                                    self.walls[w].bgcolor = Back.BLACK + \
                                                        ' '+Style.RESET_ALL
                                                    self.walls[w].isattack = 1
                                                    # make all the points lying in wall as wall status 0
                                                    for row in range(self.walls[w].ycoord, self.walls[w].ycoord+self.walls[w].height):
                                                        for col in range(self.walls[w].xcoord, self.walls[w].xcoord+self.walls[w].width):
                                                            self.wallstatus[row][col] = 0
                                                            self.status[row][col] = 0
                                                flag = 1
                                                break
                                        if flag == 1:
                                            break
                                    if flag == 1:
                                        break
                            if flag == 1:
                                var = 1
                                break

                            if flag == 0:
                                min = -1
                                min_index = -1
                                distance = -1
                                # check for huts
                                for r in range(5):
                                    if self.huts[r].isdamage == 0:
                                        distance = math.sqrt((self.huts[r].xcoord-self.troops[num][p].xcoord)**2 + (
                                            self.huts[r].ycoord-self.troops[num][p].ycoord)**2)
                                        if distance < min or min == -1:
                                            min = distance
                                            min_index = r
                                # check for cannons
                                for r in range(2):
                                    if self.cannons[r].isdamage == 0:
                                        distance = math.sqrt((self.cannons[r].xcoord-self.troops[num][p].xcoord)**2 + (
                                            self.cannons[r].ycoord-self.troops[num][p].ycoord)**2)
                                        if distance < min or min == -1:
                                            min = distance
                                            min_index = r+5
                                # check for townhall
                                if self.town_hall.isdamage == 0:
                                    distance = math.sqrt((self.town_hall.xcoord-self.troops[num][p].xcoord)**2 + (
                                        self.town_hall.ycoord-self.troops[num][p].ycoord)**2)
                                if distance < min or min == -1:
                                    min = distance
                                    min_index = 7
                                if(min_index == -1):
                                    exit()
                                if (min_index < 5 and min_index != 7):
                                    flag = 1
                                    for row in range(self.troops[num][p].ycoord-1, self.troops[num][p].ycoord+self.troops[num][p].height + 1):
                                        for col in range(self.troops[num][p].xcoord-1, self.troops[num][p].xcoord+self.troops[num][p].width+1):
                                            if self.status[row][col] == 1 and self.wallstatus[row][col] == 0:
                                                self.huts[min_index].colorpoints = self.huts[min_index].colorpoints - \
                                                    self.troops[num][p].damage
                                                if self.huts[min_index].colorpoints <= 0:
                                                    self.huts[min_index].colorpoints = 0
                                                    self.huts[min_index].isdamage = 1
                                                    self.huts[min_index].bgcolor = Back.BLACK + \
                                                        ' '+Style.RESET_ALL
                                                elif (self.huts[min_index].colorpoints <= self.huts[min_index].health / 2) and (self.huts[min_index].colorpoints > self.huts[min_index].health / 4):
                                                    self.huts[min_index].bgcolor = Back.YELLOW + \
                                                        ' '+Style.RESET_ALL
                                                elif (self.huts[min_index].colorpoints <= self.huts[min_index].health / 4) and (self.huts[min_index].colorpoints > 0):
                                                    self.huts[min_index].bgcolor = Back.RED + \
                                                        ' '+Style.RESET_ALL

                                                flag = 0
                                                break
                                        if flag == 0:
                                            break
                                    if flag == 1:
                                        if self.huts[min_index].xcoord > self.troops[num][p].xcoord:
                                            self.troops[num][p].xcoord = self.troops[num][p].xcoord + 1
                                        elif self.huts[min_index].xcoord < self.troops[num][p].xcoord:
                                            self.troops[num][p].xcoord = self.troops[num][p].xcoord - 1
                                        if self.huts[min_index].ycoord > self.troops[num][p].ycoord:
                                            self.troops[num][p].ycoord = self.troops[num][p].ycoord + 1
                                        elif self.huts[min_index].ycoord < self.troops[num][p].ycoord:
                                            self.troops[num][p].ycoord = self.troops[num][p].ycoord - 1
                                elif(min_index > 4 and min_index != 7):
                                    flag = 1
                                    for row in range(self.troops[num][p].ycoord-1, self.troops[num][p].ycoord+self.troops[num][p].height + 1):
                                        for col in range(self.troops[num][p].xcoord-1, self.troops[num][p].xcoord+self.troops[num][p].width+1):
                                            if self.status[row][col] == 1 and self.wallstatus[row][col] == 0:
                                                self.cannons[min_index-5].colorpoints = self.cannons[min_index-5].colorpoints - \
                                                    self.troops[num][p].damage
                                                if self.cannons[min_index-5].colorpoints <= 0:
                                                    self.cannons[min_index -
                                                                 5].colorpoints = 0
                                                    self.cannons[min_index -
                                                                 5].isdamage = 1
                                                    self.cannons[min_index-5].bgcolor = Back.BLACK + \
                                                        ' '+Style.RESET_ALL
                                                elif (self.cannons[min_index-5].colorpoints <= self.cannons[min_index-5].health / 2) and (self.cannons[min_index-5].colorpoints > self.cannons[min_index-5].health / 4):
                                                    self.cannons[min_index-5].bgcolor = Back.YELLOW + \
                                                        ' '+Style.RESET_ALL
                                                elif (self.cannons[min_index-5].colorpoints <= self.cannons[min_index-5].health / 4) and (self.cannons[min_index-5].colorpoints > 0):
                                                    self.cannons[min_index-5].bgcolor = Back.RED + \
                                                        ' '+Style.RESET_ALL

                                                flag = 0
                                                break
                                        if flag == 0:
                                            break
                                    if flag == 1:
                                        if self.cannons[min_index-5].xcoord > self.troops[num][p].xcoord:
                                            self.troops[num][p].xcoord = self.troops[num][p].xcoord + 1
                                        elif self.cannons[min_index-5].xcoord < self.troops[num][p].xcoord:
                                            self.troops[num][p].xcoord = self.troops[num][p].xcoord - 1
                                        if self.cannons[min_index-5].ycoord > self.troops[num][p].ycoord:
                                            self.troops[num][p].ycoord = self.troops[num][p].ycoord + 1
                                        elif self.cannons[min_index-5].ycoord < self.troops[num][p].ycoord:
                                            self.troops[num][p].ycoord = self.troops[num][p].ycoord - 1
                                else:
                                    flag = 1
                                    for row in range(self.troops[num][p].ycoord-1, self.troops[num][p].ycoord+self.troops[num][p].height + 1):
                                        for col in range(self.troops[num][p].xcoord-1, self.troops[num][p].xcoord+self.troops[num][p].width+1):
                                            if self.status[row][col] == 1 and self.wallstatus[row][col] == 0:
                                                self.town_hall.colorpoints = self.town_hall.colorpoints - \
                                                    self.troops[num][p].damage
                                                if self.town_hall.colorpoints <= 0:
                                                    self.town_hall.colorpoints = 0
                                                    self.town_hall.isdamage = 1
                                                    self.town_hall.bgcolor = Back.BLACK + \
                                                        ' '+Style.RESET_ALL
                                                elif (self.town_hall.colorpoints <= self.town_hall.health / 2) and (self.town_hall.colorpoints > self.town_hall.health / 4):
                                                    self.town_hall.bgcolor = Back.YELLOW + \
                                                        ' '+Style.RESET_ALL
                                                elif (self.town_hall.colorpoints <= self.town_hall.health / 4) and (self.town_hall.colorpoints > 0):
                                                    self.town_hall.bgcolor = Back.RED + \
                                                        ' '+Style.RESET_ALL

                                                flag = 0
                                                break
                                        if flag == 0:
                                            break
                                    if flag == 1:
                                        if self.town_hall.xcoord > self.troops[num][p].xcoord:
                                            self.troops[num][p].xcoord = self.troops[num][p].xcoord + 1
                                        elif self.town_hall.xcoord < self.troops[num][p].xcoord:
                                            self.troops[num][p].xcoord = self.troops[num][p].xcoord - 1
                                        if self.town_hall.ycoord > self.troops[num][p].ycoord:
                                            self.troops[num][p].ycoord = self.troops[num][p].ycoord + 1
                                        elif self.town_hall.ycoord < self.troops[num][p].ycoord:
                                            self.troops[num][p].ycoord = self.troops[num][p].ycoord - 1
                    if var == 1:
                        break
        self.time = current_time()
        for num in range(3):
            for p in range(2):
                if self.troops[num][p].status == 1 and self.troops[num][p].isdamage == 0:
                    for row in range(self.troops[num][p].ycoord, self.troops[num][p].ycoord+self.troops[num][p].height):
                        for col in range(self.troops[num][p].xcoord, self.troops[num][p].xcoord+self.troops[num][p].width):
                            self.board[row][col] = self.troops[num][p].bgcolor
        is_attack = 0
        # archers movement
        if(current_time() - self.archertime > 0.1):
            for num in range(3):
                var = 0
                for p in range(1):
                    min = -1
                    distance = -1
                    min_index = -1
                    flag = 0
                    touch = 0
                    if self.archers[num][p].status == 1:
                        if self.archers[num][p].isdamage == 0:
                            touch_row = -1
                            touch_col = -1

                            for row in range(self.archers[num][p].ycoord-1, self.archers[num][p].ycoord+self.archers[num][p].height + 1):
                                for col in range(self.archers[num][p].xcoord-1, self.archers[num][p].xcoord+self.archers[num][p].width+1):
                                    if self.wallstatus[row][col] == 1:
                                        touch_row = row
                                        touch_col = col
                                        flag = 1
                                        break
                                if flag == 1:
                                    break
                            if flag == 1:
                                flag = 0
                                for w in range(175):
                                    for row in range(self.walls[w].ycoord, self.walls[w].ycoord+self.walls[w].height):
                                        for col in range(self.walls[w].xcoord, self.walls[w].xcoord+self.walls[w].width):
                                            if row == touch_row and col == touch_col:
                                                self.walls[w].colorpoints = self.walls[w].colorpoints - \
                                                    self.archers[num][p].damage
                                                if self.walls[w].colorpoints <= 0:
                                                    self.walls[w].colorpoints = 0
                                                    self.walls[w].isdamage = 1
                                                    self.walls[w].bgcolor = Back.BLACK + \
                                                        ' '+Style.RESET_ALL
                                                    self.walls[w].isattack = 1
                                                    # make all the points lying in wall as wall status 0
                                                    for row in range(self.walls[w].ycoord, self.walls[w].ycoord+self.walls[w].height):
                                                        for col in range(self.walls[w].xcoord, self.walls[w].xcoord+self.walls[w].width):
                                                            self.wallstatus[row][col] = 0
                                                            self.status[row][col] = 0
                                                flag = 1
                                                break
                                        if flag == 1:
                                            break
                                    if flag == 1:
                                        break
                            vari = flag

                            if flag == 0 or flag == 1:
                                min = -1
                                min_index = -1
                                distance = -1
                                # check for huts
                                for r in range(5):
                                    if self.huts[r].isdamage == 0:
                                        distance = math.sqrt((self.huts[r].xcoord-self.archers[num][p].xcoord)**2 + (
                                            self.huts[r].ycoord-self.archers[num][p].ycoord)**2)
                                        if distance < min or min == -1:
                                            min = distance
                                            min_index = r
                                # check for cannons
                                for r in range(2):
                                    if self.cannons[r].isdamage == 0:
                                        distance = math.sqrt((self.cannons[r].xcoord-self.archers[num][p].xcoord)**2 + (
                                            self.cannons[r].ycoord-self.archers[num][p].ycoord)**2)
                                        if distance < min or min == -1:
                                            min = distance
                                            min_index = r+5
                                # check for wizard tower
                                for r in range(2):
                                    if self.wizardtowers[r].isdamage == 0:
                                        distance = math.sqrt((self.wizardtowers[r].xcoord-self.archers[num][p].xcoord)**2 + (
                                            self.wizardtowers[r].ycoord-self.archers[num][p].ycoord)**2)
                                        if distance < min or min == -1:
                                            min = distance
                                            min_index = r+7
                                # check for townhall
                                if self.town_hall.isdamage == 0:
                                    distance = math.sqrt((self.town_hall.xcoord-self.archers[num][p].xcoord)**2 + (
                                        self.town_hall.ycoord-self.archers[num][p].ycoord)**2)
                                if distance < min or min == -1:
                                    min = distance
                                    min_index = 9
                                if(min_index == -1):
                                    exit()
                                if (min_index < 5 and min_index != 7):
                                    flag = 1
                                    for row in range(self.archers[num][p].ycoord-1, self.archers[num][p].ycoord+self.archers[num][p].height + 1):
                                        for col in range(self.archers[num][p].xcoord-1, self.archers[num][p].xcoord+self.archers[num][p].width+1):
                                            if (abs(self.huts[min_index].xcoord-self.archers[num][p].xcoord) <= 2 and abs(self.huts[min_index].ycoord-self.archers[num][p].ycoord) <= 2):
                                                touch = 1
                                            if math.sqrt((self.huts[min_index].xcoord-self.archers[num][p].xcoord)**2 + (self.huts[min_index].ycoord-self.archers[num][p].ycoord)**2) <= self.archers[num][p].range and self.wallstatus[row][col] == 0:
                                                print(math.sqrt((self.huts[min_index].xcoord-self.archers[num][p].xcoord)**2 + (
                                                    self.huts[min_index].ycoord-self.archers[num][p].ycoord)**2))
                                               # exit()
                                                self.huts[min_index].colorpoints = self.huts[min_index].colorpoints - \
                                                    self.archers[num][p].damage
                                                if self.huts[min_index].colorpoints <= 0:
                                                    self.huts[min_index].colorpoints = 0
                                                    self.huts[min_index].isdamage = 1
                                                    self.huts[min_index].bgcolor = Back.BLACK + \
                                                        ' '+Style.RESET_ALL
                                                elif (self.huts[min_index].colorpoints <= self.huts[min_index].health / 2) and (self.huts[min_index].colorpoints > self.huts[min_index].health / 4):
                                                    self.huts[min_index].bgcolor = Back.YELLOW + \
                                                        ' '+Style.RESET_ALL
                                                elif (self.huts[min_index].colorpoints <= self.huts[min_index].health / 4) and (self.huts[min_index].colorpoints > 0):
                                                    self.huts[min_index].bgcolor = Back.RED + \
                                                        ' '+Style.RESET_ALL

                                                flag = 0
                                                break
                                        if flag == 0:
                                            break
                                    if touch == 0 and vari == 0:
                                        if self.huts[min_index].xcoord > self.archers[num][p].xcoord:
                                            self.archers[num][p].xcoord = self.archers[num][p].xcoord + 1
                                        elif self.huts[min_index].xcoord < self.archers[num][p].xcoord:
                                            self.archers[num][p].xcoord = self.archers[num][p].xcoord - 1
                                        if self.huts[min_index].ycoord > self.archers[num][p].ycoord:
                                            self.archers[num][p].ycoord = self.archers[num][p].ycoord + 1
                                        elif self.huts[min_index].ycoord < self.archers[num][p].ycoord:
                                            self.archers[num][p].ycoord = self.archers[num][p].ycoord - 1
                                    touch = 0
                                elif(min_index > 4 and min_index < 7):
                                    flag = 1
                                    for row in range(self.archers[num][p].ycoord-1, self.archers[num][p].ycoord+self.archers[num][p].height + 1):
                                        for col in range(self.archers[num][p].xcoord-1, self.archers[num][p].xcoord+self.archers[num][p].width+1):
                                            if (abs(self.cannons[min_index-5].xcoord-self.archers[num][p].xcoord) <= 2 and abs(self.cannons[min_index - 5].ycoord-self.archers[num][p].ycoord) <= 2):
                                                touch = 1
                                            if math.sqrt((self.cannons[min_index-5].xcoord-self.archers[num][p].xcoord)**2 + (self.cannons[min_index-5].ycoord-self.archers[num][p].ycoord)**2) <= self.archers[num][p].range and self.wallstatus[row][col] == 0:
                                                self.cannons[min_index-5].colorpoints = self.cannons[min_index-5].colorpoints - \
                                                    self.archers[num][p].damage
                                                if self.cannons[min_index-5].colorpoints <= 0:
                                                    self.cannons[min_index -
                                                                 5].colorpoints = 0
                                                    self.cannons[min_index -
                                                                 5].isdamage = 1
                                                    self.cannons[min_index-5].bgcolor = Back.BLACK + \
                                                        ' '+Style.RESET_ALL
                                                elif (self.cannons[min_index-5].colorpoints <= self.cannons[min_index-5].health / 2) and (self.cannons[min_index-5].colorpoints > self.cannons[min_index-5].health / 4):
                                                    self.cannons[min_index-5].bgcolor = Back.YELLOW + \
                                                        ' '+Style.RESET_ALL
                                                elif (self.cannons[min_index-5].colorpoints <= self.cannons[min_index-5].health / 4) and (self.cannons[min_index-5].colorpoints > 0):
                                                    self.cannons[min_index-5].bgcolor = Back.RED + \
                                                        ' '+Style.RESET_ALL

                                                flag = 0
                                                break
                                        if flag == 0:
                                            break
                                    if touch == 0 and vari == 0:
                                        if self.cannons[min_index-5].xcoord > self.archers[num][p].xcoord:
                                            self.archers[num][p].xcoord = self.archers[num][p].xcoord + 1
                                        elif self.cannons[min_index-5].xcoord < self.archers[num][p].xcoord:
                                            self.archers[num][p].xcoord = self.archers[num][p].xcoord - 1
                                        if self.cannons[min_index-5].ycoord > self.archers[num][p].ycoord:
                                            self.archers[num][p].ycoord = self.archers[num][p].ycoord + 1
                                        elif self.cannons[min_index-5].ycoord < self.archers[num][p].ycoord:
                                            self.archers[num][p].ycoord = self.archers[num][p].ycoord - 1
                                    touch = 0
                                elif(min_index > 6 and min_index < 9):
                                    # repeat for wizardtowers
                                    flag = 1
                                    for row in range(self.archers[num][p].ycoord-1, self.archers[num][p].ycoord+self.archers[num][p].height + 1):
                                        for col in range(self.archers[num][p].xcoord-1, self.archers[num][p].xcoord+self.archers[num][p].width+1):
                                            if (abs(self.wizardtowers[min_index-7].xcoord-self.archers[num][p].xcoord) <= 2 and abs(self.wizardtowers[min_index-7].ycoord-self.archers[num][p].ycoord) <= 2):
                                                touch = 1
                                            if math.sqrt((self.wizardtowers[min_index-7].xcoord-self.archers[num][p].xcoord)**2 + (self.wizardtowers[min_index-7].ycoord-self.archers[num][p].ycoord)**2) <= self.archers[num][p].range and self.wallstatus[row][col] == 0:
                                                print(math.sqrt((self.wizardtowers[min_index-7].xcoord-self.archers[num][p].xcoord)**2 + (
                                                    self.wizardtowers[min_index-7].ycoord-self.archers[num][p].ycoord)**2))
                                               # exit()
                                                self.wizardtowers[min_index-7].colorpoints = self.wizardtowers[min_index-7].colorpoints - \
                                                    self.archers[num][p].damage
                                                if self.wizardtowers[min_index-7].colorpoints <= 0:
                                                    self.wizardtowers[min_index -
                                                                      7].colorpoints = 0
                                                    self.wizardtowers[min_index -
                                                                      7].isdamage = 1
                                                    self.wizardtowers[min_index-7].bgcolor = Back.BLACK + \
                                                        ' '+Style.RESET_ALL
                                                elif (self.wizardtowers[min_index-7].colorpoints <= self.wizardtowers[min_index-7].health / 2) and (self.wizardtowers[min_index-7].colorpoints > self.wizardtowers[min_index-7].health / 4):
                                                    self.wizardtowers[min_index-7].bgcolor = Back.YELLOW + \
                                                        ' '+Style.RESET_ALL
                                                elif (self.wizardtowers[min_index-7].colorpoints <= self.wizardtowers[min_index-7].health / 4) and (self.wizardtowers[min_index-7].colorpoints > 0):
                                                    self.wizardtowers[min_index-7].bgcolor = Back.RED + \
                                                        ' '+Style.RESET_ALL

                                                flag = 0
                                                break
                                        if flag == 0:
                                            break
                                    if touch == 0 and vari == 0:
                                        if self.wizardtowers[min_index-7].xcoord > self.archers[num][p].xcoord:
                                            self.archers[num][p].xcoord = self.archers[num][p].xcoord + 1
                                        elif self.wizardtowers[min_index-7].xcoord < self.archers[num][p].xcoord:
                                            self.archers[num][p].xcoord = self.archers[num][p].xcoord - 1
                                        if self.wizardtowers[min_index-7].ycoord > self.archers[num][p].ycoord:
                                            self.archers[num][p].ycoord = self.archers[num][p].ycoord + 1
                                        elif self.wizardtowers[min_index-7].ycoord < self.archers[num][p].ycoord:
                                            self.archers[num][p].ycoord = self.archers[num][p].ycoord - 1
                                    touch = 0
                                else:
                                    flag = 1
                                    for row in range(self.archers[num][p].ycoord-1, self.archers[num][p].ycoord+self.archers[num][p].height + 1):
                                        for col in range(self.archers[num][p].xcoord-1, self.archers[num][p].xcoord+self.archers[num][p].width+1):
                                            if (abs(self.town_hall.xcoord-self.archers[num][p].xcoord) <= 2 and abs(self.town_hall.ycoord-self.archers[num][p].ycoord) <= 2):
                                                touch = 1
                                            if math.sqrt((self.town_hall.xcoord-self.archers[num][p].xcoord)**2 + (self.town_hall.ycoord-self.archers[num][p].ycoord)**2) <= self.archers[num][p].range and self.wallstatus[row][col] == 0:
                                                self.town_hall.colorpoints = self.town_hall.colorpoints - \
                                                    self.archers[num][p].damage
                                                if self.town_hall.colorpoints <= 0:
                                                    self.town_hall.colorpoints = 0
                                                    self.town_hall.isdamage = 1
                                                    self.town_hall.bgcolor = Back.BLACK + \
                                                        ' '+Style.RESET_ALL
                                                elif (self.town_hall.colorpoints <= self.town_hall.health / 2) and (self.town_hall.colorpoints > self.town_hall.health / 4):
                                                    self.town_hall.bgcolor = Back.YELLOW + \
                                                        ' '+Style.RESET_ALL
                                                elif (self.town_hall.colorpoints <= self.town_hall.health / 4) and (self.town_hall.colorpoints > 0):
                                                    self.town_hall.bgcolor = Back.RED + \
                                                        ' '+Style.RESET_ALL

                                                flag = 0
                                                break
                                        if flag == 0:
                                            break
                                    if touch == 0 and vari == 0:
                                        if self.town_hall.xcoord > self.archers[num][p].xcoord:
                                            self.archers[num][p].xcoord = self.archers[num][p].xcoord + 1
                                        elif self.town_hall.xcoord < self.archers[num][p].xcoord:
                                            self.archers[num][p].xcoord = self.archers[num][p].xcoord - 1
                                        if self.town_hall.ycoord > self.archers[num][p].ycoord:
                                            self.archers[num][p].ycoord = self.archers[num][p].ycoord + 1
                                        elif self.town_hall.ycoord < self.archers[num][p].ycoord:
                                            self.archers[num][p].ycoord = self.archers[num][p].ycoord - 1
                                    touch = 0
                    if var == 1:
                        break
        self.archertime = current_time()
        for num in range(3):
            for p in range(1):
                if self.archers[num][p].status == 1 and self.archers[num][p].isdamage == 0:
                    for row in range(self.archers[num][p].ycoord, self.archers[num][p].ycoord+self.archers[num][p].height):
                        for col in range(self.archers[num][p].xcoord, self.archers[num][p].xcoord+self.archers[num][p].width):
                            self.board[row][col] = Back.LIGHTYELLOW_EX + \
                                ' '+Style.RESET_ALL
        is_attack = 0
        # balloons movement
        if(current_time() - self.balloontime > 0.1):
            for num in range(3):
                var = 0
                for p in range(2):
                    min = -1
                    distance = -1
                    min_index = -1
                    flag = 0
                    touch = 0
                    isdefensiveexist = 0
                    for r in range(2):
                        if self.cannons[r].isdamage == 0 or self.wizardtowers[r].isdamage == 0:
                            isdefensiveexist = 1
                            break
                    if isdefensiveexist == 1:
                        if self.balloons[num][p].status == 1:
                            if self.balloons[num][p].isdamage == 0:
                                # check for cannons
                                for r in range(2):
                                    if self.cannons[r].isdamage == 0:
                                        distance = math.sqrt((self.cannons[r].xcoord-self.balloons[num][p].xcoord)**2 + (
                                            self.cannons[r].ycoord-self.balloons[num][p].ycoord)**2)
                                        if distance < min or min == -1:
                                            min = distance
                                            min_index = r
                                # check for wizard towers
                                for r in range(2):
                                    if self.wizardtowers[r].isdamage == 0:
                                        distance = math.sqrt((self.wizardtowers[r].xcoord-self.balloons[num][p].xcoord)**2 + (
                                            self.wizardtowers[r].ycoord-self.balloons[num][p].ycoord)**2)
                                        if distance < min or min == -1:
                                            min = distance
                                            min_index = r+2
                                if(min_index == -1):
                                    exit()
                                if(min_index < 2):
                                    flag = 1
                                    for row in range(self.balloons[num][p].ycoord-1, self.balloons[num][p].ycoord+self.balloons[num][p].height + 1):
                                        for col in range(self.balloons[num][p].xcoord-1, self.balloons[num][p].xcoord+self.balloons[num][p].width+1):
                                            if self.defensivestatus[row][col] == 1 and self.wallstatus[row][col] == 0:
                                                self.cannons[min_index].colorpoints = self.cannons[min_index].colorpoints - \
                                                    self.balloons[num][p].damage
                                                if self.cannons[min_index].colorpoints <= 0:
                                                    self.cannons[min_index].colorpoints = 0
                                                    self.cannons[min_index].isdamage = 1
                                                    self.cannons[min_index].bgcolor = Back.BLACK + \
                                                        ' '+Style.RESET_ALL
                                                    # make all the points in cannon status 0
                                                    for row in range(self.cannons[min_index].ycoord, self.cannons[min_index].ycoord+self.cannons[min_index].height):
                                                        for col in range(self.cannons[min_index].xcoord, self.cannons[min_index].xcoord+self.cannons[min_index].width):
                                                            self.defensivestatus[row][col] = 0
                                                            self.status[row][col] = 0
                                                elif (self.cannons[min_index].colorpoints <= self.cannons[min_index].health / 2) and (self.cannons[min_index].colorpoints > self.cannons[min_index].health / 4):
                                                    self.cannons[min_index].bgcolor = Back.YELLOW + \
                                                        ' '+Style.RESET_ALL
                                                elif (self.cannons[min_index].colorpoints <= self.cannons[min_index].health / 4) and (self.cannons[min_index].colorpoints > 0):
                                                    self.cannons[min_index].bgcolor = Back.RED + \
                                                        ' '+Style.RESET_ALL

                                                flag = 0
                                                break
                                        if flag == 0:
                                            break
                                    if self.cannons[min_index].xcoord > self.balloons[num][p].xcoord:
                                        self.balloons[num][p].xcoord = self.balloons[num][p].xcoord + 1
                                    elif self.cannons[min_index].xcoord < self.balloons[num][p].xcoord:
                                        self.balloons[num][p].xcoord = self.balloons[num][p].xcoord - 1
                                    if self.cannons[min_index].ycoord > self.balloons[num][p].ycoord:
                                        self.balloons[num][p].ycoord = self.balloons[num][p].ycoord + 1
                                    elif self.cannons[min_index].ycoord < self.balloons[num][p].ycoord:
                                        self.balloons[num][p].ycoord = self.balloons[num][p].ycoord - 1
                                    flag = 0
                                else:
                                    # repeat the same process for wizard towers
                                    flag = 1
                                    for row in range(self.balloons[num][p].ycoord-1, self.balloons[num][p].ycoord+self.balloons[num][p].height + 1):
                                        for col in range(self.balloons[num][p].xcoord-1, self.balloons[num][p].xcoord+self.balloons[num][p].width+1):
                                            if self.defensivestatus[row][col] == 1 and self.wallstatus[row][col] == 0:
                                                self.wizardtowers[min_index-2].colorpoints = self.wizardtowers[min_index-2].colorpoints - \
                                                    self.balloons[num][p].damage
                                                if self.wizardtowers[min_index-2].colorpoints <= 0:
                                                    self.wizardtowers[min_index -
                                                                      2].colorpoints = 0
                                                    self.wizardtowers[min_index -
                                                                      2].isdamage = 1
                                                    self.wizardtowers[min_index-2].bgcolor = Back.BLACK + \
                                                        ' '+Style.RESET_ALL
                                                    # make all the points in cannon status 0
                                                    for row in range(self.wizardtowers[min_index-2].ycoord, self.wizardtowers[min_index-2].ycoord+self.wizardtowers[min_index-2].height):
                                                        for col in range(self.wizardtowers[min_index-2].xcoord, self.wizardtowers[min_index-2].xcoord+self.wizardtowers[min_index-2].width):
                                                            self.defensivestatus[row][col] = 0
                                                            self.status[row][col] = 0
                                                elif (self.wizardtowers[min_index-2].colorpoints <= self.wizardtowers[min_index-2].health / 2) and (self.wizardtowers[min_index-2].colorpoints > self.wizardtowers[min_index-2].health / 4):
                                                    self.wizardtowers[min_index-2].bgcolor = Back.YELLOW + \
                                                        ' '+Style.RESET_ALL
                                                elif (self.wizardtowers[min_index-2].colorpoints <= self.wizardtowers[min_index-2].health / 4) and (self.wizardtowers[min_index-2].colorpoints > 0):
                                                    self.wizardtowers[min_index-2].bgcolor = Back.RED + \
                                                        ' '+Style.RESET_ALL
                                                flag = 0
                                                break
                                        if flag == 0:
                                            break
                                    if self.wizardtowers[min_index-2].xcoord > self.balloons[num][p].xcoord:
                                        self.balloons[num][p].xcoord = self.balloons[num][p].xcoord + 1
                                    elif self.wizardtowers[min_index-2].xcoord < self.balloons[num][p].xcoord:
                                        self.balloons[num][p].xcoord = self.balloons[num][p].xcoord - 1
                                    if self.wizardtowers[min_index-2].ycoord > self.balloons[num][p].ycoord:
                                        self.balloons[num][p].ycoord = self.balloons[num][p].ycoord + 1
                                    elif self.wizardtowers[min_index-2].ycoord < self.balloons[num][p].ycoord:
                                        self.balloons[num][p].ycoord = self.balloons[num][p].ycoord - 1
                                    flag = 0

                    if isdefensiveexist == 0:
                        if self.balloons[num][p].status == 1:
                            if self.balloons[num][p].isdamage == 0:
                                touch_row = -1
                                touch_col = -1

                                for row in range(self.balloons[num][p].ycoord-1, self.balloons[num][p].ycoord+self.balloons[num][p].height + 1):
                                    for col in range(self.balloons[num][p].xcoord-1, self.balloons[num][p].xcoord+self.balloons[num][p].width+1):
                                        if self.wallstatus[row][col] == 1:
                                            touch_row = row
                                            touch_col = col
                                            flag = 1
                                            break
                                    if flag == 1:
                                        break
                                if flag == 1:
                                    flag = 0
                                    for w in range(175):
                                        for row in range(self.walls[w].ycoord, self.walls[w].ycoord+self.walls[w].height):
                                            for col in range(self.walls[w].xcoord, self.walls[w].xcoord+self.walls[w].width):
                                                if row == touch_row and col == touch_col:
                                                    self.walls[w].colorpoints = self.walls[w].colorpoints - \
                                                        self.balloons[num][p].damage
                                                    if self.walls[w].colorpoints <= 0:
                                                        self.walls[w].colorpoints = 0
                                                        self.walls[w].isdamage = 1
                                                        self.walls[w].bgcolor = Back.BLACK + \
                                                            ' '+Style.RESET_ALL
                                                        self.walls[w].isattack = 1
                                                        # make all the points lying in wall as wall status 0
                                                        for row in range(self.walls[w].ycoord, self.walls[w].ycoord+self.walls[w].height):
                                                            for col in range(self.walls[w].xcoord, self.walls[w].xcoord+self.walls[w].width):
                                                                self.wallstatus[row][col] = 0
                                                                self.status[row][col] = 0
                                                    flag = 1
                                                    break
                                            if flag == 1:
                                                break
                                        if flag == 1:
                                            break
                                if flag == 1:
                                    var = 1
                                    break

                                if flag == 0:
                                    min = -1
                                    min_index = -1
                                    distance = -1
                                    # check for huts
                                    for r in range(5):
                                        if self.huts[r].isdamage == 0:
                                            distance = math.sqrt((self.huts[r].xcoord-self.balloons[num][p].xcoord)**2 + (
                                                self.huts[r].ycoord-self.balloons[num][p].ycoord)**2)
                                            if distance < min or min == -1:
                                                min = distance
                                                min_index = r
                                    # check for cannons
                                    for r in range(2):
                                        if self.cannons[r].isdamage == 0:
                                            distance = math.sqrt((self.cannons[r].xcoord-self.balloons[num][p].xcoord)**2 + (
                                                self.cannons[r].ycoord-self.balloons[num][p].ycoord)**2)
                                            if distance < min or min == -1:
                                                min = distance
                                                min_index = r+5
                                    # check for townhall
                                    if self.town_hall.isdamage == 0:
                                        distance = math.sqrt((self.town_hall.xcoord-self.balloons[num][p].xcoord)**2 + (
                                            self.town_hall.ycoord-self.balloons[num][p].ycoord)**2)
                                    if distance < min or min == -1:
                                        min = distance
                                        min_index = 7
                                    if(min_index == -1):
                                        exit()
                                    if (min_index < 5 and min_index != 7):
                                        flag = 1
                                        for row in range(self.balloons[num][p].ycoord-1, self.balloons[num][p].ycoord+self.balloons[num][p].height + 1):
                                            for col in range(self.balloons[num][p].xcoord-1, self.balloons[num][p].xcoord+self.balloons[num][p].width+1):
                                                if self.status[row][col] == 1 and self.wallstatus[row][col] == 0:
                                                    print(math.sqrt((self.huts[min_index].xcoord-self.balloons[num][p].xcoord)**2 + (
                                                        self.huts[min_index].ycoord-self.balloons[num][p].ycoord)**2))
                                                # exit()
                                                    self.huts[min_index].colorpoints = self.huts[min_index].colorpoints - \
                                                        self.balloons[num][p].damage
                                                    if self.huts[min_index].colorpoints <= 0:
                                                        self.huts[min_index].colorpoints = 0
                                                        self.huts[min_index].isdamage = 1
                                                        self.huts[min_index].bgcolor = Back.BLACK + \
                                                            ' '+Style.RESET_ALL
                                                    elif (self.huts[min_index].colorpoints <= self.huts[min_index].health / 2) and (self.huts[min_index].colorpoints > self.huts[min_index].health / 4):
                                                        self.huts[min_index].bgcolor = Back.YELLOW + \
                                                            ' '+Style.RESET_ALL
                                                    elif (self.huts[min_index].colorpoints <= self.huts[min_index].health / 4) and (self.huts[min_index].colorpoints > 0):
                                                        self.huts[min_index].bgcolor = Back.RED + \
                                                            ' '+Style.RESET_ALL

                                                    flag = 0
                                                    break
                                            if flag == 0:
                                                break
                                        if self.huts[min_index].xcoord > self.balloons[num][p].xcoord:
                                            self.balloons[num][p].xcoord = self.balloons[num][p].xcoord + 1
                                        elif self.huts[min_index].xcoord < self.balloons[num][p].xcoord:
                                            self.balloons[num][p].xcoord = self.balloons[num][p].xcoord - 1
                                        if self.huts[min_index].ycoord > self.balloons[num][p].ycoord:
                                            self.balloons[num][p].ycoord = self.balloons[num][p].ycoord + 1
                                        elif self.huts[min_index].ycoord < self.balloons[num][p].ycoord:
                                            self.balloons[num][p].ycoord = self.balloons[num][p].ycoord - 1
                                    elif(min_index > 4 and min_index != 7):
                                        flag = 1
                                        for row in range(self.balloons[num][p].ycoord-1, self.balloons[num][p].ycoord+self.balloons[num][p].height + 1):
                                            for col in range(self.balloons[num][p].xcoord-1, self.balloons[num][p].xcoord+self.balloons[num][p].width+1):
                                                if self.status[row][col] == 1 and self.wallstatus[row][col] == 0:
                                                    self.cannons[min_index-5].colorpoints = self.cannons[min_index-5].colorpoints - \
                                                        self.balloons[num][p].damage
                                                    if self.cannons[min_index-5].colorpoints <= 0:
                                                        self.cannons[min_index -
                                                                     5].colorpoints = 0
                                                        self.cannons[min_index -
                                                                     5].isdamage = 1
                                                        self.cannons[min_index-5].bgcolor = Back.BLACK + \
                                                            ' '+Style.RESET_ALL
                                                    elif (self.cannons[min_index-5].colorpoints <= self.cannons[min_index-5].health / 2) and (self.cannons[min_index-5].colorpoints > self.cannons[min_index-5].health / 4):
                                                        self.cannons[min_index-5].bgcolor = Back.YELLOW + \
                                                            ' '+Style.RESET_ALL
                                                    elif (self.cannons[min_index-5].colorpoints <= self.cannons[min_index-5].health / 4) and (self.cannons[min_index-5].colorpoints > 0):
                                                        self.cannons[min_index-5].bgcolor = Back.RED + \
                                                            ' '+Style.RESET_ALL

                                                    flag = 0
                                                    break
                                            if flag == 0:
                                                break

                                        if self.cannons[min_index-5].xcoord > self.balloons[num][p].xcoord:
                                            self.balloons[num][p].xcoord = self.balloons[num][p].xcoord + 1
                                        elif self.cannons[min_index-5].xcoord < self.balloons[num][p].xcoord:
                                            self.balloons[num][p].xcoord = self.balloons[num][p].xcoord - 1
                                        if self.cannons[min_index-5].ycoord > self.balloons[num][p].ycoord:
                                            self.balloons[num][p].ycoord = self.balloons[num][p].ycoord + 1
                                        elif self.cannons[min_index-5].ycoord < self.balloons[num][p].ycoord:
                                            self.balloons[num][p].ycoord = self.balloons[num][p].ycoord - 1
                                    else:
                                        flag = 1
                                        for row in range(self.balloons[num][p].ycoord-1, self.balloons[num][p].ycoord+self.balloons[num][p].height + 1):
                                            for col in range(self.balloons[num][p].xcoord-1, self.balloons[num][p].xcoord+self.balloons[num][p].width+1):
                                                if self.status[row][col] == 1 and self.wallstatus[row][col] == 0:
                                                    self.town_hall.colorpoints = self.town_hall.colorpoints - \
                                                        self.balloons[num][p].damage
                                                    if self.town_hall.colorpoints <= 0:
                                                        self.town_hall.colorpoints = 0
                                                        self.town_hall.isdamage = 1
                                                        self.town_hall.bgcolor = Back.BLACK + \
                                                            ' '+Style.RESET_ALL
                                                    elif (self.town_hall.colorpoints <= self.town_hall.health / 2) and (self.town_hall.colorpoints > self.town_hall.health / 4):
                                                        self.town_hall.bgcolor = Back.YELLOW + \
                                                            ' '+Style.RESET_ALL
                                                    elif (self.town_hall.colorpoints <= self.town_hall.health / 4) and (self.town_hall.colorpoints > 0):
                                                        self.town_hall.bgcolor = Back.RED + \
                                                            ' '+Style.RESET_ALL

                                                    flag = 0
                                                    break
                                            if flag == 0:
                                                break
                                        if self.town_hall.xcoord > self.balloons[num][p].xcoord:
                                            self.balloons[num][p].xcoord = self.balloons[num][p].xcoord + 1
                                        elif self.town_hall.xcoord < self.balloons[num][p].xcoord:
                                            self.balloons[num][p].xcoord = self.balloons[num][p].xcoord - 1
                                        if self.town_hall.ycoord > self.balloons[num][p].ycoord:
                                            self.balloons[num][p].ycoord = self.balloons[num][p].ycoord + 1
                                        elif self.town_hall.ycoord < self.balloons[num][p].ycoord:
                                            self.balloons[num][p].ycoord = self.balloons[num][p].ycoord - 1
                    if var == 1:
                        break
        self.balloontime = current_time()
        for num in range(3):
            for p in range(2):
                if self.balloons[num][p].status == 1 and self.balloons[num][p].isdamage == 0:
                    for row in range(self.balloons[num][p].ycoord, self.balloons[num][p].ycoord+self.balloons[num][p].height):
                        for col in range(self.balloons[num][p].xcoord, self.balloons[num][p].xcoord+self.balloons[num][p].width):
                            self.board[row][col] = Back.LIGHTWHITE_EX + \
                                ' '+Style.RESET_ALL
        is_attack = 0
        # cannons attack

        if(current_time() - self.cannons[1].time > 0.5):
            for p in range(2):
                xcoordinate = self.cannons[p].xcoord
                ycoordinate = self.cannons[p].ycoord
                # attack king
                if self.variable == 'k':
                    for row in range(self.cannons[p].ycoord-5, self.cannons[p].ycoord+5+self.cannons[p].height):
                        for col in range(self.cannons[p].xcoord-5, self.cannons[p].xcoord+5+self.cannons[p].width):
                            if math.sqrt((col-self.king.xcoord)**2 + (row-self.king.ycoord)**2) <= self.cannons[p].range and self.cannons[p].isdamage == 0:
                                x = self.king.health - self.cannons[p].damage
                                print(self.king.health)
                                if x <= 0:
                                    self.king.health = 0
                                    self.king.isdamage = 1
                                    self.king.bgcolor = Back.BLACK + ' '+Style.RESET_ALL
                                    is_attack = 1
                                    break
                                else:
                                    self.king.health = x
                                    self.king.len = 30 * self.king.health / self.king.maxhealth
                                    is_attack = 1
                                    break
                        if is_attack == 1:
                            break
                elif(self.variable == 'q'):
                    for row in range(self.cannons[p].ycoord-5, self.cannons[p].ycoord+5+self.cannons[p].height):
                        for col in range(self.cannons[p].xcoord-5, self.cannons[p].xcoord+5+self.cannons[p].width):
                            if math.sqrt((col-self.queen.xcoord)**2 + (row-self.queen.ycoord)**2) <= self.cannons[p].range and self.cannons[p].isdamage == 0:
                                x = self.queen.health - self.cannons[p].damage
                                if x <= 0:
                                    self.queen.health = 0
                                    self.queen.isdamage = 1
                                    self.queen.bgcolor = Back.BLACK + ' '+Style.RESET_ALL
                                    is_attack = 1
                                    break
                                else:
                                    self.queen.health = x
                                    self.queen.len = 30 * self.queen.health / self.queen.maxhealth
                                    is_attack = 1
                                    break
                        if is_attack == 1:
                            break
               # attack troops
                if is_attack == 0:
                    for num in range(3):
                        for q in range(2):
                            if self.troops[num][q].status == 1 and self.troops[num][q].isdamage == 0:
                                for row in range(self.cannons[p].ycoord-5, self.cannons[p].ycoord+5+self.cannons[p].height):
                                    for col in range(self.cannons[p].xcoord-5, self.cannons[p].xcoord+5+self.cannons[p].width):
                                        if math.sqrt((col-self.troops[num][q].xcoord)**2 + (row-self.troops[num][q].ycoord)**2) <= self.cannons[p].range and self.cannons[p].isdamage == 0:
                                            x = self.troops[num][q].hitpoints - \
                                                self.cannons[p].damage
                                            if x <= 0:
                                                self.troops[num][q].hitpoints = 0
                                                self.troops[num][q].isdamage = 1
                                                self.troops[num][q].bgcolor = Back.BLACK + \
                                                    ' '+Style.RESET_ALL
                                                is_attack = 1
                                                break
                                            else:
                                                self.troops[num][q].hitpoints = x
                                                is_attack = 1
                                                break
                                    if is_attack == 1:
                                        break
                            if is_attack == 1:
                                break
                        if is_attack == 1:
                            break
               # attack archers
                if is_attack == 0:
                    for num in range(3):
                        for q in range(1):
                            if self.archers[num][q].status == 1 and self.archers[num][q].isdamage == 0:
                                for row in range(self.cannons[p].ycoord-5, self.cannons[p].ycoord+5+self.cannons[p].height):
                                    for col in range(self.cannons[p].xcoord-5, self.cannons[p].xcoord+5+self.cannons[p].width):
                                        if math.sqrt((col-self.archers[num][q].xcoord)**2 + (row-self.archers[num][q].ycoord)**2) <= self.cannons[p].range and self.cannons[p].isdamage == 0:
                                            x = self.archers[num][q].hitpoints - \
                                                self.cannons[p].damage
                                            if x <= 0:
                                                self.archers[num][q].hitpoints = 0
                                                self.archers[num][q].isdamage = 1
                                                self.archers[num][q].bgcolor = Back.BLACK + \
                                                    ' '+Style.RESET_ALL
                                                is_attack = 1
                                                break
                                            else:
                                                self.archers[num][q].hitpoints = x
                                                is_attack = 1
                                                break
                                    if is_attack == 1:
                                        break
                            if is_attack == 1:
                                break
                        if is_attack == 1:
                            break
        self.cannons[1].time = current_time()

        # wizardtower attack
        if(current_time() - self.wizardtowers[1].time > 0.5):
            for p in range(2):
                xcoordinate = self.wizardtowers[p].xcoord
                ycoordinate = self.wizardtowers[p].ycoord
                width, height, damage, xcoord, ycoord = -1, -1, -1, -1, -1
                # attack king
                is_attack = 0
               # attack troops
                if is_attack == 0:
                    troop_row = -1
                    troop_col = -1
                    for num in range(3):
                        for q in range(2):
                            if self.troops[num][q].status == 1 and self.troops[num][q].isdamage == 0:
                                for row in range(self.wizardtowers[p].ycoord-5, self.wizardtowers[p].ycoord+5+self.wizardtowers[p].height):
                                    for col in range(self.wizardtowers[p].xcoord-5, self.wizardtowers[p].xcoord+5+self.wizardtowers[p].width):
                                        if math.sqrt((col-self.troops[num][q].xcoord)**2 + (row-self.troops[num][q].ycoord)**2) <= self.wizardtowers[p].range and self.wizardtowers[p].isdamage == 0:
                                            x = self.troops[num][q].hitpoints - \
                                                self.wizardtowers[p].damage
                                            troop_row = num
                                            troop_col = q
                                            if x <= 0:
                                                self.troops[num][q].hitpoints = 0
                                                self.troops[num][q].isdamage = 1
                                                self.troops[num][q].bgcolor = Back.BLACK + \
                                                    ' '+Style.RESET_ALL
                                                is_attack = 1
                                                break
                                            else:
                                                self.troops[num][q].hitpoints = x
                                                is_attack = 1
                                                width = self.troops[num][q].width
                                                height = self.troops[num][q].height
                                                damage = self.troops[num][q].damage
                                                xcoord = self.troops[num][q].xcoord
                                                ycoord = self.troops[num][q].ycoord

                                                break
                                    if is_attack == 1:
                                        break
                            if is_attack == 1:
                                break
                        if is_attack == 1:
                            break
                    if is_attack == 0:
                        # repeat the above process for archers
                        for num in range(3):
                            for q in range(1):
                                if self.archers[num][q].status == 1 and self.archers[num][q].isdamage == 0:
                                    for row in range(self.wizardtowers[p].ycoord-5, self.wizardtowers[p].ycoord+5+self.wizardtowers[p].height):
                                        for col in range(self.wizardtowers[p].xcoord-5, self.wizardtowers[p].xcoord+5+self.wizardtowers[p].width):
                                            if math.sqrt((col-self.archers[num][q].xcoord)**2 + (row-self.archers[num][q].ycoord)**2) <= self.wizardtowers[p].range and self.wizardtowers[p].isdamage == 0:
                                                x = self.archers[num][q].hitpoints - \
                                                    self.wizardtowers[p].damage
                                                troop_row = num
                                                troop_col = q
                                                if x <= 0:
                                                    self.archers[num][q].hitpoints = 0
                                                    self.archers[num][q].isdamage = 1
                                                    self.archers[num][q].bgcolor = Back.BLACK + \
                                                        ' '+Style.RESET_ALL
                                                    is_attack = 1
                                                    break
                                                else:
                                                    self.archers[num][q].hitpoints = x
                                                    is_attack = 1
                                                    width = self.troops[num][q].width
                                                    height = self.troops[num][q].height
                                                    damage = self.troops[num][q].damage
                                                    xcoord = self.troops[num][q].xcoord
                                                    ycoord = self.troops[num][q].ycoord
                                                    break
                                        if is_attack == 1:
                                            break
                                if is_attack == 1:
                                    break
                            if is_attack == 1:
                                break
                    if is_attack == 0:
                        # repeat the same for balloons
                        for num in range(3):
                            for q in range(2):
                                if self.balloons[num][q].status == 1 and self.balloons[num][q].isdamage == 0:
                                    for row in range(self.wizardtowers[p].ycoord-5, self.wizardtowers[p].ycoord+5+self.wizardtowers[p].height):
                                        for col in range(self.wizardtowers[p].xcoord-5, self.wizardtowers[p].xcoord+5+self.wizardtowers[p].width):
                                            if math.sqrt((col-self.balloons[num][q].xcoord)**2 + (row-self.balloons[num][q].ycoord)**2) <= self.wizardtowers[p].range and self.wizardtowers[p].isdamage == 0:
                                                x = self.balloons[num][q].hitpoints - \
                                                    self.wizardtowers[p].damage
                                                troop_row = num
                                                troop_col = q
                                                if x <= 0:
                                                    self.balloons[num][q].hitpoints = 0
                                                    self.balloons[num][q].isdamage = 1
                                                    self.balloons[num][q].bgcolor = Back.BLACK + \
                                                        ' '+Style.RESET_ALL
                                                    is_attack = 1
                                                    break
                                                else:
                                                    self.balloons[num][q].hitpoints = x
                                                    is_attack = 1
                                                    width = self.troops[num][q].width
                                                    height = self.troops[num][q].height
                                                    damage = self.troops[num][q].damage
                                                    xcoord = self.troops[num][q].xcoord
                                                    ycoord = self.troops[num][q].ycoord
                                                    break
                                        if is_attack == 1:
                                            break
                                if is_attack == 1:
                                    break
                            if is_attack == 1:
                                break
                    if(is_attack == 1):
                        # attack king in the 3*3 area arounf troops[troop_row][troop_col]
                        if self.variable == 'k':
                            if(abs(self.king.xcoord - xcoord) <= ((width + 3)/2) and abs(self.king.ycoord - ycoord) <= ((height + 3)/2)):
                                x = self.king.health - \
                                    damage
                                if x <= 0:
                                    self.king.health = 0
                                    self.king.isdamage = 1
                                    self.king.bgcolor = Back.BLACK + ' '+Style.RESET_ALL
                                else:
                                    self.king.health = x
                                    self.king.len = 30 * self.king.health / self.king.maxhealth

                        elif(self.variable == 'q'):
                            if(abs(self.queen.xcoord - xcoord) <= ((width + 3)/2) and abs(self.queen.ycoord - ycoord) <= ((height + 3)/2)):
                                x = self.queen.health - \
                                    damage
                                if x <= 0:
                                    self.queen.health = 0
                                    self.queen.isdamage = 1
                                    self.queen.bgcolor = Back.BLACK + ' '+Style.RESET_ALL
                                else:
                                    self.queen.health = x
                                    self.queen.len = 30 * self.queen.health / self.queen.maxhealth
                        is_attack = 0
                        # attack troops
                        for num in range(3):
                            for q in range(2):
                                if self.troops[num][q].isdamage == 0:
                                    if(abs(xcoord - self.troops[num][q].xcoord) <= ((width + 3)/2) and abs(ycoord - self.troops[num][q].ycoord) <= ((height + 3)/2)):
                                        x = self.troops[num][q].hitpoints - \
                                            damage
                                        if x <= 0:
                                            self.troops[num][q].hitpoints = 0
                                            self.troops[num][q].isdamage = 1
                                            self.troops[num][q].bgcolor = Back.BLACK + \
                                                ' '+Style.RESET_ALL
                                            is_attack = 1
                                            break
                                        else:
                                            self.troops[num][q].hitpoints = x
                                            is_attack = 1
                                            break
                        # attack archers
                        for num in range(3):
                            for q in range(1):
                                if self.archers[num][q].isdamage == 0:
                                    if(abs(xcoord - self.archers[num][q].xcoord) <= ((width + 3)/2) and abs(ycoord - self.archers[num][q].ycoord) <= ((height + 3)/2)):
                                        x = self.archers[num][q].hitpoints - \
                                            damage
                                        if x <= 0:
                                            self.archers[num][q].hitpoints = 0
                                            self.archers[num][q].isdamage = 1
                                            self.archers[num][q].bgcolor = Back.BLACK + \
                                                ' '+Style.RESET_ALL
                                            is_attack = 1
                                            break
                                        else:
                                            self.archers[num][q].hitpoints = x
                                            is_attack = 1
                                            break
                        # attack balloons
                        for num in range(3):
                            for q in range(2):
                                if self.balloons[num][q].isdamage == 0:
                                    if(abs(xcoord - self.balloons[num][q].xcoord) <= ((width + 3)/2) and abs(ycoord - self.balloons[num][q].ycoord) <= ((height + 3)/2)):
                                        x = self.balloons[num][q].hitpoints - \
                                            damage
                                        if x <= 0:
                                            self.balloons[num][q].hitpoints = 0
                                            self.balloons[num][q].isdamage = 1
                                            self.balloons[num][q].bgcolor = Back.BLACK + \
                                                ' '+Style.RESET_ALL
                                            is_attack = 1
                                            break
                                        else:
                                            self.balloons[num][q].hitpoints = x
                                            is_attack = 1
                                            break

                        # currently attacked troop is

        self.wizardtowers[1].time = current_time()
        # queen attack bonus
        if self.variable == 'q':
            flag = 1
            status = []
            def min(x,y):
                if(x<y):
                    return x
                else:
                    return y
            if self.input_char == 'g':
                if(self.queen.previous_move == 'A'):
                    for row in range(max(self.queen.ycoord-8, 0), min(self.queen.ycoord+self.queen.height + 8, self.queen.ysize)):
                        for col in range(max(self.queen.xcoord-20, 0), max(self.queen.xcoord-11, 0)):
                            if self.status[row][col] == 1:
                                self.queen.target_rows.append(row)
                                self.queen.target_cols.append(col)
                elif(self.queen.previous_move == 'D'):
                    for row in range(max(self.queen.ycoord-8, 0), min(self.queen.ycoord+self.queen.height + 8, self.king.ysize)):
                        for col in range(min(self.queen.xcoord+12, self.queen.xsize), min(self.queen.xcoord+21, self.queen.xsize)):
                            if self.status[row][col] == 1:
                                self.queen.target_rows.append(row)
                                self.queen.target_cols.append(col)
                elif(self.queen.previous_move == 'W'):
                    for row in range(max(self.queen.ycoord-20, 0), max(self.queen.ycoord-11, 0)):
                        for col in range(max(self.queen.xcoord-8, 0), min(self.queen.xcoord+self.queen.width + 8, self.king.xsize)):
                            if self.status[row][col] == 1:
                                self.queen.target_rows.append(row)
                                self.queen.target_cols.append(col)
                elif(self.queen.previous_move == 'S'):
                    for row in range(min(self.queen.ycoord+12, self.queen.ysize), min(self.queen.ycoord+21,self.queen.ysize)):
                        for col in range(max(self.queen.xcoord-8, 0), min(self.queen.xcoord+self.queen.width + 8, self.queen.xsize)):
                            if self.status[row][col] == 1:
                                self.queen.target_rows.append(row)
                                self.queen.target_cols.append(col)
                if(len(self.queen.target_rows) != 0 and len(self.queen.target_cols) != 0):
                    self.queen.times[self.queen.time_count] = current_time()
                    self.queen.qa[self.queen.time_count] = 1
                    self.queen.time_count += 1

                    #flag = 1
                    # break
                # check for huts
            for p in range(4):
                status.append(0)
            stat = 0
            for target_row, target_col in zip(self.queen.target_rows, self.queen.target_cols):
                if(status[0] == 0):
                    for p in range(5):
                        if self.huts[p].isattack == 0:
                            for row in range(self.huts[p].ycoord, self.huts[p].ycoord+self.huts[p].height):
                                for col in range(self.huts[p].xcoord, self.huts[p].xcoord+self.huts[p].width):
                                    if row == target_row and col == target_col:
                                        if(current_time() - self.queen.times[self.queen.attack_count] >= 1) and self.queen.qa[self.queen.attack_count] == 1:
                                            self.huts[p].colorpoints = self.huts[p].colorpoints - \
                                                self.king.damage
                                            if self.huts[p].colorpoints <= 0:
                                                self.huts[p].colorpoints = 0
                                                self.huts[p].isdamage = 1
                                                self.huts[p].bgcolor = Back.BLACK + \
                                                    ' '+Style.RESET_ALL
                                            elif (self.huts[p].colorpoints <= self.huts[p].health / 2) and (self.huts[p].colorpoints > self.huts[p].health / 4):
                                                self.huts[p].bgcolor = Back.YELLOW + \
                                                    ' '+Style.RESET_ALL
                                            elif (self.huts[p].colorpoints <= self.huts[p].health / 4) and (self.huts[p].colorpoints > 0):
                                                self.huts[p].bgcolor = Back.RED + \
                                                    ' '+Style.RESET_ALL
                                            self.huts[p].isattack = 1
                                            stat = 1
                                            status[0] = 1
                                            break
                                if status[0] == 1:
                                    break
                        status[0] = 0
            # check for walls
                if(status[1] == 0):
                    for p in range(150):
                        if self.walls[p].isattack == 0:
                            for row in range(self.walls[p].ycoord, self.walls[p].ycoord+self.walls[p].height):
                                for col in range(self.walls[p].xcoord, self.walls[p].xcoord+self.walls[p].width):
                                    if row == target_row and col == target_col:
                                        if(current_time() - self.queen.times[self.queen.attack_count] >= 1) and self.queen.qa[self.queen.attack_count] == 1:
                                            self.walls[p].colorpoints = self.walls[p].colorpoints - \
                                                self.king.damage
                                        if self.walls[p].colorpoints <= 0:
                                            self.walls[p].colorpoints = 0
                                            self.walls[p].isdamage = 1
                                            self.walls[p].bgcolor = Back.BLACK + \
                                                ' '+Style.RESET_ALL
                                            self.walls[p].isattack = 1
                                        stat = 1
                                        status[1] = 1
                                        break
                                if status[1] == 1:
                                    break
                        status[1] = 0

                # check for town hall
                if(status[2] == 0):
                    if self.town_hall.isattack == 0:
                        for row in range(self.town_hall.ycoord, self.town_hall.ycoord+self.town_hall.height):
                            for col in range(self.town_hall.xcoord, self.town_hall.xcoord+self.town_hall.width):
                                if row == target_row and col == target_col:
                                    if(current_time() - self.queen.times[self.queen.attack_count] >= 3) and self.queen.qa[self.queen.attack_count] == 1:
                                        self.town_hall.colorpoints = self.town_hall.colorpoints - self.king.damage
                                        if self.town_hall.colorpoints <= 0:
                                            self.town_hall.colorpoints = 0
                                            self.town_hall.isdamage = 1
                                            self.town_hall.bgcolor = Back.BLACK+' '+Style.RESET_ALL
                                        elif (self.town_hall.colorpoints <= self.town_hall.health / 2) and (self.town_hall.colorpoints > self.town_hall.health / 4):
                                            self.town_hall.bgcolor = Back.YELLOW+' '+Style.RESET_ALL
                                        elif (self.town_hall.colorpoints <= self.town_hall.health / 4) and (self.town_hall.colorpoints > 0):
                                            self.town_hall.bgcolor = Back.RED+' '+Style.RESET_ALL
                                        self.town_hall.isattack = 1
                                        stat = 1
                                        # print("Hello")
                                        # exit()
                                        status[2] = 1
                                        break
                            if status[2] == 1:
                                break

                # check for cannons
                if(status[3] == 0):
                    for p in range(2):
                        if self.cannons[p].isattack == 0:
                            for row in range(self.cannons[p].ycoord, self.cannons[p].ycoord+self.cannons[p].height):
                                for col in range(self.cannons[p].xcoord, self.cannons[p].xcoord+self.cannons[p].width):
                                    if row == target_row and col == target_col:
                                        if(current_time() - self.queen.times[self.queen.attack_count] >= 1) and self.queen.qa[self.queen.attack_count] == 1:
                                            self.cannons[p].colorpoints = self.cannons[p].colorpoints - \
                                                self.king.damage
                                            if self.cannons[p].colorpoints <= 0:
                                                self.cannons[p].colorpoints = 0
                                                self.cannons[p].isdamage = 1
                                                self.cannons[p].bgcolor = Back.BLACK + \
                                                    ' '+Style.RESET_ALL
                                            elif (self.cannons[p].colorpoints <= self.cannons[p].health / 2) and (self.cannons[p].colorpoints > self.cannons[p].health / 4):
                                                self.cannons[p].bgcolor = Back.YELLOW + \
                                                    ' '+Style.RESET_ALL
                                            elif (self.cannons[p].colorpoints <= self.cannons[p].health / 4) and (self.cannons[p].colorpoints > 0):
                                                self.cannons[p].bgcolor = Back.RED + \
                                                    ' '+Style.RESET_ALL
                                            stat = 1
                                            status[3] = 1
                                            self.cannons[p].isattack = 1
                                            break
                        if status[3] == 1:
                            break
                    status[3] = 0
            if(stat == 1):
                self.queen.qa[self.queen.attack_count] = 0
                self.queen.attack_count = self.queen.attack_count + 1

            for p in range(5):
                self.huts[p].isattack = 0
            for p in range(150):
                self.walls[p].isattack = 0
            self.town_hall.isattack = 0
            self.cannons[0].isattack = 0
            self.cannons[1].isattack = 0

        print("\n".join(["".join(row) for row in self.board]))
        if self.gameover == 0:
            flag = 0
            for p in range(5):
                if self.huts[p].isdamage == 0:
                    flag = 1
            if self.town_hall.isdamage == 0:
                flag = 1
            for p in range(2):
                if self.cannons[p].isdamage == 0:
                    flag = 1
            for p in range(2):
                if self.wizardtowers[p].isdamage == 0:
                    flag = 1
            if flag == 0:
                print("VICTORY")
                exit()
            for num in range(3):
                for p in range(2):
                    if self.troops[num][p].isdamage == 0:
                        flag = 1
            for num in range(3):
                for p in range(1):
                    if self.archers[num][p].isdamage == 0:
                        flag = 1
            for num in range(3):
                for p in range(2):
                    if self.balloons[num][p].isdamage == 0:
                        flag = 1
            if self.variable == 'k' and self.king.isdamage == 0:
                flag = 1
            if self.variable == 'q' and self.queen.isdamage == 0:
                flag = 1    
            if flag == 0:
                print("DEFEAT")
                exit()

    def user_input(self):
        char = userinput()
        self.input_char = char
      #  print(char)
        if(char == ' '):
            self.attack()
        elif(char == 'j'):
            if self.troops_count[0] < 2:
                self.troops[0][self.troops_count[0]
                               ].bgcolor = Back.CYAN + ' ' + Style.RESET_ALL
                self.troops[0][self.troops_count[0]].status = 1
                self.troops_count[0] += 1
        elif(char == 'k'):
            if self.troops_count[1] < 2:
                self.troops[1][self.troops_count[1]
                               ].bgcolor = Back.CYAN + ' ' + Style.RESET_ALL
                self.troops[1][self.troops_count[1]].status = 1
                self.troops_count[1] += 1
        elif(char == 'l'):
            if self.troops_count[2] < 2:
                self.troops[2][self.troops_count[2]
                               ].bgcolor = Back.CYAN + ' ' + Style.RESET_ALL
                self.troops[2][self.troops_count[2]].status = 1
                self.troops_count[2] += 1
        elif(char == 'b'):
            if self.archers_count[0] < 1:
                self.archers[0][self.archers_count[0]
                                ].bgcolor = Back.CYAN + ' ' + Style.RESET_ALL
                self.archers[0][self.archers_count[0]].status = 1
                self.archers_count[0] += 1
        elif(char == 'n'):
            if self.archers_count[1] < 1:
                self.archers[1][self.archers_count[1]
                                ].bgcolor = Back.CYAN + ' ' + Style.RESET_ALL
                self.archers[1][self.archers_count[1]].status = 1
                self.archers_count[1] += 1
        elif(char == 'm'):
            if self.archers_count[2] < 1:
                self.archers[2][self.archers_count[2]
                                ].bgcolor = Back.CYAN + ' ' + Style.RESET_ALL
                self.archers[2][self.archers_count[2]].status = 1
                self.archers_count[2] += 1
        elif(char == 'i'):
            if self.balloons_count[0] < 2:
                self.balloons[0][self.balloons_count[0]
                                 ].bgcolor = Back.LIGHTWHITE_EX + ' ' + Style.RESET_ALL
                self.balloons[0][self.balloons_count[0]].status = 1
                self.balloons_count[0] += 1
        elif(char == 'o'):
            if self.balloons_count[1] < 2:
                self.balloons[1][self.balloons_count[1]
                                 ].bgcolor = Back.LIGHTWHITE_EX + ' ' + Style.RESET_ALL
                self.balloons[1][self.balloons_count[1]].status = 1
                self.balloons_count[1] += 1
        elif(char == 'p'):
            if self.balloons_count[2] < 2:
                self.balloons[2][self.balloons_count[2]
                                 ].bgcolor = Back.LIGHTWHITE_EX + ' ' + Style.RESET_ALL
                self.balloons[2][self.balloons_count[2]].status = 1
                self.balloons_count[2] += 1

        elif(char == 'r'):
            self.rage_spell()
        elif(char == 'h'):
            self.heal_spell()
        elif(char == 'q'):
            exit()
        else:
            if(self.variable == 'k'):
                self.king.move_king(char, self.status)
            elif(self.variable == 'q'):
                self.queen.move_queen(char, self.status)
       # self.print()

    def attack(self):
        if self.variable == 'k':
            flag = 1
            target_rows = []
            target_cols = []
            status = []
            for p in range(4):
                status.append(0)
            for row in range(self.king.ycoord-5, self.king.ycoord+self.king.height + 6):
                for col in range(self.king.xcoord-5, self.king.xcoord+self.king.width+6):
                    if self.status[row][col] == 1 and math.sqrt((col-self.king.xcoord)**2 + (row-self.king.ycoord)**2) <= self.king.range:
                        target_rows.append(row)
                        target_cols.append(col)
                        #flag = 1
                        # break
            # check for huts
            for target_row, target_col in zip(target_rows, target_cols):
                if(status[0] == 0):
                    for p in range(5):
                        if self.huts[p].isattack == 0:
                            for row in range(self.huts[p].ycoord, self.huts[p].ycoord+self.huts[p].height):
                                for col in range(self.huts[p].xcoord, self.huts[p].xcoord+self.huts[p].width):
                                    if row == target_row and col == target_col:
                                        self.huts[p].colorpoints = self.huts[p].colorpoints - \
                                            self.king.damage
                                        if self.huts[p].colorpoints <= 0:
                                            self.huts[p].colorpoints = 0
                                            self.huts[p].isdamage = 1
                                            self.huts[p].bgcolor = Back.BLACK + \
                                                ' '+Style.RESET_ALL
                                        elif (self.huts[p].colorpoints <= self.huts[p].health / 2) and (self.huts[p].colorpoints > self.huts[p].health / 4):
                                            self.huts[p].bgcolor = Back.YELLOW + \
                                                ' '+Style.RESET_ALL
                                        elif (self.huts[p].colorpoints <= self.huts[p].health / 4) and (self.huts[p].colorpoints > 0):
                                            self.huts[p].bgcolor = Back.RED + \
                                                ' '+Style.RESET_ALL
                                        self.huts[p].isattack = 1

                                        status[0] = 1
                                        break
                                if status[0] == 1:
                                    break
                        status[0] = 0
            # check for walls
                if(status[1] == 0):
                    for p in range(175):
                        if self.walls[p].isattack == 0:
                            for row in range(self.walls[p].ycoord, self.walls[p].ycoord+self.walls[p].height):
                                for col in range(self.walls[p].xcoord, self.walls[p].xcoord+self.walls[p].width):
                                    if row == target_row and col == target_col:
                                        self.walls[p].colorpoints = self.walls[p].colorpoints - \
                                            self.king.damage
                                    if self.walls[p].colorpoints <= 0:
                                        self.walls[p].colorpoints = 0
                                        self.walls[p].isdamage = 1
                                        self.walls[p].bgcolor = Back.BLACK + \
                                            ' '+Style.RESET_ALL
                                        self.walls[p].isattack = 1
                                        status[1] = 1
                                        break
                                if status[1] == 1:
                                    break
                        status[1] = 0

                # check for town hall
                if(status[2] == 0):
                    if self.town_hall.isattack == 0:
                        for row in range(self.town_hall.ycoord, self.town_hall.ycoord+self.town_hall.height):
                            for col in range(self.town_hall.xcoord, self.town_hall.xcoord+self.town_hall.width):
                                if row == target_row and col == target_col:
                                    self.town_hall.colorpoints = self.town_hall.colorpoints - self.king.damage
                                    if self.town_hall.colorpoints <= 0:
                                        self.town_hall.colorpoints = 0
                                        self.town_hall.isdamage = 1
                                        self.town_hall.bgcolor = Back.BLACK+' '+Style.RESET_ALL
                                    elif (self.town_hall.colorpoints <= self.town_hall.health / 2) and (self.town_hall.colorpoints > self.town_hall.health / 4):
                                        self.town_hall.bgcolor = Back.YELLOW+' '+Style.RESET_ALL
                                    elif (self.town_hall.colorpoints <= self.town_hall.health / 4) and (self.town_hall.colorpoints > 0):
                                        self.town_hall.bgcolor = Back.RED+' '+Style.RESET_ALL
                                    self.town_hall.isattack = 1
                                    # print("Hello")
                                    # exit()
                                    status[2] = 1
                                    break
                            if status[2] == 1:
                                break

                # check for cannons
                if(status[3] == 0):
                    for p in range(2):
                        if self.cannons[p].isattack == 0:
                            for row in range(self.cannons[p].ycoord, self.cannons[p].ycoord+self.cannons[p].height):
                                for col in range(self.cannons[p].xcoord, self.cannons[p].xcoord+self.cannons[p].width):
                                    if row == target_row and col == target_col:
                                        self.cannons[p].colorpoints = self.cannons[p].colorpoints - \
                                            self.king.damage
                                        if self.cannons[p].colorpoints <= 0:
                                            self.cannons[p].colorpoints = 0
                                            self.cannons[p].isdamage = 1
                                            self.cannons[p].bgcolor = Back.BLACK + \
                                                ' '+Style.RESET_ALL
                                        elif (self.cannons[p].colorpoints <= self.cannons[p].health / 2) and (self.cannons[p].colorpoints > self.cannons[p].health / 4):
                                            self.cannons[p].bgcolor = Back.YELLOW + \
                                                ' '+Style.RESET_ALL
                                        elif (self.cannons[p].colorpoints <= self.cannons[p].health / 4) and (self.cannons[p].colorpoints > 0):
                                            self.cannons[p].bgcolor = Back.RED + \
                                                ' '+Style.RESET_ALL
                                        status[3] = 1
                                        self.cannons[p].isattack = 1
                                        break
                        if status[3] == 1:
                            break
                    status[3] = 0
            for p in range(5):
                self.huts[p].isattack = 0
            for p in range(150):
                self.walls[p].isattack = 0
            self.town_hall.isattack = 0
            self.cannons[0].isattack = 0
            self.cannons[1].isattack = 0

        elif(self.variable == 'q'):
            # attack all in 5x5 area whose center is 8 tiles away
            flag = 1
            target_rows = []
            target_cols = []
            status = []
            for p in range(4):
                status.append(0)
            if(self.queen.previous_move == 'A'):
                for row in range(max(self.queen.ycoord-1, 0), min(self.queen.ycoord+self.queen.height + 2, self.queen.ysize)):
                    for col in range(max(self.queen.xcoord-10, 0), max(self.queen.xcoord-5, 0)):
                        if self.status[row][col] == 1:
                            target_rows.append(row)
                            target_cols.append(col)

            elif(self.queen.previous_move == 'D'):
                for row in range(max(self.queen.ycoord-1, 0), min(self.queen.ycoord+self.queen.height + 2, self.king.ysize)):
                    for col in range(min(self.queen.xcoord+6, self.queen.xsize), min(self.queen.xcoord+11, self.queen.xsize)):
                        if self.status[row][col] == 1:
                            target_rows.append(row)
                            target_cols.append(col)
            elif(self.queen.previous_move == 'W'):
                for row in range(max(self.queen.ycoord-10, 0), max(self.queen.ycoord-5, 0)):
                    for col in range(max(self.queen.xcoord-1, 0), min(self.queen.xcoord+self.queen.width + 2, self.king.xsize)):
                        if self.status[row][col] == 1:
                            target_rows.append(row)
                            target_cols.append(col)
            elif(self.queen.previous_move == 'S'):
                for row in range(min(self.queen.ycoord+6, self.queen.ysize), min(self.queen.ycoord+11,self.queen.ysize)):
                    for col in range(max(self.queen.xcoord-1, 0), min(self.queen.xcoord+self.queen.width + 2, self.queen.xsize)):
                        if self.status[row][col] == 1:
                            target_rows.append(row)
                            target_cols.append(col)
                        #flag = 1
                        # break
            # check for huts
            for target_row, target_col in zip(target_rows, target_cols):
                if(status[0] == 0):
                    for p in range(5):
                        if self.huts[p].isattack == 0:
                            for row in range(self.huts[p].ycoord, self.huts[p].ycoord+self.huts[p].height):
                                for col in range(self.huts[p].xcoord, self.huts[p].xcoord+self.huts[p].width):
                                    if row == target_row and col == target_col:
                                        self.huts[p].colorpoints = self.huts[p].colorpoints - \
                                            self.king.damage
                                        if self.huts[p].colorpoints <= 0:
                                            self.huts[p].colorpoints = 0
                                            self.huts[p].isdamage = 1
                                            self.huts[p].bgcolor = Back.BLACK + \
                                                ' '+Style.RESET_ALL
                                        elif (self.huts[p].colorpoints <= self.huts[p].health / 2) and (self.huts[p].colorpoints > self.huts[p].health / 4):
                                            self.huts[p].bgcolor = Back.YELLOW + \
                                                ' '+Style.RESET_ALL
                                        elif (self.huts[p].colorpoints <= self.huts[p].health / 4) and (self.huts[p].colorpoints > 0):
                                            self.huts[p].bgcolor = Back.RED + \
                                                ' '+Style.RESET_ALL
                                        self.huts[p].isattack = 1
                                        status[0] = 1
                                        break
                                if status[0] == 1:
                                    break
                        status[0] = 0
            # check for walls
                if(status[1] == 0):
                    for p in range(175):
                        if self.walls[p].isattack == 0:
                            for row in range(self.walls[p].ycoord, self.walls[p].ycoord+self.walls[p].height):
                                for col in range(self.walls[p].xcoord, self.walls[p].xcoord+self.walls[p].width):
                                    if row == target_row and col == target_col:
                                        self.walls[p].colorpoints = self.walls[p].colorpoints - \
                                            self.king.damage
                                        if self.walls[p].colorpoints <= 0:
                                            self.walls[p].colorpoints = 0
                                            self.walls[p].isdamage = 1
                                            self.walls[p].bgcolor = Back.BLACK + \
                                                ' '+Style.RESET_ALL
                                            self.walls[p].isattack = 1
                                            status[1] = 1
                                            break
                                if status[1] == 1:
                                    break
                        status[1] = 0

                # check for town hall
                if(status[2] == 0):
                    if self.town_hall.isattack == 0:
                        for row in range(self.town_hall.ycoord, self.town_hall.ycoord+self.town_hall.height):
                            for col in range(self.town_hall.xcoord, self.town_hall.xcoord+self.town_hall.width):
                                if row == target_row and col == target_col:
                                    self.town_hall.colorpoints = self.town_hall.colorpoints - self.king.damage
                                    if self.town_hall.colorpoints <= 0:
                                        self.town_hall.colorpoints = 0
                                        self.town_hall.isdamage = 1
                                        self.town_hall.bgcolor = Back.BLACK+' '+Style.RESET_ALL
                                    elif (self.town_hall.colorpoints <= self.town_hall.health / 2) and (self.town_hall.colorpoints > self.town_hall.health / 4):
                                        self.town_hall.bgcolor = Back.YELLOW+' '+Style.RESET_ALL
                                    elif (self.town_hall.colorpoints <= self.town_hall.health / 4) and (self.town_hall.colorpoints > 0):
                                        self.town_hall.bgcolor = Back.RED+' '+Style.RESET_ALL
                                    self.town_hall.isattack = 1
                                    # print("Hello")
                                    # exit()
                                    status[2] = 1
                                    break
                            if status[2] == 1:
                                break

                # check for cannons
                if(status[3] == 0):
                    for p in range(2):
                        if self.cannons[p].isattack == 0:
                            for row in range(self.cannons[p].ycoord, self.cannons[p].ycoord+self.cannons[p].height):
                                for col in range(self.cannons[p].xcoord, self.cannons[p].xcoord+self.cannons[p].width):
                                    if row == target_row and col == target_col:
                                        self.cannons[p].colorpoints = self.cannons[p].colorpoints - \
                                            self.king.damage
                                        if self.cannons[p].colorpoints <= 0:
                                            self.cannons[p].colorpoints = 0
                                            self.cannons[p].isdamage = 1
                                            self.cannons[p].bgcolor = Back.BLACK + \
                                                ' '+Style.RESET_ALL
                                        elif (self.cannons[p].colorpoints <= self.cannons[p].health / 2) and (self.cannons[p].colorpoints > self.cannons[p].health / 4):
                                            self.cannons[p].bgcolor = Back.YELLOW + \
                                                ' '+Style.RESET_ALL
                                        elif (self.cannons[p].colorpoints <= self.cannons[p].health / 4) and (self.cannons[p].colorpoints > 0):
                                            self.cannons[p].bgcolor = Back.RED + \
                                                ' '+Style.RESET_ALL
                                        status[3] = 1
                                        self.cannons[p].isattack = 1
                                        break
                        if status[3] == 1:
                            break
                    status[3] = 0
            for p in range(5):
                self.huts[p].isattack = 0
            for p in range(150):
                self.walls[p].isattack = 0
            self.town_hall.isattack = 0
            self.cannons[0].isattack = 0
            self.cannons[1].isattack = 0

    def rage_spell(self):
        for num in range(3):
            for p in range(2):
                if self.troops[num][p].isdamage == 0 and self.troops[num][p].status == 1 and self.troops[num][p].rage_spell == 0:
                    self.troops[num][p].damage = self.troops[num][p].damage * 2
                    self.troops[num][p].rage_spell = 1
        if self.variable == 'k':
            if self.king.isdamage == 0 and self.king.rage_spell == 0:
                self.king.damage = self.king.damage * 2
                self.king.rage_spell = 1
        elif(self.variable == 'q'):
            if self.queen.isdamage == 0 and self.queen.rage_spell == 0:
                self.queen.damage = self.queen.damage * 2
                self.queen.rage_spell = 1

    def heal_spell(self):
        for num in range(3):
            for p in range(2):
                if self.troops[num][p].isdamage == 0 and self.troops[num][p].status == 1 and self.troops[num][p].heal_spell == 0:
                    self.troops[num][p].health = self.troops[num][p].health * \
                        (3/2)
                    self.troops[num][p].heal_spell = 1
        if self.variable == 'k':
            if self.king.isdamage == 0 and self.king.heal_spell == 0:
                self.king.health = self.king.health * (3/2)
                self.king.len = 30 * self.king.health / self.king.maxhealth
                self.king.heal_spell = 1
        elif(self.variable == 'q'):
            if self.queen.isdamage == 0 and self.queen.heal_spell == 0:
                self.queen.health = self.queen.health * (3/2)
                self.queen.len = 30 * self.queen.health / self.queen.maxhealth
                self.queen.heal_spell = 1
