import sys
sys.path.insert(0, './src')
from src.village import *
from src.king import *
from src.building import *
from src.queen import *
from input import *
from time import sleep
village = Village()
village.build_walls()
village.build_troops()
village.build_archers()
village.build_balloons()
print("Enter q for queen and k for king :")
var = input()
village.variable = var
while(True):
    check = village.user_input()
    if(check == 'q'):
        break
    if village.print() == True:
        break
